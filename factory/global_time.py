class Timer:
    
    def __init__(self) -> None:
        self.current_time = 0

    def run_timer(self):
        self.current_time += 1

    def get_current_time(self):
        return self.current_time