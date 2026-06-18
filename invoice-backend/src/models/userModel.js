const db = require("../config/db");

const findByEmail = async (email) => {
  const [rows] = await db.execute(
    "SELECT * FROM users WHERE email=?",
    [email]
  );

  return rows[0];
};

const createUser = async (fullName, email, password) => {
  const [result] = await db.execute(
    `INSERT INTO users
     (full_name,email,password)
     VALUES(?,?,?)`,
    [fullName, email, password]
  );

  return result.insertId;
};

const findById = async (id) => {
  const [rows] = await db.execute(
    `SELECT id,full_name,email
     FROM users
     WHERE id=?`,
    [id]
  );

  return rows[0];
};

module.exports = {
  findByEmail,
  createUser,
  findById
};