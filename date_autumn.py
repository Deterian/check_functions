def date_autumn(dates):
    autumn = list()
    for y in range(2019, 1899, -1):
        for m10 in range(11, 9, -1):
            for d10 in range(31, 9, -1):
                autumn.append(str(m10) + '-' + str(d10) + '-' + str(y))
            for d1 in range(9, 0, -1):
                autumn.append(str(m10) + '-' + '0' + str(d1) + '-' + str(y))
        for d10 in range(31, 9, -1):
            autumn.append('09' + '-' + str(d10) + '-' + str(y))
        for d1 in range(9, 0, -1):
            autumn.append('09' + '-' + '0' + str(d1) + '-' + str(y))
    for d in autumn:
        if d in dates:
            return d
