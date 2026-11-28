
# apl-source:1
# مثال 272 — العنصر الأغلبي (بوير-مور)
# apl-source:2
# Boyer-Moore majority vote
# apl-source:3
# Demonstrates: إيجاد العنصر الأكثر تكرارا بلا عد كامل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/272-majority.apl
# apl-source:6

# apl-source:7
def أغلبي(قائمة):
    # apl-source:8
    مرشح = قائمة[0]
    # apl-source:9
    رصيد = 1
    # apl-source:10
    for ي in range(1, len(قائمة)):
        # apl-source:11
        if قائمة[ي] == مرشح:
            # apl-source:12
            رصيد = رصيد + 1
        # apl-source:13
        else:
            # apl-source:14
            رصيد = رصيد - 1
        # apl-source:15
        if رصيد == 0:
            # apl-source:16
            مرشح = قائمة[ي]
            # apl-source:17
            رصيد = 1
    # apl-source:18
    return مرشح
# apl-source:19

# apl-source:20
print(أغلبي([3, 2, 3]))
# apl-source:21
print(أغلبي([2, 2, 1, 1, 1, 2, 2]))
# apl-source:22
