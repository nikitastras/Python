import pyautogui
import datetime

def take_screenshot(filename=None):
    if filename is None:
        # Create a filename based on current date and time if none is provided
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
    
    # Capture screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")

if __name__ == "__main__":
    take_screenshot()
