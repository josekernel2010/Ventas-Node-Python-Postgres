// importamos la coneccion llamando a pool y la ruta de coneccion
const { pool } = require("../conexion");

/*1. Sentencia para mostrar la tabla sql*/
const todos = (req, res) => {
  const sql = "SELECT * FROM producto";
  /*ejecutamos la sentencia mediante .query donde 
 le pasamos la sentencia y si hay err o nos responde un resultado*/
  pool.query(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error !!!" + err);
    } else {
      // enviamos el resultado .rows para que nos muestre las filas
      res.send(result.rows);
    }
  });
};

/*2. Sentencia de busqueda*/
const buscar = (req, res) => {
  // pasamos el id como parametros y le vamos a indicar que sea el id
  const id = req.params.id;
  // en la sentencia concatenamos el id $1 en postgresql
  const sql = `SELECT * FROM producto where id=$1;`;
  /*  para evitar inyeccion de sql (1 or 1=1) muestra toda la tabla
   */

  //const sql = `SELECT * FROM producto where id = ?`;
  //ejecutamos la sentencia mediante .query
  pool.query(sql, [id], (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error !!!" + err);
    } else {
      res.send(result.rows);
    }
  });
};

/*3. Sentencia de registro */
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
      res.send("Ha ocurrido un error !!!" + err);
    } else {
      res.send("::Registro exitoso::");
    }
  });
};

/*4. Sentencia de Modificación "update, set" */
const modificar = (req, res) => {
  // req.params.id el id de la base de datos
  const id = req.params.id;
  //los valores desde python req.body
  const campo = req.body.campo;
  const nuevoValor = req.body.nuevoValor;
  // variable sin definir para la sentencia
  sql = "";
  if (campo == "1") {
    sql = `update producto set nombre='${nuevoValor}' where id=${id}`;
  } else if (campo == "2") {
    sql = `update producto set descripcion='${nuevoValor}' where id=${id}`;
  } else if (campo == "3") {
    sql = `update producto set precio='${nuevoValor}' where id=${id}`;
  }
  //ejecutamos la sentencia mediante .query
  pool.query(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error !!!" + err);
    } else {
      res.send("::Modificación exitosa::");
    }
  });
};

/*5. Sentencia Delete */
const eliminar = (req, res) => {
  // pasamos el id como parametros y le vamos a indicar que sea el id
  const id = req.params.id;
  // en la sentencia concatenamos el id
  const sql = `DELETE FROM producto WHERE id = $1`;
  pool.query(sql, [id], (err) => {
    if (err) {
      res.send("Ha ocurrido un error !!!" + err);
    } else {
      res.send("::Eliminación exitosa::");
    }
  });
};

// exportamos todas las funciones
module.exports = { todos, buscar, registro, modificar, eliminar };
