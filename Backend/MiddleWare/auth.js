import jwt from "jsonwebtoken";

export const authenticator = async (req, res, next) => {
  try {
    const { token } = req.cookies;

    console.log("Authenticating...");

    if (!token) {
      return res.status(401).json({
        success: false,
        message: "Not authorized"
      });
    }

    const decoded = jwt.verify(token, process.env.JWT_KEY);

    req.user = decoded;

    next();

  } catch (error) {
    return res.status(401).json({
      success: false,
      message: "Invalid or expired token"
    });
  }
};