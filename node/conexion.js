const Pool = require("pg").Pool;

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "ventas",
  password: "1079",
  port: 5432,
});

module.exports = pool;
