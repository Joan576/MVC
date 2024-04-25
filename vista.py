class View:
    def show_tasks(self, tasks):
        print("Lista de tareas:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completada" if task.completed else "Pendiente"
            print(f"{idx}. {task.title} - {task.description} ({status})")

    def get_task_input(self):
        title = input("Ingrese el título de la tarea: ")
        description = input("Ingrese la descripción de la tarea: ")
        return title, description