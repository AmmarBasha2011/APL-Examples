
# apl-source:1
# مثال 455 — تنسيق العناوين الإنجليزية
# apl-source:2
# Title case converter
# apl-source:3
# Demonstrates: كلمات صغرى تبقى صغيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/455-title-case.apl
# apl-source:6

# apl-source:7
صغرى = ["a", "an", "the", "of", "in", "on", "and"]
# apl-source:8

# apl-source:9
def عنوان_سليم(نص_الدخل):
    # apl-source:10
    كلمات = نص_الدخل.split(" ")
    # apl-source:11
    نتائج = []
    # apl-source:12
    for ي in range(len(كلمات)):
        # apl-source:13
        كلمة = كلمات[ي]
        # apl-source:14
        if ي > 0 and صغرى.count(كلمة) > 0:
            # apl-source:15
            نتائج.append(كلمة)
        # apl-source:16
        else:
            # apl-source:17
            نتائج.append(كلمة[0].upper() + كلمة[1:])
    # apl-source:18
    return " ".join(نتائج)
# apl-source:19

# apl-source:20
print(عنوان_سليم("the lord of the rings"))
# apl-source:21
print(عنوان_سليم("a tale of two cities"))
# apl-source:22
