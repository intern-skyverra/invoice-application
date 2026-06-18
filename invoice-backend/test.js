require("dotenv").config();

const db = require("./src/config/db");

async function testDB() {
  try {
    const [rows] = await db.query("SELECT 1");
    console.log("✅ Database Connected Successfully");
    console.log(rows);
  } catch (err) {
    console.error("❌ Database Error");
    console.error(err.message);
  }
}

testDB();