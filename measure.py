def similarity(s1, s2):
    """
    calculate this arbitrary measure:

    1-\Big(\frac{\sum_{i}\sum_{i-2, i\neq0}^{i+2}|i-f(i)|}{4l(l-1)}\Big)
    """

    indexes = {}
    for i, s in enumerate(s2):
        indexes[s] = i

    sum_distance = 0

    for i, s in enumerate(s1):
        for offset in [-2, -1, 1, 2]:
            sum_distance += abs(i-indexes[s])

    return 1 - (sum_distance/(4*len(s1)*(len(s1)-1)))



