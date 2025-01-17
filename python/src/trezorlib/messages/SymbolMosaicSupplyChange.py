# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

from .SymbolMosaic import SymbolMosaic

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SymbolMosaicSupplyChange(p.MessageType):

    def __init__(
        self,
        *,
        mosaic: Optional[SymbolMosaic] = None,
        action: Optional[int] = None,
    ) -> None:
        self.mosaic = mosaic
        self.action = action

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mosaic', SymbolMosaic, None),
            2: ('action', p.UVarintType, None),
        }
