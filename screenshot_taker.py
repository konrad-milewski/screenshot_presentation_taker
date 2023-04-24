import cv2
import numpy as np
import time
from PIL import ImageGrab

# Set the initial frame
previous_frame = None

# Set the time to wait before taking a screenshot (in seconds)
screenshot_wait_time = 3

# Continuously capture the screen
while True:
    # Capture the current screen
    screen = np.array(ImageGrab.grab())

    # Convert to grayscale
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # If this is the first frame, set it as the previous frame and continue
    if previous_frame is None:
        previous_frame = gray_screen
        continue

    # Calculate the absolute difference between the current and previous frame
    diff = cv2.absdiff(previous_frame, gray_screen)

    # If the difference is above a certain threshold, wait for a short time
    threshold = 1000
    if np.sum(diff) > threshold:
        time.sleep(screenshot_wait_time)
        screenshot = ImageGrab.grab()
        screenshot.save(f"slide_{time.time()}.png")

    # Set the current frame as the previous frame for the next iteration
    previous_frame = gray_screen
