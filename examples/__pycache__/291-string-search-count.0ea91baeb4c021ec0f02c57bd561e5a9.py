
# apl-source:1
# مثال 291 — عد تكرارات نموذج في نص
# apl-source:2
# Pattern occurrence count
# apl-source:3
# Demonstrates: بحث ساذج بكل المواضع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/291-string-search-count.apl
# apl-source:6

# apl-source:7
def عد_التكرارات(نص_الدخل, نموذج):
    # apl-source:8
    عدد = 0
    # apl-source:9
    ن = len(نص_الدخل)
    # apl-source:10
    م = len(نموذج)
    # apl-source:11
    for ي in range(ن - م + 1):
        # apl-source:12
        if نص_الدخل[ي:ي + م] == نموذج:
            # apl-source:13
            عدد = عدد + 1
    # apl-source:14
    return عدد
# apl-source:15

# apl-source:16
print(عد_التكرارات("ababcabc", "abc"))
# apl-source:17
print(عد_التكرارات("aaaa", "aa"))
# apl-source:18
print(عد_التكرارات("hello world", "xyz"))
# apl-source:19
