
# apl-source:1
# مثال 439 — توسيط وتعبئة النصوص
# apl-source:2
# Pad and center strings
# apl-source:3
# Demonstrates: توسيط عناوين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/439-pad-center.apl
# apl-source:6

# apl-source:7
def وسطي(نص_الدخل, عرض_مطلوب):
    # apl-source:8
    نقص = عرض_مطلوب - len(نص_الدخل)
    # apl-source:9
    if نقص <= 0:
        # apl-source:10
        return نص_الدخل
    # apl-source:11
    قبل = ""
    # apl-source:12
    for _ in range(نقص // 2):
        # apl-source:13
        قبل = قبل + " "
    # apl-source:14
    ناتج = قبل + نص_الدخل
    # apl-source:15
    while len(ناتج) < عرض_مطلوب:
        # apl-source:16
        ناتج = ناتج + " "
    # apl-source:17
    return ناتج
# apl-source:18

# apl-source:19
print("=" * 40)
# apl-source:20
print(وسطي("تقرير المبيعات", 40))
# apl-source:21
print("=" * 40)
# apl-source:22
