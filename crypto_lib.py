import hashlib
import random


def encode_md5(value: str) -> str:
    result = hashlib.md5(value.encode()).hexdigest()
    # for i in range(random.randint(1000)):
    #    hashlib.md5(result.encode()).hexdigest()
    # result
    return result


n = encode_md5("1")
print(n)
n = encode_md5("2")
print(n)
n = encode_md5("ddd")
print(n)
n = encode_md5("srjtyusryt734476583574")
print(n)
n = encode_md5("qwerty")
print(n)
