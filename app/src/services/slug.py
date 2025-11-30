import string
from secrets import choice


ALPHABET: str = string.ascii_letters + string.digits

# Generate a random slug of a given length
def generate_slug(length: int = 7) -> str:
    return "".join(choice(ALPHABET) for _ in range(length))