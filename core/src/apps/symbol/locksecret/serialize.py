import binascii

from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages import SymbolEntityType, SymbolSecretLock, SymbolSecretProof, SymbolTransactionCommon
from trezor.crypto import base32

from ..common_serializors import serialize_tx_common



def secret_lock(
    common: SymbolTransactionCommon,
    lock: SymbolSecretLock,
) -> bytearray:

    tx = serialize_tx_common(common, SymbolEntityType.SECRET_LOCK)

    address = base32.decode(lock.recipient)
    write_bytes_unchecked( tx, address )
    write_bytes_unchecked( tx, binascii.unhexlify(lock.secret) )
    write_uint64_le( tx, lock.mosaic.id )
    write_uint64_le( tx, lock.mosaic.amount )
    write_uint64_le( tx, lock.duration )
    write_uint8( tx, lock.hash_algorithm )

    return tx


def secret_proof(
    common: SymbolTransactionCommon,
    lock: SymbolSecretProof,
) -> bytearray:

    tx = serialize_tx_common(common, SymbolEntityType.SECRET_PROOF)

    address = base32.decode(lock.recipient)
    write_bytes_unchecked( tx, address )
    write_bytes_unchecked( tx, binascii.unhexlify(lock.secret) )

    proof = binascii.unhexlify(lock.proof)

    write_uint16_le( tx, len(proof) )
    write_uint8( tx, lock.hash_algorithm )
    write_bytes_unchecked( tx, proof )

    return tx
