
from django.core.management import execute_from_command_line
import sys
import webbrowser
import subprocess
import time

if __name__ == "__main__":
    # Start the Django server in a subprocess
    server_process = subprocess.Popen([sys.executable, "manage.py", "runserver"])

    # Allow some time for the server to start
    time.sleep(5)  # Wait for 5 seconds to ensure the server is running

    # Open the web browser
    webbrowser.open("http://127.0.0.1:8000/")

    # Check if the server is still running
    server_process.wait()  # Wait for the server process to finish