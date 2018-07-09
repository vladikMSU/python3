def is_number(str) :
    if str[0] == '-' :
        return str[1:].isdigit()
    return str.isdigit()

words = []

while True :
    line = input()
    if not line :
        break
    words += line.split()


ints = [int(word) for word in words if is_number(word)]

print(max(ints))