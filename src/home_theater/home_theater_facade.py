from .amplifier import Amplifier
from .projector import Projector
from .streaming_player import StreamingPlayer
from .theater_lights import TheaterLights


class HomeTheaterFacade:
    def __init__(self, amp: Amplifier, projector: Projector, lights: TheaterLights, player: StreamingPlayer):
        self.amp = amp
        self.projector = projector
        self.lights = lights
        self.player = player

    def watch_movie(self, movie: str) -> list[str]:
        return [
            self.lights.dim(10),
            self.projector.on(),
            self.projector.wide_screen_mode(),
            self.amp.on(),
            self.amp.set_volume(5),
            self.player.on(),
            self.player.play(movie),
        ]

    def end_movie(self) -> list[str]:
        return [self.player.stop(), self.player.off(), self.amp.off(), self.projector.off(), self.lights.on()]
