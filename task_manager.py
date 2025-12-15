import uuid

# Simulação de um "banco de dados" em memória
tasks = {}

def create_task(title: str, description: str, priority: str, due_date: str = "N/A"):
    """Cria uma nova tarefa e a armazena no dicionário de tarefas."""
    if not title or not description or not priority:
        raise ValueError("Título, descrição e prioridade são obrigatórios.")

    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Pendente",
        "due_date": due_date 
    }
    return task_id

def get_task(task_id: str):
    return tasks.get(task_id)

def update_task_status(task_id: str, new_status: str):
    task = tasks.get(task_id)
    if task:
        task["status"] = new_status
        return True
    return False

def delete_task(task_id: str):
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

def list_tasks():
    return tasks