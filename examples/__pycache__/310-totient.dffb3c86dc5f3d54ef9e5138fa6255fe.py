
# apl-source:1
# مثال 310 — دالة أويلر (مؤشر القواسم المشتركة)
# apl-source:2
# Euler's totient
# apl-source:3
# Demonstrates: عد الأعداد الأولية النسبية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/310-totient.apl
# apl-source:6

# apl-source:7
def قاسم_مشترك(أ, ب):
    # apl-source:8
    while ب != 0:
        # apl-source:9
        مؤقت = ب
        # apl-source:10
        ب = أ % ب
        # apl-source:11
        أ = مؤقت
    # apl-source:12
    return أ
# apl-source:13

# apl-source:14
def أويلر(ن):
    # apl-source:15
    عدد = 0
    # apl-source:16
    for ك in range(1, ن + 1):
        # apl-source:17
        if قاسم_مشترك(ك, ن) == 1:
            # apl-source:18
            عدد = عدد + 1
    # apl-source:19
    return عدد
# apl-source:20

# apl-source:21
print("φ(9) =", أويلر(9))
# apl-source:22
print("φ(10) =", أويلر(10))
# apl-source:23
print("φ(13) =", أويلر(13))
# apl-source:24
