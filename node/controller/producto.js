const { pool } = require("../conexion");

const todos = (req, res) => {
  const sql = "SELECT * FROM producto order by id";
  pool.query(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send(result.rows);
    }
  });
};

const buscar = (req, res) => {
  const id = req.params.id;
  const sql = `SELECT * FROM producto where id=${id}`;
  pool.query(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send(result.rows);
    }
  });
};

const registro = (req, res) => {
  const nombre = req.body.nombre;
  const descripcion = req.body.descripcion;
  const precio = req.body.precio;
  const sql = `INSERT INTO producto (nombre, descripcion, precio)
         VALUES ('${nombre}', '${descripcion}', ${precio})`;
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send("Registro exitoso");
    }
  });
};

const modificacion = (req, res) => {
  const id = req.params.id;
  const campo = req.body.campo;
  const nuevoValor = req.body.nuevoValor;
  const sql = "";
  if (campo == "1") {
    sql = `UPDATE producto SET nombre = '${nuevoValor}' WHERE id = ${id}`;
  } else if (campo == "2") {
    sql = `UPDATE producto SET descripcion = '${nuevoValor}' WHERE id = ${id}`;
  } else if (campo == "3") {
    sql = `UPDATE producto SET precio = ${nuevoValor} WHERE id = ${id}`;
  }
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send("Modificación exitosa");
    }
  });
};

const eliminar = (req, res) => {
  const id = req.params.id;
  const sql = `DELETE FROM producto WHERE id = ${id}`;
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send("Eliminación exitosa");
    }
  });
};

module.exports = { todos, buscar, registro, modificacion, eliminar };
