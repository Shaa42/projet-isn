from threading import Thread

class GameTimer:
    def __init__(self, duration):
        self.duration = duration
        self.remaining = duration
        self.running = False
        
    def start(self):
        self.running = True
        timer_thread = Thread(target=self._countdown)
        timer_thread.daemon = True
        timer_thread.start()
        
    def _countdown(self):
        import time
        while self.remaining > 0 and self.running:
            time.sleep(1)
            self.remaining -= 1
        if self.remaining <= 0:
            global game_running, event_message
            game_running = False
            event_message = "Temps écoulé ! Une tempête a éclaté !"