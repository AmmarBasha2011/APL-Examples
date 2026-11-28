
# apl-source:1
# مثال 258 — العمر بالأيام
# apl-source:2
# Age in days
# apl-source:3
# Demonstrates: حساب الأيام بين تاريخين يدويا
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/258-age-days.apl
# apl-source:6

# apl-source:7
def كبيسة(سنة_م):
    # apl-source:8
    if سنة_م % 400 == 0:
        # apl-source:9
        return True
    # apl-source:10
    if سنة_م % 100 == 0:
        # apl-source:11
        return False
    # apl-source:12
    return سنة_م % 4 == 0
# apl-source:13

# apl-source:14
def أيام_منذ_الميلاد(يوم_م, شهر_م, سنة_م):
    # apl-source:15
    أيام_شهور = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # apl-source:16
    مجموع = يوم_م
    # apl-source:17
    for س in range(1, سنة_م):
        # apl-source:18
        if كبيسة(س):
            # apl-source:19
            مجموع = مجموع + 366
        # apl-source:20
        else:
            # apl-source:21
            مجموع = مجموع + 365
    # apl-source:22
    for م in range(شهر_م - 1):
        # apl-source:23
        مجموع = مجموع + أيام_شهور[م]
    # apl-source:24
    if شهر_م > 2 and كبيسة(سنة_م):
        # apl-source:25
        مجموع = مجموع + 1
    # apl-source:26
    return مجموع
# apl-source:27

# apl-source:28
ميلاد = أيام_منذ_الميلاد(9, 9, 2000)
# apl-source:29
اليوم_م = أيام_منذ_الميلاد(23, 11, 2026)
# apl-source:30
print("العمر بالأيام:", اليوم_م - ميلاد)
# apl-source:31
print("بالأسابيع تقريبا:", (اليوم_م - ميلاد) // 7)
# apl-source:32
