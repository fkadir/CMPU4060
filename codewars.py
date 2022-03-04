#CODEWARS

# digital root
# best practice
def digital_root(n):
    print(n)
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# my solution
def my_digital_root(n):
    n = str(n)
    if len(n) < 2:
        return int(n)
    while len(n) >= 2:
        sumy = 0
        for x in n:
            sumy += int(x)
        n = str(sumy)
    return sumy


# find outliers
# best practice
def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


# my solution
def my_find_outlier(integers):
    odd, even = [], []
    for x in range(0, len(integers)):
        if integers[x] % 2 == 0:
            even.append(integers[x])
        else:
            odd.append(integers[x])

    if len(even) < len(odd):
        return even[0]
    else:
        return odd[0]


#