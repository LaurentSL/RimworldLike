import pygame.time


class Timer:

    def __init__(self, waiting_period_in_ms: int = 1000) -> None:
        self._waiting_period_in_ms = waiting_period_in_ms
        self._start_time = None
        self._is_running = False
        self._is_completed = False

    @property
    def is_completed(self):
        return self._is_completed

    def update(self) -> None:
        if self._is_running:
            current_time = pygame.time.get_ticks()
            if current_time - self._start_time >= self._waiting_period_in_ms:
                self.stop()

    def start(self, waiting_period_in_ms: int = -1) -> None:
        if self._is_running:
            return
        if waiting_period_in_ms > 0:
            self._waiting_period_in_ms = waiting_period_in_ms
        self._start_time = pygame.time.get_ticks()
        self._is_running = True
        self._is_completed = False

    def stop(self):
        self._is_running = False
        self._is_completed = True
