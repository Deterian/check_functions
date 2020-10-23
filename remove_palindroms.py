def remove_palindroms(spells):
    res = 0
    ne = 0
    size = len(spells)
    while ne < size:
        k = 0
        e = spells[res].lower()
        e = ''.join(e.split())
        if len(e) // 2 == 0:
            chet = 0
        else:
            chet = 1
        for i in range(0, len(e) // 2 + chet):
            j = len(e) - 1 - i
            if e[i] == e[j]:
                k += 1
        if k == len(e) // 2 + chet:
            spells.pop(res)
        else:
            res += 1
        ne += 1

