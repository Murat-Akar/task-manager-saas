from dotenv import load_dotenv
import os

load_dotenv()

app_env = os.getenv("APP_ENV")

print(app_env)
print("Hello from task manager")
print("Second change")
print("Task Manager Feature")
