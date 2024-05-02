import cv2
import asyncio
from pynput import mouse

async def capture_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Save the captured frame as a photo
    if ret:
        cv2.imwrite("webcam_photo.jpg", frame)
        print("Webcam photo captured: webcam_photo.jpg")
    else:
        print("Error: Could not capture photo from webcam")

    # Release the webcam
    cap.release()

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

async def start_logging():
    # Start logging mouse coordinates after a delay
    await asyncio.sleep(2)  # Adjust the delay as needed
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

async def main():
    # Create tasks
    mouse_task = asyncio.create_task(start_logging())
    webcam_task = asyncio.create_task(capture_webcam())

    # Wait for both tasks to complete
    await asyncio.gather(mouse_task, webcam_task)

if __name__ == "__main__":
    # Create and run the event loop
    asyncio.run(main())
