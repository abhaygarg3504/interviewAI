# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import StreamingResponse
# from transformers import pipeline
# import tempfile
# import shutil
# import io
# from gtts import gTTS

# app = FastAPI()

# # Speech → Text model
# stt = pipeline("automatic-speech-recognition", model="openai/whisper-base")

# @app.get("/")
# def health():
#     return {"status": "running"}

# @app.post("/stt")
# async def speech_to_text(file: UploadFile = File(...)):

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
#         shutil.copyfileobj(file.file, tmp)
#         path = tmp.name

#     result = stt(path)

#     return {"text": result["text"]}


# @app.post("/tts")
# async def text_to_speech(data: dict):

#     text = data["text"]

#     tts = gTTS(text)

#     buffer = io.BytesIO()
#     tts.write_to_fp(buffer)
#     buffer.seek(0)

#     return StreamingResponse(buffer, media_type="audio/mp3")
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse,Response
import torch
from transformers import pipeline
import tempfile
from scipy.io.wavfile import write as wav_write
import io
from io import BytesIO
import soundfile as sf
import numpy as np
import uvicorn

app = FastAPI()


print("Loading STT model...")
stt_model = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    device="cpu"
) 


print("Loading TTS model...")
tts = pipeline(
    "text-to-speech",
    model="facebook/mms-tts-eng",
    device=-1  
)


@app.post("/stt")
async def speech_to_text(file: UploadFile):
    print('stt')
    audio_bytes = await file.read()
    audio, sample_rate = sf.read(io.BytesIO(audio_bytes))
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    result = stt_model({
        "array": audio,
        "sampling_rate": sample_rate
    })

    return {"text": result["text"]}


@app.post("/tts")
async def text_to_speech(payload: dict):
     print('tts')
     text = payload["text"]

     out = tts(text)

     audio = out["audio"]
     sample_rate = int(out["sampling_rate"])  

     audio = np.asarray(audio).squeeze()

     audio = np.nan_to_num(audio)

     audio = np.clip(audio, -1.0, 1.0)
     audio = (audio * 32767).astype(np.int16)

     buffer = BytesIO()
     wav_write(buffer, sample_rate, audio)  
     buffer.seek(0)
     return Response(
        content=buffer.read(),
        media_type="audio/wav"
    )

@app.get("/")
def health():
    return {"status": "ok"}
\
