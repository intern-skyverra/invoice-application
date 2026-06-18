const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

const User = require("../models/userModel");

const signup = async (data) => {

  const existing = await User.findByEmail(data.email);

  if (existing)
    throw new Error("Email already exists");

  const hashedPassword =
    await bcrypt.hash(data.password, 10);

  const userId = await User.createUser(
    data.fullName,
    data.email,
    hashedPassword
  );

  const token = jwt.sign(
    { id: userId },
    process.env.JWT_SECRET,
    {
      expiresIn:
        process.env.JWT_EXPIRES_IN
    }
  );

  return token;
};

const login = async (data) => {

  const user = await User.findByEmail(
    data.email
  );

  if (!user)
    throw new Error("Invalid credentials");

  const match =
    await bcrypt.compare(
      data.password,
      user.password
    );

  if (!match)
    throw new Error("Invalid credentials");

  const token = jwt.sign(
    { id: user.id },
    process.env.JWT_SECRET,
    {
      expiresIn:
        process.env.JWT_EXPIRES_IN
    }
  );

  return token;
};

module.exports = {
  signup,
  login
};