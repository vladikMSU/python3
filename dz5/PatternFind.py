def matches(str, pattern) :
    """ Check if str matches with pattern"""
    
    # if lengths are not equal => doesnt match
    if len(str) < len(pattern) :
        return False

    substr, sym, rest = pattern.partition('@')

    while True:
        if not str.startswith(substr) :
            return False

        if not sym :
            return True

        # cut substr and 1 sym standing for '@'
        str = str[len(substr)+1:]

        substr, sym, rest = rest.partition('@')




# MAIN

line = input()

pattern = input()


ans = -1

# start pos
i = 0

first_substr, _, _ = pattern.partition('@')

while line:
    pos = line.find(first_substr)

    if pos == -1 :
        break

    line = line[pos:]
    i += pos

    if matches(line[:len(pattern)+1], pattern) :
        ans = i
        break

    if not first_substr :
        line = line[1:]
        i+=1
    else :
        line = line[len(first_substr):]
        i+=len(first_substr)


print(ans)