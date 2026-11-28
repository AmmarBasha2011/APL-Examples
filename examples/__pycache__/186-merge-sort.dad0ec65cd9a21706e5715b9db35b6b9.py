
# apl-source:1
# مثال 186 — ترتيب الدمج
# apl-source:2
# Merge sort
# apl-source:3
# Demonstrates: العودية، تقسيم القوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/186-merge-sort.apl
# apl-source:6

# apl-source:7
def دمج(أيسر, أيمن):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    while len(أيسر) > 0 and len(أيمن) > 0:
        # apl-source:10
        if أيسر[0] <= أيمن[0]:
            # apl-source:11
            نتيجة.append(أيسر.pop(0))
        # apl-source:12
        else:
            # apl-source:13
            نتيجة.append(أيمن.pop(0))
    # apl-source:14
    return نتيجة + أيسر + أيمن
# apl-source:15

# apl-source:16
def ترتيب_دمج(قائمة):
    # apl-source:17
    if len(قائمة) <= 1:
        # apl-source:18
        return قائمة
    # apl-source:19
    منتصف = len(قائمة) // 2
    # apl-source:20
    أيسر = ترتيب_دمج(قائمة[0:منتصف])
    # apl-source:21
    أيمن = ترتيب_دمج(قائمة[منتصف:])
    # apl-source:22
    return دمج(أيسر, أيمن)
# apl-source:23

# apl-source:24
أرقام = [38, 27, 43, 3, 9, 82, 10]
# apl-source:25
print("قبل:", أرقام)
# apl-source:26
print("بعد:", ترتيب_دمج(أرقام))
# apl-source:27
