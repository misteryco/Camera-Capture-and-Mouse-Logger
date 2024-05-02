import subprocess
import os
import platform


def get_activate_script():
    """
    Construct the path to the virtual environment's activate script depending on OS specifics.

    Returns:
        str: The absolute path to the activate script of the virtual environment.
    """
    venv_folder = ".venv" if platform.system() == "Windows" else "venv"
    second = "Scripts" if platform.system() == "Windows" else "bin"
    third = "activate.bat" if platform.system() == "Windows" else "activate"

    return os.path.join(os.path.abspath(os.path.dirname(__file__)), venv_folder, second, third)


def run_command(command):
    """
    Run a command in the shell.

    Args:
        command (str): The command to be executed in the shell.
    """
    subprocess.Popen(command, shell=True).wait()


if __name__ == "__main__":
    """
    Main block for running flask_app.py and main.py scripts.

    This block sets up and executes two subprocesses for running the "flask_app.py" and the "main.py" script.
    Two subprocesses are started to run the Flask app and main.py script respectively.
    
    If a KeyboardInterrupt is raised (typically by pressing Ctrl+C), both subprocesses are terminated gracefully.

    Note:
        This block assumes that the Flask app is run using the command 'python flask_app.py'
        and the main.py script is run using the command 'python main.py'.
        Ensure that these scripts exist and are executable from the command line.
    """
    activate_cmd = f". {get_activate_script()}" if platform.system() != "Windows" else f"call {get_activate_script()}"
    working_dir = os.path.abspath(os.path.dirname(__file__))
    activate_cmd += f" && cd {working_dir}"

    flask_command = activate_cmd + " && python flask_app.py"
    flask_process = subprocess.Popen(flask_command, shell=True)

    main_command = activate_cmd + " && python main.py"
    main_process = subprocess.Popen(main_command, shell=True)

    try:
        flask_process.wait()
        main_process.wait()

    except KeyboardInterrupt:
        flask_process.terminate()
        main_process.terminate()
