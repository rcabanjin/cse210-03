


class Director:

    def __init__(self):

    def start_game(self):
        while self._is_playing:
            self._is_playing = False
            self.update()
            time.sleep(0.1)
        