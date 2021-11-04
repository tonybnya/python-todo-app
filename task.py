"""
task.py - module with the class Task, an object modeling a todolist task.
"""

from datetime import datetime

LAST_ID = 0


class Task:
    """Initialize the class with its attributes"""

    def __init__(self, task):
        self.task = task
        self.done = "N"
        self.date = dt_string()
        global LAST_ID
        LAST_ID += 1
        self.id_ = LAST_ID

    # Method to print the readable form of the object
    def __str__(self):
        return f"{self.id_}> {self.task}, done: {self.done}, date: {self.date}"


def dt_string():
    """Function to get the time"""

    # Get the current time
    now = datetime.now()
    # Format it in a readable way
    dt_str = now.strftime("%d-%m-%Y %H:%M:%S")

    return dt_str
