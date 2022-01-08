// express requiere para crear rutas
// importamos el módulo express
const express = require("express");
// le asignamos el .Router
const router = express.Router();
// aquí ponemos la ruta del controlador
const productoContrller = require("../controller/producto");

//Rutas de producto
router.get("/todos", productoContrller.todos);
router.get("/buscar/:id", productoContrller.buscar);
router.post("/registro", productoContrller.registro);
router.post("/modificacion/:id", productoContrller.modificacion);
router.post("/eliminar/:id", productoContrller.eliminar);

// exportamos router
module.exports = router;
