
# apl-source:1
# مثال 253 — جدول سداد قرض
# apl-source:2
# Loan amortization
# apl-source:3
# Demonstrates: قسط شهري وجدول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/253-loan-amortization.apl
# apl-source:6

# apl-source:7
def قسط_شهري(مبلغ, نسبة_سنوية, عدد_الشهور):
    # apl-source:8
    ر = نسبة_سنوية / 100 / 12
    # apl-source:9
    if ر == 0:
        # apl-source:10
        return مبلغ / عدد_الشهور
    # apl-source:11
    return مبلغ * ر / (1 - (1 + ر) ** -عدد_الشهور)
# apl-source:12

# apl-source:13
قسط = قسط_شهري(10000, 6, 12)
# apl-source:14
print("القسط الشهري:", round(قسط, 2))
# apl-source:15

# apl-source:16
متبقي = 10000
# apl-source:17
ر = 0.06
# apl-source:18
for شهر in range(1, 4):
    # apl-source:19
    فائدة = متبقي * ر
    # apl-source:20
    سداد_أصل = قسط - فائدة
    # apl-source:21
    متبقي = متبقي - سداد_أصل
    # apl-source:22
    print("شهر", شهر, ": فائدة", round(فائدة, 2), "| أصل", round(سداد_أصل, 2), "| متبقي", round(متبقي, 2))
# apl-source:23
