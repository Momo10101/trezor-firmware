# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SymbolCosignature(p.MessageType):

    def __init__(
        self,
        *,
        version: Optional[int] = None,
        signer_public_key: Optional[str] = None,
        signature: Optional[str] = None,
    ) -> None:
        self.version = version
        self.signer_public_key = signer_public_key
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('version', p.UVarintType, None),
            2: ('signer_public_key', p.UnicodeType, None),
            3: ('signature', p.UnicodeType, None),
        }