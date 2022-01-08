// módulo "pg" y clase Pool para generar las conecciones a la base de datos
const Pool = require("pg").Pool;

// instancia de pool con las caracteristicas de la coneccion
const pool = new Pool({
  user: process.env.USER,
  host: process.env.HOST,
  database: process.env.DATABASE,
  password: process.env.PASSWORD,
  port: process.env.PORT,
});

// exportando el módulo pool
module.exports = { pool };
