
# apl-source:1
# مثال 230 — تنسيق العناوين الإنجليزية
# apl-source:2
# Title case formatter
# apl-source:3
# Demonstrates: تكبير أول حرف، كلمات صغيرة مستثناة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/230-title-case.apl
# apl-source:6

# apl-source:7
صغيرة = ["a", "an", "the", "and", "or", "of", "in", "on", "at", "to"]
# apl-source:8

# apl-source:9
def عنوان_منسق(نص_الدخل):
    # apl-source:10
    كلمات = نص_الدخل.lower().split(" ")
    # apl-source:11
    نتيجة = []
    # apl-source:12
    for ي in range(len(كلمات)):
        # apl-source:13
        ك = كلمات[ي]
        # apl-source:14
        if ي == 0 or ك not in صغيرة:
            # apl-source:15
            نتيجة.append(ك[0].upper() + ك[1:])
        # apl-source:16
        else:
            # apl-source:17
            نتيجة.append(ك)
    # apl-source:18
    return " ".join(نتيجة)
# apl-source:19

# apl-source:20
print(عنوان_منسق("the lord of the rings"))
# apl-source:21
print(عنوان_منسق("a tale of two cities"))
# apl-source:22
