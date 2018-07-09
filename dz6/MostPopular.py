words = [word.lower() for word in input().split()]

freqs = {}
for word in words:
    freqs[word] = freqs.get(word, 0) + 1

print (len([word for word in freqs if freqs[word] == max(freqs.values())]))