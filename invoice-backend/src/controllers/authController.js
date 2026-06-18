const authService =require("../services/authService");

const {
  signupSchema,
  loginSchema
} = require("../utils/validator");

exports.signup = async (req,res) => {

  try {

    const { error } =
      signupSchema.validate(req.body);

    if(error)
      return res.status(400).json({
        message:error.details[0].message
      });

    const token =
      await authService.signup(req.body);

    res.status(201).json({
      token
    });

  } catch(err){

    res.status(400).json({
      message:err.message
    });

  }
};

exports.login = async (req,res) => {

  try {

    const { error } =
      loginSchema.validate(req.body);

    if(error)
      return res.status(400).json({
        message:error.details[0].message
      });

    const token =
      await authService.login(req.body);

    res.status(200).json({
      token
    });

  } catch(err){

    res.status(400).json({
      message:err.message
    });

  }
}