def agregar_tarea(tareas, titulo, categoria="General"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    if not isinstance(categoria, str) or not categoria.strip():
        raise ValueError("La categoría es obligatoria")
    tarea = {
        "id": max((tarea["id"] for tarea in tareas), default=0) + 1,
        "titulo": titulo,
        "categoria": categoria.strip(),
        "completada": False,
    }
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def eliminar_tarea(tareas, tarea_id):
    for indice, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(indice)
    raise ValueError("Tarea no encontrada")


def pendientes(tareas, categoria=None):
    tareas_pendientes = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return tareas_pendientes

    categoria = categoria.strip().casefold()
    if not categoria:
        return []
    return [
        tarea for tarea in tareas_pendientes
        if tarea.get("categoria", "").casefold() == categoria
    ]
