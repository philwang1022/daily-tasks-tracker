import json
from main import load_tasks, save_tasks

def test_save_and_load(tmp_path):
    test_file = tmp_path / "tasks.json"
    tasks = [{"title": "Test Task", "done": False}]
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
    with open(test_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded[0]["title"] == "Test Task"
