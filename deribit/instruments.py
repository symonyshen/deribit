from common import TradableElement

class Instrument(TradableElement):

    def __init__(self, name: str) -> None:
        super().__init__(name=name, kind='option')

    def