
# apl-source:1
# مثال 313 — مثلث باسكال
# apl-source:2
# Pascal's triangle
# apl-source:3
# Demonstrates: بناء صفوف من السابق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/313-pascal.apl
# apl-source:6

# apl-source:7
def مثلث_باسكال(صفوف):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    for ي in range(صفوف):
        # apl-source:10
        سطر = [1 for _ in range(ي + 1)]
        # apl-source:11
        for ز in range(1, ي):
            # apl-source:12
            سطر[ز] = نتيجة[ي - 1][ز - 1] + نتيجة[ي - 1][ز]
        # apl-source:13
        نتيجة.append(سطر)
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
for سطر in مثلث_باسكال(6):
    # apl-source:17
    print(سطر)
# apl-source:18
