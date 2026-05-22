import uuid


def generate_id(length: int = 6) -> str:
    return uuid.uuid4().hex[:length]