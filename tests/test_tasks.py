import unittest
from tasks import agregar_tarea, completar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])
        self.assertEqual(tarea["categoria"], "General")

    def test_agregar_tarea_con_categoria(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", " Estudio ")
        self.assertEqual(tarea["categoria"], "Estudio")

    def test_agregar_tarea_con_categoria_vacia(self):
        for categoria in ("", "   "):
            with self.subTest(categoria=categoria):
                tareas = []
                with self.assertRaisesRegex(ValueError, "La categoría es obligatoria"):
                    agregar_tarea(tareas, "Leer documentación", categoria)
                self.assertEqual(tareas, [])

    def test_filtrar_pendientes_por_categoria(self):
        tareas = []
        estudio = agregar_tarea(tareas, "Leer documentación", "Estudio")
        practica = agregar_tarea(tareas, "Practicar", "Práctica")
        completada = agregar_tarea(tareas, "Repasar", "Estudio")
        completar_tarea(tareas, completada["id"])

        self.assertEqual(pendientes(tareas, " eSTUDIO "), [estudio])
        self.assertEqual(pendientes(tareas, "Otro"), [])
        self.assertEqual(pendientes(tareas), [estudio, practica])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])


if __name__ == "__main__":
    unittest.main()
