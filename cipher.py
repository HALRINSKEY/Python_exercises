import string

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypy = ""
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypy += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypy += lowercase[new]
        else:
            encrypy += c

    return encrypy

print(cipher("This is cipher",5))
