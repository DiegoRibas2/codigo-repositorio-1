import pyautogui
import time
import threading
import keyboard

class autoclicker:
    def __init__(self, interval):
        self.interval = interval
        self.running = False

        def start_clicking(self):
         self.running = True
         while self.running:
                pyautogui.click()
                time.sleep(self.interval)
 
        def stop_clicking(self):
            self.running = False
         
def on_press_event(clicker):
           if not clicker.running:
            threading.Thread(target=clicker.start_clicking).start()

def on_release_event(clicker):
    clicker.stop_clicking()

    if __name__ == "__main__":
        interval = float(input("intervalo entre cliques (em segundos):"))
        clicker = autoclicker(interval)

        print("pressione 'l' para começar e parar o autoclicker")
        keyboard.on_press_key("l", lambda _: on_press_event(clicker))
        keyboard.on_press_key("l", lambda _: on_release_event(clicker))

        keyboard.wait("esc")
        print("saindo do programa...")

    
    