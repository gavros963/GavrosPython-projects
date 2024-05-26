def collatz(n):
    x = n
    if x % 2 is 0:
        x = int(x/2)
    else:
        x = int((x*3)+1)
    print(x)
    if x == 1:
        return
    else:
        collatz(x)
i = 1    
while i <= 1000:
    collatz(i)
    i = i + 1