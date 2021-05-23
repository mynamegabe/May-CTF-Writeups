def encode(fHpr):
    encoded = ""
    prevchar = " "
    for sDhe in fHpr:
        encoded += chr(ord(sDhe)+ord(prevchar))
        print(ord(sDhe)+ord(prevchar))
        prevchar = sDhe
    return encoded

def decode(str1):
    decoded = ""
    prevchar = " "
    for char in str1:
        print(decoded)
        decoded += chr(ord(char)-ord(prevchar))
        prevchar = chr(ord(char)-ord(prevchar))
    return decoded
