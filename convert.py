
def to_string(a: int | float | bytes) -> str:
    if isinstance(a,bytes):
        return a.decode('utf-8')
    return str(a)
def to_int(a: float) -> int:
    return int(a)
def to_float(a: int) -> float:
    return float(a)
def to_bytes(a: int | str | list) -> bytes:
    if isinstance(a, int):
        return bytes([a])
    if isinstance(a, str):
        return bytes(a, 'utf-8')
    return bytes(a) 