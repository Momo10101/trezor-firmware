# Automatically generated by pb2py
# fmt: off
# isort:skip_file
import protobuf as p

from .SymbolMosaic import SymbolMosaic

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SymbolHashLock(p.MessageType):

    def __init__(
        self,
        *,
        mosaic: Optional[SymbolMosaic] = None,
        duration: Optional[int] = None,
        hash: Optional[str] = None,
    ) -> None:
        self.mosaic = mosaic
        self.duration = duration
        self.hash = hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mosaic', SymbolMosaic, None),
            2: ('duration', p.UVarintType, None),
            3: ('hash', p.UnicodeType, None),
        }