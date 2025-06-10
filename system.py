from imports import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def listen_for_key(stop_event):
    while not stop_event.is_set():
        if keyboard.is_pressed('q'):
            stop_event.set()
            break
        time.sleep(0.1)