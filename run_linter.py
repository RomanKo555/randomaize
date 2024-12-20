import threading
import subprocess



def run_linter():
    print("Running linter...")
    subprocess.run(["flake8", "."])

if __name__ == "__main__":
    run_linter()

    print("All tasks completed.")