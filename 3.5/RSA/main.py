from RSA.env import Generate, Decode, Encode

def decode(text, data):
    return Decode(text, data)

def encode(text, data):
    return Encode(text, data)

def generate():
    data = Generate()
    while not data:
        data = Generate()
    return data