
# apl-source:1
# مثال 32 — خط أنابيب بالمولدات
# apl-source:2
# Generator Pipeline
# apl-source:3
# Demonstrates: yield, yield from, generators, lazy evaluation
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/32-generator-pipeline.apl
# apl-source:6

# apl-source:7
def دالة_أعداد(الحد):
    # apl-source:8
    رقم = 0
    # apl-source:9
    while رقم < الحد:
        # apl-source:10
        yield رقم
        # apl-source:11
        رقم = رقم + 1
# apl-source:12

# apl-source:13
أعداد = دالة_أعداد
def دالة_مربعات(المصدر):
    # apl-source:14
    for رقم in المصدر:
        # apl-source:15
        yield رقم * رقم
# apl-source:16

# apl-source:17
مربعات = دالة_مربعات
def دالة_الأعداد_الزوجية(المصدر):
    # apl-source:18
    for رقم in المصدر:
        # apl-source:19
        if رقم % 2 == 0:
            # apl-source:20
            yield رقم
# apl-source:21

# apl-source:22
الأعداد_الزوجية = دالة_الأعداد_الزوجية
def دالة_مجموع(المصدر):
    # apl-source:23
    المجموع = 0
    # apl-source:24
    for رقم in المصدر:
        # apl-source:25
        المجموع = المجموع + رقم
    # apl-source:26
    return المجموع
# apl-source:27

# apl-source:28
مجموع = دالة_مجموع
print("=== خط أنابيب بالمولدات ===")
# apl-source:29
print("")
# apl-source:30
print("1) مربعات أول 6 أعداد: " + str(list(مربعات(أعداد(6)))))
# apl-source:31
print("2) زوجية من أول 10: " + str(list(الأعداد_الزوجية(أعداد(10)))))
# apl-source:32
print("3) مجموع مربعات أول 5: " + str(مجموع(مربعات(أعداد(5)))))
# apl-source:33
print("")
# apl-source:34
print("4) خط أنابيب كامل (زوجية من مربعات):")
# apl-source:35
for قيمة in الأعداد_الزوجية(مربعات(أعداد(8))):
    # apl-source:36
    print("   " + str(قيمة))
# apl-source:37
