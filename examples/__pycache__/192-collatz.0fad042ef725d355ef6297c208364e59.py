
# apl-source:1
# مثال 192 — متتالية كولاتز
# apl-source:2
# Collatz sequence
# apl-source:3
# Demonstrates: طالما، الشروط، حساب الخطوات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/192-collatz.apl
# apl-source:6

# apl-source:7
def كولاتز(ن):
    # apl-source:8
    خطوات = 0
    # apl-source:9
    قمة = ن
    # apl-source:10
    while ن != 1:
        # apl-source:11
        if ن % 2 == 0:
            # apl-source:12
            ن = ن // 2
        # apl-source:13
        else:
            # apl-source:14
            ن = 3 * ن + 1
        # apl-source:15
        if ن > قمة:
            # apl-source:16
            قمة = ن
        # apl-source:17
        خطوات = خطوات + 1
    # apl-source:18
    return [خطوات, قمة]
# apl-source:19

# apl-source:20
for بداية in [6, 27, 97]:
    # apl-source:21
    نتيجة = كولاتز(بداية)
    # apl-source:22
    print("بدءا من", بداية, ": خطوات =", نتيجة[0], ", أعلى قيمة =", نتيجة[1])
# apl-source:23
