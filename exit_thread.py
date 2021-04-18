import threading
import keyboard
from program import my_thread

def exit_thread():
    global my_thread
    my_thread._stop()
    my_thread.start()

def monitoring():
    keyboard.add_hotkey('Ctrl + X', exit_thread)
    keyboard.wait()

my_monitoring = threading.Thread(target=monitoring)