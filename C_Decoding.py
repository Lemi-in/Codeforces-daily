n = int(input())
s = input()

decoded_word = ''

for i in range(n):
    if i % 2 == 0:
        decoded_word = decoded_word + s[i]
    else:
        decoded_word = s[i] + decoded_word

print(decoded_word)
