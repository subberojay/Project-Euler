
eulercoins = [1504170715041707]
lastcoin = 1504170715041707

x = 8912517754604

while True is True:
    if x < lastcoin:
        eulercoins.append(x)
        lastcoin = x
        print(x)
        print(sum(eulercoins))
    x += 1504170715041707
    x %= 4503599627370517
    
print(sum(eulercoins))