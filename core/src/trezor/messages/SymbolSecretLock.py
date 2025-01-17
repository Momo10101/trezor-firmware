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


class SymbolSecretLock(p.MessageType):

    def __init__(
        self,
        *,
        recipient: Optional[str] = None,
        secret: Optional[str] = None,
        mosaic: Optional[SymbolMosaic] = None,
        duration: Optional[int] = None,
        hash_algorithm: Optional[int] = None,
    ) -> None:
        self.recipient = recipient
        self.secret = secret
        self.mosaic = mosaic
        self.duration = duration
        self.hash_algorithm = hash_algorithm

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient', p.UnicodeType, None),
            2: ('secret', p.UnicodeType, None),
            3: ('mosaic', SymbolMosaic, None),
            4: ('duration', p.UVarintType, None),
            5: ('hash_algorithm', p.UVarintType, None),
        }
