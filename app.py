#!/usr/bin/env python3

"""
Author      : tonybnya
Date        : 2021
Description : app.py - a todolist app with pop-up notifications.
              For persistence, data are stored in a text file.
"""

import sys
from beepy import beep
from pynotifier import Notification
from task import Task

MENU = "./usage.txt"
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

    # Open the DB file in default read only mode('r')
    with open(DB_FILE) as file_obj:
        # Get the content of the file
        content = file_obj.read()

    # Check if the file is empty
    if len(content) == 0:
        print("No task added yet.")
        popup("No task added yet.")

    # Check if the file is not empty
    if len(content) > 0:
        print(f"\n{content}\n")
        popup("Tasks printed to the console.")


def change():
    """Function to change/modify a specific task"""

    pass


def delete():
    """Function to delete a specific task"""

    pass


def done():
    """Function to set a task to done/completed"""

    pass


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

    print(menu())
    choice = input("Choose an option > ")

    if choice == "1":
        item = input("Enter your task:\n> ")
        task = Task(item)
        add(str(task))
        print("Task added successfully!")
        popup(f"""task: {task.task}\ndone: {task.done}\ndate: {task.date}""")

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        print(menu())
        popup("Help menu in the console.")
    else:
        popup("Bye!")
        sys.exit("Unknown option")


# Standard boilerplate statement to call the main function
if __name__ == "__main__":
    main()
