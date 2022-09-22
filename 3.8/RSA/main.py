from RSA.env import Generate, Decode, Encode

def decode(text: str, data: dict[str, any]) -> str:
    return Decode(text, data)

def encode(text: str, data: dict[str, any]) -> str:
    return Encode(text, data)

def generate() -> dict[str, any]:
    data = Generate()
    while not data:
        data = Generate()
    return data