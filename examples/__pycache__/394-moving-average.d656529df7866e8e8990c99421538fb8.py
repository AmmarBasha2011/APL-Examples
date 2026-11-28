
# apl-source:1
# مثال 394 — المتوسط المتحرك
# apl-source:2
# Moving average
# apl-source:3
# Demonstrates: نافذة انزلاقية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/394-moving-average.apl
# apl-source:6

# apl-source:7
def متحرك(قائمة, نافذة):
    # apl-source:8
    نتائج = []
    # apl-source:9
    for ب in range(len(قائمة) - نافذة + 1):
        # apl-source:10
        مجموع = 0
        # apl-source:11
        for ي in range(نافذة):
            # apl-source:12
            مجموع = مجموع + قائمة[ب + ي]
        # apl-source:13
        نتائج.append(مجموع / نافذة)
    # apl-source:14
    return نتائج
# apl-source:15

# apl-source:16
أسعار = [10, 12, 14, 13, 15, 17, 16, 18]
# apl-source:17
print("متوسط 3 أيام:", متحرك(أسعار, 3))
# apl-source:18
