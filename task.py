"""
task.py - module with the class Task, an object modeling a todolist task.
"""

from datetime import datetime

# Define a text file as the database
DB_FILE = "./todolist.txt"


class Task:
    """A class representing a task."""

    # Initialize the class with its attributes
    def __init__(self, task):
        self.task = task
        self.done = "N"
        self.date = dt_string()
        self.id_ = LAST_ID + 1

    # Method to print the readable form of the object
    def __str__(self):
        return f"{self.id_}|{self.task}|{self.done}|{self.date}"


def get_last_line(filename):
    """Function to get the line of the DB file"""

    # Open the DB file in read mode
    with open(filename) as file_obj:
        # Get the content of the file
        content = file_obj.readlines()

    if len(content) == 0:
        last_line = ""
    else:
        last_line = content[-1]

    return last_line


def get_last_id(filename):
    """Function to get the ID of the last task"""

    # Define a variable to get the last line of the DB file
    last_line = get_last_line(filename)

    # If the file is empty, `last_line` should also be empty
    if last_line == "":
        # Set the last ID to 0
        last_id = 0
    else:
        # Strip & split the line, get the ID and format it into integer
        last_id = int(last_line.strip().split("|")[0])

    return last_id


# Get the last ID
LAST_ID = get_last_id(DB_FILE)


def dt_string():
    """Function to get the time"""

    # Get the current time
    now = datetime.now()
    # Format it into a readable way
    dt_str = now.strftime("%d-%m-%Y %H:%M:%S")

    return dt_str
