from .media import Media, Kaldnes

class Filter:

    def __init__(self, *, volume: float = 0, media: Media = Kaldnes):
        self.media = media
        self.volume = volume

    @property
    def bsa(self):
        return self.media.ssa * self.volume
