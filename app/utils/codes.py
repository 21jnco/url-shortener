import string
import secrets

ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 6


def generate_code(length: str = CODE_LENGTH) -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(length))