// express requiere para crear rutas
// importamos el módulo express
const express = require("express");
// le asignamos el .Router
const router = express.Router();
// aquí ponemos la ruta del controlador
const productoController = require("../controller/producto");

//Rutas de producto
router.get("/todos", productoController.todos);
router.get("/buscar/:id", productoController.buscar);
router.post("/registro", productoController.registro);
router.post("/modificar/:id", productoController.modificar);
router.post("/eliminar/:id", productoController.eliminar);

// exportamos router
module.exports = router;
