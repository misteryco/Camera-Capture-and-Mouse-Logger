# Camera-Capture-and-Mouse-Logger

Coordinates capture Mouse Click Capture, and Image Capture with WebSocket Server

# About the app:

This is a Python3.11 code that listen for mouse movements and mouse clicks, it streams mouse coordinates via websocket server.
An on mouse click code capture image with the webcam, and the image is saved on the drive as image and as binary in SQLite
database.
To achieve nonblocking behavior especially when capture image, multiprocessing and asyncio are utilized. 

Mouse Click Capture and Image Logging gittare visible through web interface running on  http://127.0.0.1:5000  to show mouse coordinates in realtime and to allow 
download of the images. From DB.

The app is tested and works on Linux - Ubunty 22.04, and On Windows - Win11.

But if you have problems to run it on Linux it may need additional installation and configuration:

      1. An X server must be installed and running.
      2. The environment variable $DISPLAY must be set.
      3. In older version ov Linux usage of pynput version 1.6.0, this should be changed in requirements.txt before running 
      'pip install -r requirements.txt' command.

On linux:  
   Capturing system-wide clicks have security or privacy implications., 
   Clicks are captured only in the browser that runs logging webpage.
## Prerequisites

Python3.11: [python.org](https://www.python.org/downloads/).

On Linux -> X server  :  [x.org](https://www.x.org/wiki/).

## Setup

1. **Clone this Repository:**

    ```bash
    git clone https://github.com/misteryco/Camera-Capture-and-Mouse-Logger.git
    cd Camera-Capture-and-Mouse-Logger
    ```
2. **Create new Virtual Environment:**

    ```Bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:

        ```Bash
        .\venv\Scripts\activate.bat
        ```

    - On macOS/Linux:

        ```Bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**

    ```Bash
    pip install -r requirements.txt
    ```

6. **Run the project:**
    - In activated venv terminal run:
    ```Bash
    python start.py
    ```
    - open http://127.0.0.1:5000.
   to stop running scripts use Ctr + C
## Stack

- [Python](https://www.python.org/)
- [Websockets](https://websockets.readthedocs.io/en/stable/index.html)
- [sqlalchemy](https://docs.sqlalchemy.org/en/20/)
- [OpenCV](https://docs.opencv.org/4.x/)
- [pynput](https://pynput.readthedocs.io/en/latest/index.html)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
