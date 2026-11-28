
# apl-source:1
# مثال 263 — صراف آلي مبسط
# apl-source:2
# Simple ATM
# apl-source:3
# Demonstrates: رصيد وعمليات، ورق نقدي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/263-atm.apl
# apl-source:6

# apl-source:7
رصيد = 2500
# apl-source:8

# apl-source:9
def اسحب_نقد(مبلغ):
    # apl-source:10
    عام_رصيد = رصيد
    # apl-source:11
    if مبلغ > رصيد:
        # apl-source:12
        return "رصيد غير كاف"
    # apl-source:13
    if مبلغ % 50 != 0:
        # apl-source:14
        return "المبلغ يجب أن يكون من مضاعفات 50"
    # apl-source:15
    return "تم صرف " + str(مبلغ)
# apl-source:16

# apl-source:17
print(اسحب_نقد(500))
# apl-source:18
print(اسحب_نقد(130))
# apl-source:19
print(اسحب_نقد(99999))
# apl-source:20

# apl-source:21
فئات = [200, 100, 50]
# apl-source:22
مطلوب = 750
# apl-source:23
print("صرف", مطلوب, ":")
# apl-source:24
for فئة in فئات:
    # apl-source:25
    عدد = مطلوب // فئة
    # apl-source:26
    مطلوب = مطلوب % فئة
    # apl-source:27
    if عدد > 0:
        # apl-source:28
        print(" ", عدد, "×", فئة)
# apl-source:29
