from threading import Thread
import time
from pynput.keyboard import Controller, Key
import tkinter as tk

def press_f16_every_minute_with_counter():
    global counter
    keyboard = Controller()
    while True:
        keyboard.press(Key.f16)
        keyboard.release(Key.f16)
        counter += 1
        print(f"F16 key pressed {counter} times")
        time.sleep(60)

def show_counter():
    root = tk.Tk()
    root.title("F16 Key Press Counter")
    counter_label = tk.Label(root, text="F16 Key Pressed: 0", font=("Helvetica", 16))
    counter_label.pack(pady=20)

    def update_counter():
        while True:
            counter_label.config(text=f"F16 Key Pressed: {counter}")
            root.update_idletasks()
            time.sleep(1)

if __name__ == "__main__":
    counter = 0
    Thread(target=show_counter, daemon=True).start()
    press_f16_every_minute_with_counter()