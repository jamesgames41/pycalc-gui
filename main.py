import subprocess
import os


def run_script(file_name):
    """Helper function to run a python file"""
    try:
        # This launches the script as a separate process
        subprocess.run(['python', file_name], check=True)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        print("\n--- Pycalc Launcher ---")
        print("1. basic calculator")
        print("2. 2d shape area calculator")
        print("3. 3d shape area calculator")
        print("4. Exit")

        choice = input("\nEnter the number of your option: ")

        if choice == '1':
            print("Launching basic calc...\n")
            run_script('basic calc.py')
        elif choice == '2':
            print("Launching 2d area calc ...\n")
            run_script('2d shape.py')
        elif choice == '3':
            print("Launching 3d shape area calc ...\n")
            run_script('3d shape.py')
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()