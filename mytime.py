import datetime
import time
import tkinter as tk
from tkinter import messagebox


def send_notification(message):
    # Show a pop-up window with the notification message
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Notification", message)
    root.destroy()


def perform_task(task_name):
    # Implement your logic for each task
    print(f"Performing task: {task_name}...")


def calculate_end_time(hours):
    # Calculate the end time based on the specified number of hours
    return datetime.datetime.now() + datetime.timedelta(hours=hours)


# Define the tasks and their durations (in hours)
tasks = [
    {"name": "C++", "hours": 2},
    {"name": "Books Django 4", "hours": 3},
    {"name": "Learn English", "hours": 2},
]

# Start time for the first task
current_time = datetime.datetime.now()

# Calculate the end times for each task
for task in tasks:
    task["end_time"] = calculate_end_time(task["hours"])

# Start the main loop
for task in tasks:
    # Display a notification before starting the current task
    send_notification(f"Start: {task['name']}!")

    # Perform the current task
    perform_task(task["name"])

    # Check if it's time to perform the next task
    if current_time >= task["end_time"]:
        continue

    # Sleep until the end time of the current task
    time.sleep((task["end_time"] - current_time).total_seconds())

# Display a notification at the end of the last task
send_notification("All tasks completed!")
