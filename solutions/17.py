
def int_to_list(n):
    s = str(n)
    return [int(s[i]) for i in range(len(s))]

def letter_count(n):
    digits = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [6, 6, 5, 5, 5, 7, 6, 6]
    l = int_to_list(n)
    if len(l) == 1:
        ten_count = digits[n - 1]
    else:
        if l[-2] == 0 and l[-1] != 0:
            ten_count = digits[l[-1] - 1]
        elif l[-2] == 0 and l[-1] == 0:
            ten_count = -3
        elif l[-2] == 1:
            ten_count = teens[l[-1]]
        elif l[-1] == 0:
            ten_count = tens[l[-2] - 2]
        else:
            ten_count = tens[l[-2] - 2] + digits[l[-1] - 1]
    if len(l) <= 2:
        return ten_count
    elif len(l) == 3:
        return digits[l[0] - 1] + 10 + ten_count
    return 11

total_letters = 0

for k in range(1, 1001):
    total_letters += letter_count(k)
    
print(total_letters)
        