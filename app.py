from flask import app


print("Hello, World!")
tasks = []

print("Welcome to Todo App")

tasks.append("Learn Git")
print(tasks)

tasks.remove("Learn Git")
print("Task deleted successfully")

task = input("Enter your task: ")
tasks.append(task)

print(tasks)
