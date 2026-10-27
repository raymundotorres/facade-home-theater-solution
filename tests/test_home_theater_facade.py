from home_theater.amplifier import Amplifier
from home_theater.home_theater_client import HomeTheaterClient
from home_theater.home_theater_facade import HomeTheaterFacade
from home_theater.projector import Projector
from home_theater.streaming_player import StreamingPlayer
from home_theater.theater_lights import TheaterLights


def build_facade():
    return HomeTheaterFacade(Amplifier(), Projector(), TheaterLights(), StreamingPlayer())


def test_client_uses_one_task_oriented_entry_point():
    steps = HomeTheaterClient(build_facade()).watch_movie("Design Patterns")
    assert steps[0] == "lights:dim:10"
    assert steps[-1] == "player:play:Design Patterns"


def test_facade_can_end_movie_without_moving_subsystem_responsibilities():
    assert build_facade().end_movie() == [
        "player:stop", "player:off", "amplifier:off", "projector:off", "lights:on"
    ]
