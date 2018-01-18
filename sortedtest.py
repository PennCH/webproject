def cmp_ignore_case(s1, s2):
    n1 = s1.upper()
    n2 = s2.upper()
    if n1 > n2:
        return 1
    if n1 < n2:
        return -1
    return 0
print (list(sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)))