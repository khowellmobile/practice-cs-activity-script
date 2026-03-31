import pygetwindow as gw # type: ignore
from pywinauto import Application # type: ignore
import win32api # type: ignore
import time

INTERVAL = 900  # 10min = 600, 15min = 900
WINDOW_TITLE_SUBSTRING = "Practice CS"
LAST_MOUSE_POSITION = (0, 0)


def get_current_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S", current_time)
    return formatted_time


def click_window():
    global LAST_MOUSE_POSITION
    try:
        windows = gw.getWindowsWithTitle(WINDOW_TITLE_SUBSTRING)
        if not windows:
            print(f"Window with title containing '{WINDOW_TITLE_SUBSTRING}' not found.")
            return
        target_window = windows[0]
        app = Application().connect(handle=target_window._hWnd)
        dlg = app.window(handle=target_window._hWnd)

        # Get current mouse position before clicking
        original_mouse_position = win32api.GetCursorPos()

        ## Protection for cases where user is away from computer
        if original_mouse_position == LAST_MOUSE_POSITION:
            print(
                f"Mouse position unchanged since last click. Skipping click at {get_current_time()}."
            )
            return
        else:
            LAST_MOUSE_POSITION = original_mouse_position

        # Check if minimized
        was_minimized = dlg.is_minimized()
        if was_minimized:
            dlg.restore()
            time.sleep(0.5)  # Wait for the window to restore

        rect = dlg.rectangle()
        width = rect.width()
        dlg.click_input(coords=(int(width / 2), 10))

        # Restore original mouse position
        win32api.SetCursorPos(original_mouse_position)

        if was_minimized:
            dlg.minimize()

        print(f"Clicked on '{WINDOW_TITLE_SUBSTRING}' at {get_current_time()}")

    except Exception as e:
        print(f"Error: {e}")


def keep_alive():
    print(
        f"Keep-alive script started w/ interval {INTERVAL} seconds. Press Ctrl+C to stop."
    )
    try:
        while True:
            click_window()
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Script terminated by user.")


if __name__ == "__main__":
    keep_alive()
