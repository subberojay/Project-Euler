
filename = 'files/p042_words.txt'

f = open(filename,'r')
words = (f.read()).split(',')
for i in range(len(words)):
    words[i] = words[i].strip('"')
triangleNos = [n*(n + 1)//2 for n in range(1, 41)]
trianglewords = 0
for w in words:
    word_val = 0
    for c in w:
        word_val += ord(c) - 64
    if word_val in triangleNos:
        trianglewords += 1

print(trianglewords)