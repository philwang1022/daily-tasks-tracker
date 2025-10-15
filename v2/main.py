import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ 新增任務：{title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("目前沒有任務。")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎉 完成任務：{tasks[index - 1]['title']}")
    else:
        print("❌ 無效的任務編號")

if __name__ == "__main__":
    print("== Daily Tasks Tracker ==")
    print("指令：add/list/done/exit")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "exit":
            break
        elif cmd == "list":
            list_tasks()
        elif cmd.startswith("add "):
            _, title = cmd.split(" ", 1)
            add_task(title)
        elif cmd.startswith("done "):
            try:
                index = int(cmd.split(" ")[1])
                complete_task(index)
            except ValueError:
                print("請輸入有效的任務編號。")
        else:
            print("未知指令。")
