"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative integer quantity parsed from *value*.

    Raises ValueError for non-integer input or quantities less than 1.
    """
    result = int(value.strip())
    if result <= 0:
        raise ValueError(f"Quantity must be a positive integer, got {result}")
    return result
