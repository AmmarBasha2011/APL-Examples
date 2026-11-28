
# apl-source:1
# مثال 325 — النافذة المنزلقة
# apl-source:2
# Sliding window sums
# apl-source:3
# Demonstrates: مجموع كل نافذة بحجم ك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/325-sliding-window.apl
# apl-source:6

# apl-source:7
def نوافذ_مجاميع(قائمة, ك):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    for ي in range(len(قائمة) - ك + 1):
        # apl-source:10
        مجموع = 0
        # apl-source:11
        for ز in range(ي, ي + ك):
            # apl-source:12
            مجموع = مجموع + قائمة[ز]
        # apl-source:13
        نتيجة.append(مجموع)
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
print(نوافذ_مجاميع([1, 2, 3, 4, 5], 3))
# apl-source:17
print(نوافذ_مجاميع([10, 20, 30, 40], 2))
# apl-source:18
