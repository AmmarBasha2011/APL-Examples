
# apl-source:1
# مثال 354 — كسر اعتيادي يدوي
# apl-source:2
# Manual rational numbers
# apl-source:3
# Demonstrates: تبسيط وجمع الكسور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/354-rational.apl
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
class كسر_يدوي:
    # apl-source:15
    def __init__(ذات, فوق_كسر, تحت_كسر):
        # apl-source:16
        ق = قاسم_مشترك(فوق_كسر, تحت_كسر)
        # apl-source:17
        ذات.فوق_كسر = فوق_كسر // ق
        # apl-source:18
        ذات.تحت_كسر = تحت_كسر // ق
# apl-source:19

    # apl-source:20
    def اجمع(ذات, آخر):
        # apl-source:21
        ب = ذات.فوق_كسر * آخر.تحت_كسر + آخر.فوق_كسر * ذات.تحت_كسر
        # apl-source:22
        م = ذات.تحت_كسر * آخر.تحت_كسر
        # apl-source:23
        return كسر_يدوي(ب, م)
# apl-source:24

    # apl-source:25
    def كنص(ذات):
        # apl-source:26
        return str(ذات.فوق_كسر) + "/" + str(ذات.تحت_كسر)
# apl-source:27

# apl-source:28
أ = كسر_يدوي(1, 2)
# apl-source:29
ب = كسر_يدوي(1, 3)
# apl-source:30
print("1/2 + 1/3 =", أ.اجمع(ب).كنص())
# apl-source:31
print("تبسيط 4/8 =", كسر_يدوي(4, 8).كنص())
# apl-source:32
