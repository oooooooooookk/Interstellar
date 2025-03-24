import subprocess

def run_npm_start():
    try:
        # Run 'npm run start' command
        result = subprocess.run(['npm', 'run', 'start'], check=True, text=True, capture_output=True)
        print("Output:\n", result.stdout)
        print("Errors:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running 'npm run start': {e}")
        print("Error Output:\n", e.stderr)
    except FileNotFoundError:
        print("npm is not installed or not found in the system PATH.")

if __name__ == "__main__":
    run_npm_start()
