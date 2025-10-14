import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("目前沒有任務！")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("輸入任務名稱：")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ 任務已新增！")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("輸入要標記完成的任務編號：")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("✅ 任務已完成！")
    except (ValueError, IndexError):
        print("❌ 無效的編號！")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("輸入要刪除的任務編號：")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑 已刪除任務：{removed['title']}")
    except (ValueError, IndexError):
        print("❌ 無效的編號！")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== 每日任務追蹤器 =====")
        print("1. 查看任務")
        print("2. 新增任務")
        print("3. 標記完成")
        print("4. 刪除任務")
        print("5. 離開")

        choice = input("選擇功能：")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 再見！")
            break
        else:
            print("❌ 無效的選擇！")

if __name__ == "__main__":
    main()
