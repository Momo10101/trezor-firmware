from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolNamespaceRegistration  import SymbolNamespaceRegistration
from trezor.messages import SymbolAddressAlias, SymbolEntityType, SymbolMosaicAlias
from trezor.crypto import base32
#import binascii

from ..common_serializors import serialize_tx_header

def serialize_namespace_registration(
    header: SymbolHeader, namespace: SymbolNamespaceRegistration
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.NAMESPACE_REGISTRATION)

    write_uint64_le( tx, namespace.duration )
    write_uint64_le( tx, namespace.id )
    write_uint8( tx, namespace.registration_type )
    write_uint8( tx, len(namespace.name) )
    write_bytes_unchecked( tx, namespace.name )

    return tx



def serialize_address_alias(
    header: SymbolHeader, address_alias: SymbolAddressAlias
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.ADDRESS_ALIAS)

    address = base32.decode(address_alias.address)

    write_uint64_le( tx, address_alias.namespace_id )
    write_bytes_unchecked( tx, address )
    write_uint8( tx, address_alias.action )

    return tx


def serialize_mosaic_alias(
    header: SymbolHeader, mosaic_alias: SymbolMosaicAlias
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.ADDRESS_ALIAS)

    write_uint64_le( tx, mosaic_alias.namespace_id )
    write_uint64_le( tx, mosaic_alias.mosaic_id    )
    write_uint8( tx, mosaic_alias.action )

    return tx
