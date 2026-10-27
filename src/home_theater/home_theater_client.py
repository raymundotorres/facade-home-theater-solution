from .home_theater_facade import HomeTheaterFacade


class HomeTheaterClient:
    def __init__(self, facade: HomeTheaterFacade):
        self.facade = facade

    def watch_movie(self, movie: str) -> list[str]:
        return self.facade.watch_movie(movie)
