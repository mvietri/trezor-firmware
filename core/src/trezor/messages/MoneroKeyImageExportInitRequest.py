# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MoneroSubAddressIndicesList import MoneroSubAddressIndicesList

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroKeyImageExportInitRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 530

    def __init__(
        self,
        *,
        address_n: List[int] = None,
        subs: List[MoneroSubAddressIndicesList] = None,
        num: int = None,
        hash: bytes = None,
        network_type: int = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.subs = subs if subs is not None else []
        self.num = num
        self.hash = hash
        self.network_type = network_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('num', p.UVarintType, None),
            2: ('hash', p.BytesType, None),
            3: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            4: ('network_type', p.UVarintType, None),
            5: ('subs', MoneroSubAddressIndicesList, p.FLAG_REPEATED),
        }
