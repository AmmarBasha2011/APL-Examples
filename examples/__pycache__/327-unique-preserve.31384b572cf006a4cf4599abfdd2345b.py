
# apl-source:1
# مثال 327 — فريد مع الحفاظ على الترتيب
# apl-source:2
# Unique preserving order
# apl-source:3
# Demonstrates: قاموس ظهور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/327-unique-preserve.apl
# apl-source:6

# apl-source:7
def فريد(قائمة):
    # apl-source:8
    مرئية = {}
    # apl-source:9
    نتيجة = []
    # apl-source:10
    for عنصر in قائمة:
        # apl-source:11
        if عنصر not in مرئية:
            # apl-source:12
            مرئية[عنصر] = True
            # apl-source:13
            نتيجة.append(عنصر)
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
print(فريد([3, 1, 3, 2, 1, 4, 2]))
# apl-source:17
print(فريد(["ب", "أ", "ب", "ج", "أ"]))
# apl-source:18
