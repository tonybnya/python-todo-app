#!/usr/bin/env python3

"""
Author      : tonybnya
Date        : 2021
Description : app.py - a todolist app with pop-up notifications.
              For persistence, data are stored in a text file.
"""

import sys
import colorama
from colorama import Fore, Style
from beepy import beep
from pynotifier import Notification
from task import Task

colorama.init(autoreset=True)

MENU = "./menu.txt"
DB_FILE = "./todolist.txt"


def add(task):
    """Function to add a task object to the todolist"""

    # Open the DB file in append & read mode ('a+')
    with open(DB_FILE, "a+") as file_obj:
        # Move read cursor to the start of file
        file_obj.seek(0)
        # Get the content of the file
        data = file_obj.read()
        # If file is not empty, append '\n'
        if len(data) > 0:
            file_obj.write("\n")

        # Append text at the end of file
        file_obj.write(task)


def list_tasks():
    """Function to list all the tasks registered"""

    # Call `open_file` function
    content = open_file(DB_FILE)

    # Check if the file is empty
    if len(content) == 0:
        print("No task added yet.")
        popup("No task added yet.")

    # Check if the file is not empty
    if len(content) > 0:
        print("========================================")
        print("\t*** ALL TASKS ***")
        print("========================================")
        for line in content:
            lst = line.strip().split("|")
            print(f"\nTask: {lst[1]}\nid: {lst[0]}\ndone: {'No' if lst[2] == 'N' else 'Yes'}\ndate created: {lst[3]}")
            print("----------------------------------------")

        popup("Tasks printed to the console.")


def delete_task(id_):
    """Function to delete a specific task"""

    # Call `open_file` function
    content = open_file(DB_FILE)

    with open(DB_FILE, "w") as file_obj:
        for line in content:
            if line.strip().split("|")[0] != id_:
                file_obj.write(line)


def change(id_, new_task):
    """Function to change/modify a specific task"""

    # Call `open_file` function
    data = open_file(DB_FILE)

    for line in data:
        # Condition to modify the line
        if id_ != line.strip().split("|")[0]:
            continue
        else:
            lst = line.strip().split("|")

        # Create the new line with right data
        new_line = f"{lst[0]}|{new_task}|{lst[2]}|{lst[3]}"
        # Change this line in data
        data[int(id_) - 1] = new_line + "\n"

    # Open the DB file in write mode
    with open(DB_FILE, "w") as file_obj:
        # Overwrite the data
        file_obj.writelines(data)


def done(id_):
    """Function to set a task to done/completed"""

    # Call `open_file` function
    data = open_file(DB_FILE)

    for line in data:
        if id_ != line.strip().split("|")[0]:
            continue
        else:
            lst = line.strip().split("|")

        # Create the new line with right data
        new_line = f"{lst[0]}|{lst[1]}|{'Y'}|{lst[3]}"
        # Change this line in data
        data[int(id_) - 1] = new_line + "\n"

    # Open the DB file in write mode
    with open(DB_FILE, "w") as file_obj:
        # Overwrite the data
        file_obj.writelines(data)


def open_file(filename):
    """Function to open file"""

    # Open the DB file in read mode
    with open(DB_FILE) as file_obj:
        # Read data line by line
        data = file_obj.readlines()

    return data


def menu():
    """Function to show the menu/help message"""

    with open(MENU) as file_obj:
        content = file_obj.read()

    return content


def popup(message):
    """Function to show a pop-up notification with a beep sound"""

    Notification(
        title="Todo App",
        description=message,
        duration=10,  # seconds
        urgency="normal"
    ).send()

    # 1 : 'coin', 2 : 'robot_error', 3 : 'error', 4 : 'ping',
    # 5 : 'ready', 6 : 'success', 7 : 'wilhelm'
    beep(sound=3)


def main():
    """Main program"""

    if len(sys.argv) != 2:
        # Apply colorama module to print the menu with colored text
        print(Style.BRIGHT + Fore.YELLOW + menu())
        popup("Check the usage menu")
        sys.exit(1)

    args = ["add", "ls", "del", "ch", "done", "help"]
    option = sys.argv[1]

    if option == args[0]:
        item = input("Enter your task:\n> ")
        task = Task(item)
        add(str(task))
        print("Task added successfully!")
        popup(f"""task: {task.task}\ndone: {task.done}\ndate: {task.date}""")

    elif option == args[1]:
        list_tasks()

    elif option == args[2]:
        id_ = input("Enter the ID of the task to delete > ")
        delete_task(id_)

        print("Task deleted!")
        popup("Task deleted!")

    elif option == args[3]:
        id_ = input("Type the Task ID to change > ")
        new_task = input("Type the new task >\n")
        change(id_, new_task)

        print("Change done!")
        popup("Change done!")

    elif option == args[4]:
        id_ = input("Enter an ID to set its task to done > ")
        done(id_)

        print("Task set to done!")
        popup("Task set to done!")

    elif option == args[5]:
        # Apply colorama module to print the menu with colored text
        print(Style.BRIGHT + Fore.YELLOW + menu())
        popup("Help menu in the console.")

    else:
        popup("Bye!")
        sys.exit("Unknown option.")


# Standard boilerplate statement to call the main function
if __name__ == "__main__":
    main()
