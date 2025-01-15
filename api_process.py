import os
import subprocess

os.chdir("D:/OneDrive - Radhakrishna Foodland Pvt Ltd/Python_Project/API_store_in_DB/API_Testing")

subprocess.run(["python", "manage.py", "runserver", "0.0.0.0:8000"])


