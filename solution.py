def solution(n):
    if n < 4:
        return '%s/%s' % (2 ** (n - 1), 2 ** n)

    a = 2
    aa = 1
    aaa = 1
    p = 4
    count = 8
    for i in range(4, n + 1):
        temp = aaa
        aaa = aa
        aa = a
        a = p
        p = count
        count = 2 * count - temp
    return '%s/%s' % (aaa + aa + a, count)


print(solution(10))
print(solution(5))
