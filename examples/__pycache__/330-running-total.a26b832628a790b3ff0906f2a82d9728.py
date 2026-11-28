
# apl-source:1
# مثال 330 — المجموع التراكمي
# apl-source:2
# Running total
# apl-source:3
# Demonstrates: تراكم خطوة بخطوة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/330-running-total.apl
# apl-source:6

# apl-source:7
def تراكمي(قائمة):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    مجموع = 0
    # apl-source:10
    for عنصر in قائمة:
        # apl-source:11
        مجموع = مجموع + عنصر
        # apl-source:12
        نتيجة.append(مجموع)
    # apl-source:13
    return نتيجة
# apl-source:14

# apl-source:15
print(تراكمي([1, 2, 3, 4]))
# apl-source:16
print(تراكمي([10, -5, 20, 5]))
# apl-source:17

# apl-source:18
مبيعات = [100, 250, 175, 300]
# apl-source:19
تراكم = تراكمي(مبيعات)
# apl-source:20
print("مبيعات:", مبيعات)
# apl-source:21
print("تراكمي:", تراكم)
# apl-source:22
