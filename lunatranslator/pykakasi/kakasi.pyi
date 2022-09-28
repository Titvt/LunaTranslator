from .kanji import Itaiji as Itaiji
from .kanji import JConv as JConv
from .properties import Ch as Ch
from .scripts import IConv as IConv
from typing import Dict, List

class PyKakasiException(Exception): ...
class UnknownCharacterException(PyKakasiException): ...

class Kakasi:
    def __init__(self) -> None: ...
    def convert(self, text: str) -> List[Dict[str, str]]: ...