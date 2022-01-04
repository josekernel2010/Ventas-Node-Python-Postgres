const express = require("express");
const router = express.Router();
const productoContrller = require("../controller/producto");

router.get("/todos", productoContrller.todos);
router.get("/buscar/:id", productoContrller.buscar);
router.post("/registro", productoContrller.registro);
router.post("/modificacion/:id", productoContrller.modificacion);
router.post("/eliminar/:id", productoContrller.eliminar);

module.exports = router;
