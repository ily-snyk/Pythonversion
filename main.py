# main.py

import sys
import platform
from datetime import datetime

def greet():
    print("Hello, Python 3.11 project!")
    print(f"Running on Python version: {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Script: {sys.argv[0]}")

if __name__ == "__main__":
    greet()
