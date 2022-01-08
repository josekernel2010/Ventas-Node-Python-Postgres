// importamos la coneccion llamando a pool y la ruta de coneccion
const { pool } = require("../conexion");

// creamos funcion que va a contener una consulta sql
const todos = (req, res) => {
  const sql = "SELECT * FROM producto";
  /*ejecutamos la sentencia mediante .query donde 
 le pasamos la sentencia y si hay err o nos responde un resultado*/
  pool.query(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      // enviamos el resultado .rows para que nos muestre las filas
      res.send(result.rows);
    }
  });
};

// funcion de busqueda
const buscar = (req, res) => {
  // pasamos el id como parametros y le vamos a indicar que sea el id
  const id = req.params.id;
  // en la sentencia concatenamos el id
  const sql = `SELECT * FROM producto where id=${id}`;
  //ejecutamos la sentencia mediante .query
  pool.query(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send(result.rows);
    }
  });
};

const registro = (req, res) => {
  // req.body nos sirve para obtener los valores desde python
  const nombre = req.body.nombre;
  const descripcion = req.body.descripcion;
  const precio = req.body.precio;
  const sql = `INSERT INTO producto (nombre, descripcion, precio)
         VALUES ('${nombre}', '${descripcion}', ${precio})`;
  //ejecutamos la sentencia mediante .query
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send("Registro exitoso");
    }
  });
};

const modificacion = (req, res) => {
  // req.params.id el id de la base de datos
  const id = req.params.id;
  //los valores desde python req.body
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
  //ejecutamos la sentencia mediante .query
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send("Modificación exitosa");
    }
  });
};

const eliminar = (req, res) => {
  // pasamos el id como parametros y le vamos a indicar que sea el id
  const id = req.params.id;
  // en la sentencia concatenamos el id
  const sql = `DELETE FROM producto WHERE id = ${id}`;
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error " + err);
    } else {
      res.send("Eliminación exitosa");
    }
  });
};

// exportamos todas las funciones
module.exports = { todos, buscar, registro, modificacion, eliminar };
