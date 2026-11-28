
# apl-source:1
# مثال 281 — كل المجموعات الفرعية
# apl-source:2
# All subsets (backtracking)
# apl-source:3
# Demonstrates: توليد 2^ن مجموعة بالتراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/281-subsets.apl
# apl-source:6

# apl-source:7
def فرعيات(عناصر):
    # apl-source:8
    نتيجة = [[]]
    # apl-source:9
    for عنصر in عناصر:
        # apl-source:10
        جديدة = []
        # apl-source:11
        for مجموعة in نتيجة:
            # apl-source:12
            جديدة.append(مجموعة + [عنصر])
        # apl-source:13
        for مجموعة in جديدة:
            # apl-source:14
            نتيجة.append(مجموعة)
    # apl-source:15
    return نتيجة
# apl-source:16

# apl-source:17
print(فرعيات([1, 2, 3]))
# apl-source:18
print("عدد فرعيات 4 عناصر:", len(فرعيات([1, 2, 3, 4])))
# apl-source:19
