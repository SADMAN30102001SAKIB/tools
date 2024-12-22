import time

import keyboard
import pyautogui


def clear_input_field():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")


def perform_actions():
    i = 1
    while True:
        pyautogui.write("autoText" + str(i))
        # pyautogui.write("autoText")
        pyautogui.press("enter")
        clear_input_field()
        i = i + 1
        # time.sleep(1)


def on_focus_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "enter":
            perform_actions()


keyboard.hook(on_focus_event)

print("Script started. Press Enter on an input field to begin, Ctrl to stop.")

keyboard.wait("ctrl")

keyboard.unhook_all()
print("Script stopped.")
