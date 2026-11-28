
# apl-source:1
# مثال 259 — عداد تنازلي لتاريخ
# apl-source:2
# Countdown to a date
# apl-source:3
# Demonstrates: فرق التواريخ بالأيام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/259-countdown.apl
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
اليوم_م = أيام_منذ_الميلاد(23, 11, 2026)
# apl-source:29
رأس_السنة_م = أيام_منذ_الميلاد(1, 1, 2027)
# apl-source:30
print("باقي على رأس السنة_م:", رأس_السنة_م - اليوم_م, "يوم_ما")
# apl-source:31
