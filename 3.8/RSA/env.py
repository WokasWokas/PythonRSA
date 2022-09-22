from functools import cache
from Environment.env import dictionary
from Parser.setting import Parse
from random import getrandbits, seed
from time import time

UpdateSeed = lambda: seed(version=int(time())) 
_LetterDict = {}

count = 1
for letter in dictionary:
    _LetterDict[letter] = count
    count += 1

_KeyLength = int(Parse().get('keylength')[0])
__BLOCK_LENGTH__ = 1

def GetKeyFromDict(Dict: dict, _value: any) -> any:
    for key, value in Dict.items():
        if value == _value: return key

@cache
def IsPrime(number: int) -> bool: 
    if (number == 2 or number == 3):
        return True
    if (number % 2 == 0 or number % 3 == 0 or number == 1):
        return False
    i = 5
    while (i*i < number):
        if (number % i == 0 or number % (i + 2) == 0):
            return False
        i += 4
    return True

def SplitString(text: str) -> tuple[str]:
    return [text[i:i+__BLOCK_LENGTH__] for i in range(0, len(text), __BLOCK_LENGTH__)]

@cache
def gcd(value1: int, value2: int) -> int:
    while ((value1 != 0) and (value2 != 0)):
        if (value1 > value2):
            value1 -= value2
        else:
            value2 -= value1
    return max(value1, value2)

def GenerateNumber() -> int:
    return getrandbits(_KeyLength)

def GetRandomPrimeNumber() -> int:
    number = GenerateNumber()
    while not IsPrime(number):
        number = GenerateNumber()
    return number

def GetExponent(pubk: int, euler: int) -> int:
    Exponent = GetRandomPrimeNumber()
    while Exponent > pubk or gcd(Exponent, euler) != 1:
        Exponent = GetRandomPrimeNumber()
    return Exponent 

def GetPrivateKey(exp: int, euler) -> int:
    privkey = GetRandomPrimeNumber()
    count, ucount = 0, 0
    while (privkey * exp - 1) % euler != 0:
        if count % 30 == 0:
            if ucount == 500:
                return False
            UpdateSeed()
            ucount += 1
        privkey = GetRandomPrimeNumber()
        count += 1
    return privkey

def Generate():
    UpdateSeed()
    FirstPrime = GetRandomPrimeNumber()
    SecondPrime = GetRandomPrimeNumber()
    if _KeyLength >= 8:
        if SecondPrime < 16 and FirstPrime < 16: return False
    if gcd(FirstPrime, SecondPrime) != 1: return False
    PublicKey = FirstPrime * SecondPrime
    Euler = (FirstPrime - 1) * (SecondPrime - 1)
    Exponent = GetExponent(PublicKey, Euler)
    PrivateKey = GetPrivateKey(Exponent, Euler)
    if not PrivateKey: return False
    data = {
        "firstkey": FirstPrime,
        "secondkey": SecondPrime,
        "euler": Euler,
        "privkey": [PrivateKey, PublicKey],
        "pubkey": [Exponent, PublicKey],
    }
    return data

def Decode(text: str, data: dict) -> str:
    decodedblocks = []
    for block in SplitString(text):
        value = _LetterDict[block]
        decodedblocks.append(pow(value, data['pubkey'][0], data['pubkey'][1]))
    return ' '.join(str(block) for block in decodedblocks)

def Encode(text: int, data: dict) -> str:
    try:
        blocks = []
        for block in text.split(' '):
            value = pow(int(block), data['privkey'][0], data['privkey'][1])
            blocks.append(value)
        return (''.join(GetKeyFromDict(_LetterDict, block) for block in blocks)).replace('\0', '')
    except ValueError:
        return 'Wrong Value!'
