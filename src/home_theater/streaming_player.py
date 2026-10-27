class StreamingPlayer:
    def on(self):
        return "player:on"

    def play(self, movie):
        return f"player:play:{movie}"

    def stop(self):
        return "player:stop"

    def off(self):
        return "player:off"
