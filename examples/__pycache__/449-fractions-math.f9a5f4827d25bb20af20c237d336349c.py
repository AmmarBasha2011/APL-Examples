
# apl-source:1
# مثال 449 — كسور رياضية
# apl-source:2
# Fraction arithmetic
# apl-source:3
# Demonstrates: جمع وضرب وتبسيط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/449-fractions-math.apl
# apl-source:6

# apl-source:7
def قاسم_مشترك(أ, ب):
    # apl-source:8
    while ب != 0:
        # apl-source:9
        بدل = ب
        # apl-source:10
        ب = أ % ب
        # apl-source:11
        أ = بدل
    # apl-source:12
    return أ
# apl-source:13

# apl-source:14
def بسط_كسر(بسط, مقام_عدد):
    # apl-source:15
    ق = قاسم_مشترك(abs(بسط), abs(مقام_عدد))
    # apl-source:16
    return [بسط // ق, مقام_عدد // ق]
# apl-source:17

# apl-source:18
def اجمع_كسر(ب1, م1, ب2, م2):
    # apl-source:19
    return بسط_كسر(ب1 * م2 + ب2 * م1, م1 * م2)
# apl-source:20

# apl-source:21
def اضرب_كسر(ب1, م1, ب2, م2):
    # apl-source:22
    return بسط_كسر(ب1 * ب2, م1 * م2)
# apl-source:23

# apl-source:24
print("1/2 + 1/3 =", اجمع_كسر(1, 2, 1, 3))
# apl-source:25
print("2/3 * 3/4 =", اضرب_كسر(2, 3, 3, 4))
# apl-source:26
print("تبسيط 10/15 =", بسط_كسر(10, 15))
# apl-source:27
