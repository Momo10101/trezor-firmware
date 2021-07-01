# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

from .SymbolAggregateTransaction import SymbolAggregateTransaction
from .SymbolSingleTransaction import SymbolSingleTransaction

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SymbolSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 90

    def __init__(
        self,
        *,
        address_n: Optional[List[int]] = None,
        aggregate: Optional[SymbolAggregateTransaction] = None,
        single: Optional[SymbolSingleTransaction] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.aggregate = aggregate
        self.single = single

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('aggregate', SymbolAggregateTransaction, None),
            3: ('single', SymbolSingleTransaction, None),
        }