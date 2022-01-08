// importamos el modúlo express
const express = require("express");
// a esta variable le asignamos la ruta de conección
const conexion = require("./conexion");

// importamos las rutas desde la ruta del archivo
const productoRouter = require("./route/producto");

// creando la aplicacion apartir de express
const app = express();

// middleware para poder leer los datos que vengan desde python
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// se activa con el prefijo /producto todas las rutas de ruter
app.use("/producto", productoRouter);

// que la aplicacion escuche por el puerto 3000
app.listen(3000, () => {
  console.log("Aplicación corriendo en el puerto 3000");
});
