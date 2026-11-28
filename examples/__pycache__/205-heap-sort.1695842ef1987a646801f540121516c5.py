
# apl-source:1
# مثال 205 — ترتيب الكومة
# apl-source:2
# Heap sort
# apl-source:3
# Demonstrates: بناء الكومة، الغربلة للأسفل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/205-heap-sort.apl
# apl-source:6

# apl-source:7
def غربل(قائمة, ن_كومة, جذر):
    # apl-source:8
    أكبر_موضع = جذر
    # apl-source:9
    أيسر = 2 * جذر + 1
    # apl-source:10
    أيمن = 2 * جذر + 2
    # apl-source:11
    if أيسر < ن_كومة and قائمة[أيسر] > قائمة[أكبر_موضع]:
        # apl-source:12
        أكبر_موضع = أيسر
    # apl-source:13
    if أيمن < ن_كومة and قائمة[أيمن] > قائمة[أكبر_موضع]:
        # apl-source:14
        أكبر_موضع = أيمن
    # apl-source:15
    if أكبر_موضع != جذر:
        # apl-source:16
        مؤقت = قائمة[جذر]
        # apl-source:17
        قائمة[جذر] = قائمة[أكبر_موضع]
        # apl-source:18
        قائمة[أكبر_موضع] = مؤقت
        # apl-source:19
        غربل(قائمة, ن_كومة, أكبر_موضع)
# apl-source:20

# apl-source:21
def ترتيب_كومة(قائمة):
    # apl-source:22
    ن = len(قائمة)
    # apl-source:23
    for ي in range(ن // 2):
        # apl-source:24
        غربل(قائمة, ن, ن // 2 - 1 - ي)
    # apl-source:25
    for ي in range(1, ن):
        # apl-source:26
        ك = ن - ي
        # apl-source:27
        مؤقت = قائمة[0]
        # apl-source:28
        قائمة[0] = قائمة[ك]
        # apl-source:29
        قائمة[ك] = مؤقت
        # apl-source:30
        غربل(قائمة, ك, 0)
    # apl-source:31
    return قائمة
# apl-source:32

# apl-source:33
أرقام = [12, 11, 13, 5, 6, 7]
# apl-source:34
print("قبل:", أرقام)
# apl-source:35
print("بعد:", ترتيب_كومة(أرقام))
# apl-source:36
