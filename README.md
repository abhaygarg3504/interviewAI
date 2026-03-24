# Smart Prep - AI-Powered Interview Preparation Platform

Smart Prep is a comprehensive AI-driven platform designed to help users prepare for job interviews through interactive mock interviews, real-time feedback, and personalized reports. The platform leverages advanced AI technologies including speech recognition, natural language processing, and computer vision to provide an immersive interview experience.

## 🚀 Features

### Core Functionality
- **User Authentication**: Secure login and registration system with JWT tokens
- **Resume Upload & Analysis**: PDF resume parsing and intelligent analysis
- **Mock Interviews**: AI-powered interview simulations with customizable scenarios
- **Real-time Speech Recognition**: Convert speech to text using OpenAI Whisper
- **Text-to-Speech**: Generate natural-sounding responses using MMS-TTS
- **Face Detection**: Monitor user engagement and expressions during interviews
- **Performance Reports**: Detailed feedback and scoring on interview performance
- **User Manual**: Comprehensive guide for platform usage

### Technical Features
- **Multi-modal Interaction**: Support for audio, video, and text inputs
- **Cloud Storage**: Secure file storage using Cloudinary
- **Database Integration**: MongoDB for user data and session management
- **Real-time Communication**: WebRTC-based video conferencing capabilities
- **AI-Powered Analysis**: Google Cloud AI services for advanced processing

## 🏗️ Architecture

The application follows a microservices architecture with three main components:

### Backend (Node.js/Express)
- **Framework**: Express.js with ES6 modules
- **Database**: MongoDB with Mongoose ODM
- **Authentication**: JWT-based auth with bcrypt password hashing
- **File Handling**: Multer for multipart uploads, Cloudinary for cloud storage
- **AI Services**: Integration with Google Cloud Speech-to-Text, Text-to-Speech, and Generative AI
- **Media Processing**: FFmpeg for audio/video processing

### Frontend (React/Vite)
- **Framework**: React 19 with Vite build tool
- **UI Library**: Material-UI (MUI) for modern, responsive design
- **Routing**: React Router for client-side navigation
- **State Management**: React Context API
- **Real-time Features**: Webcam integration with face-api.js and MediaPipe
- **PDF Processing**: PDF.js for client-side PDF parsing
- **Notifications**: React Toastify for user feedback

### Transformer API (Python/FastAPI)
- **Framework**: FastAPI for high-performance async API
- **Speech Processing**: OpenAI Whisper for speech-to-text
- **Text Generation**: Facebook MMS-TTS for text-to-speech
- **Audio Processing**: SoundFile and SciPy for audio manipulation

## 📁 Project Structure

```
Smart-Prep/
├── Backend/                          # Node.js Express Server
│   ├── package.json                  # Backend dependencies
│   ├── server.js                     # Main server file
│   ├── Controller/                   # Business logic controllers
│   │   ├── auth.js                   # Authentication controller
│   │   ├── AuthDB.js                 # Auth database operations
│   │   ├── ChatDB.js                 # Chat database operations
│   │   └── Speech.js                 # Speech processing controller
│   ├── MiddleWare/                   # Express middleware
│   │   ├── auth.js                   # Authentication middleware
│   │   └── error.js                  # Error handling middleware
│   └── Routes/                       # API route definitions
│       ├── auth.js                   # Authentication routes
│       └── Speech.js                 # Speech-related routes
├── Client/                           # React Frontend
│   ├── package.json                  # Frontend dependencies
│   ├── vite.config.js                # Vite configuration
│   ├── index.html                    # HTML template
│   ├── src/
│   │   ├── App.jsx                   # Main React component
│   │   ├── main.jsx                  # React entry point
│   │   ├── App.css                   # Global styles
│   │   ├── index.css                 # Base styles
│   │   ├── assets/                   # Static assets
│   │   └── Components/               # React components
│   │       ├── Forms/                # Authentication forms
│   │       │   ├── Login.jsx         # Login component
│   │       │   └── Register.jsx      # Registration component
│   │       ├── Home/                 # Home page components
│   │       │   ├── Home.jsx          # Main home component
│   │       │   ├── Header.jsx        # Navigation header
│   │       │   ├── Report.jsx        # Performance reports
│   │       │   └── UserManual.jsx    # User guide
│   │       ├── Room.jsx              # Interview room component
│   │       ├── Loading.jsx           # Loading spinner
│   │       └── Loader.jsx            # Custom loader
│   └── public/                       # Public assets
└── Transformer-API/                  # Python AI Services
    ├── app.py                        # FastAPI application
    └── __pycache__/                  # Python bytecode cache
```

## 🛠️ Technology Stack

### Backend
- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: MongoDB
- **Authentication**: JSON Web Tokens (JWT)
- **Password Hashing**: bcrypt
- **File Upload**: Multer
- **Cloud Storage**: Cloudinary
- **AI Services**: Google Cloud AI
- **Media Processing**: FFmpeg
- **PDF Parsing**: pdf-parse, pdfjs-dist

### Frontend
- **Runtime**: Node.js
- **Framework**: React 19
- **Build Tool**: Vite
- **UI Library**: Material-UI
- **Icons**: Lucide React
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **Notifications**: React Toastify
- **Webcam**: React Webcam
- **Face Detection**: face-api.js, MediaPipe
- **PDF Processing**: PDF.js

### AI Services
- **Runtime**: Python 3.x
- **Framework**: FastAPI
- **Speech-to-Text**: OpenAI Whisper
- **Text-to-Speech**: Facebook MMS-TTS
- **Audio Processing**: SoundFile, SciPy, NumPy

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8+
- MongoDB
- Google Cloud Account (for AI services)
- Cloudinary Account (for file storage)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhaygarg3504/interviewAI.git
   cd Smart-Prep
   ```

2. **Backend Setup**
   ```bash
   cd Backend
   npm install
   # Create .env file with required environment variables
   npm run dev
   ```

3. **Frontend Setup**
   ```bash
   cd ../Client
   npm install
   npm run dev
   ```

4. **Transformer API Setup**
   ```bash
   cd ../Transformer-API
   pip install -r requirements.txt
   python app.py
   ```

### Environment Variables

Create `.env` files in the respective directories:

**Backend/.env**
```
PORT=5000
MONGO_URL=mongodb://localhost:27017/smartprep
JWT_SECRET=your_jwt_secret
FRONTEND_URL=http://localhost:5173
TRANSFORMERS_API_URL=http://localhost:8000
GOOGLE_CLOUD_PROJECT_ID=your_project_id
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

**Client/.env**
```
VITE_API_URL=http://localhost:5000
```

## 📡 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/getuser` - Get current user info
- `POST /auth/logout` - User logout

### Speech Processing
- `POST /speech/stt` - Speech to text conversion
- `POST /speech/tts` - Text to speech conversion
- `POST /speech/analyze` - Analyze interview responses

## 🎯 Usage

1. **Registration/Login**: Create an account or log in
2. **Profile Setup**: Upload your resume and enter professional details
3. **Interview Preparation**: Choose interview type and difficulty
4. **Mock Interview**: Participate in AI-powered interview sessions
5. **Review Feedback**: Analyze performance reports and improve

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for Whisper speech recognition
- Google Cloud for AI services
- Facebook Research for MMS-TTS
- Material-UI for UI components
- All contributors and open-source projects used

## 📞 Support

For support, email support@smartprep.com or join our Discord community.

---

**Made with ❤️ for interview preparation**