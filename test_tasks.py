import pytest
from task_manager import create_task, get_task, update_task_status, delete_task, tasks

@pytest.fixture(autouse=True)
def cleanup_tasks():
    tasks.clear()
    yield

def test_create_and_get_task():
    task_id = create_task("Teste", "Descricao", "Media", "2025-01-01")
    task = get_task(task_id)
    assert task is not None
    assert task['title'] == "Teste"

def test_update_task_status():
    task_id = create_task("Front", "React", "Alta")
    success = update_task_status(task_id, "Concluído")
    task = get_task(task_id)
    assert success is True
    assert task['status'] == "Concluído"

def test_delete_task():
    task_id = create_task("Code Review", "Sprint 1", "Media")
    success = delete_task(task_id)
    task = get_task(task_id)
    assert success is True
    assert task is None

def test_create_task_with_missing_fields():
    with pytest.raises(ValueError):
        create_task("", "Valida", "Baixa")