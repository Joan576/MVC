from modelo import Task
from vista import View

class Controller:
    def __init__(self):
        self.tasks = []
        self.view = View()

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def show_tasks(self):
        self.view.show_tasks(self.tasks)

    def run(self):
        while True:
            choice = input("1. Mostrar tareas\n2. Agregar tarea\n3. Salir\nIngrese su elección: ")
            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                title, description = self.view.get_task_input()
                self.add_task(title, description)
            elif choice == '3':
                break
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")


if __name__ == "__main__":
    controller = Controller()
    controller.run()