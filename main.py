class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        """
        Добавляет новую задачу в список.
        :param description: Описание задачи
        :param due_date: Срок выполнения
        """
        self.tasks.append({"description": description, "due_date": due_date, "status": False})

    def mark_as_done(self, description):
        """
        Отмечает задачу как выполненную.
        :param description: Описание задачи
        """
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = True
                print(f"Задача '{description}' отмечена как выполненная.")
                break
        else:
            print(f"Задача с описанием '{description}' не найдена.")

    def current_tasks(self):
        """
        Печатает список не выполненных задач.
        """
        print("Текущие задачи:")
        for task in self.tasks:
            if not task["status"]:
                print(f"Описание: {task['description']}, Срок: {task['due_date']}")


# Пример использования
if __name__ == "__main__":
    task_manager = Task()

    # Добавим несколько задач
    task_manager.add_task("Купить молоко", "2024-04-20")
    task_manager.add_task("Прочитать книгу", "2024-04-25")

    # Выведем текущие задачи
    task_manager.current_tasks()

    # Отметим одну задачу как выполненную
    task_manager.mark_as_done("Купить молоко")

    # Снова выведем текущие задачи, чтобы увидеть изменения
    task_manager.current_tasks()
