
# apl-source:1
# مثال 12 — فحص الأعداد الأولية
# apl-source:2
# Prime Number Checker
# apl-source:3
# Demonstrates: sqrt, modulo, user functions, early exit
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/12-prime-check.apl
# apl-source:6

# apl-source:7
def أولي(عدد):
    # apl-source:8
    if عدد < 2:
        # apl-source:9
        return False
    # apl-source:10
    if عدد == 2:
        # apl-source:11
        return True
    # apl-source:12
    if عدد % 2 == 0:
        # apl-source:13
        return False
    # apl-source:14
    القاسم = 3
    # apl-source:15
    while القاسم * القاسم <= عدد:
        # apl-source:16
        if عدد % القاسم == 0:
            # apl-source:17
            return False
        # apl-source:18
        القاسم = القاسم + 2
    # apl-source:19
    return True
# apl-source:20

# apl-source:21
def أوليات_حتى(الحد):
    # apl-source:22
    النتيجة = []
    # apl-source:23
    رقم = 2
    # apl-source:24
    while رقم <= الحد:
        # apl-source:25
        if أولي(رقم):
            # apl-source:26
            النتيجة = النتيجة + [رقم]
        # apl-source:27
        رقم = رقم + 1
    # apl-source:28
    return النتيجة
# apl-source:29

# apl-source:30
print("=== فحص الأعداد الأولية ===")
# apl-source:31
قائمة = أوليات_حتى(50)
# apl-source:32
print("الأعداد الأولية حتى 50:")
# apl-source:33
print("  " + str(قائمة))
# apl-source:34
print("")
# apl-source:35
print("عددها: " + str(len(قائمة)))
# apl-source:36
print("")
# apl-source:37
print("اختبار:")
# apl-source:38
for رقم in [1, 2, 7, 9, 13, 21, 97, 100]:
    # apl-source:39
    print(f"  {رقم} أولي؟ {أولي(رقم)}")
# apl-source:40
