
# apl-source:1
# مثال 362 — القاسم المشترك بإقليدس العودي
# apl-source:2
# Recursive Euclid GCD
# apl-source:3
# Demonstrates: عودية رياضية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/362-gcd-euclid.apl
# apl-source:6

# apl-source:7
def قاسم(أ, ب):
    # apl-source:8
    if ب == 0:
        # apl-source:9
        return أ
    # apl-source:10
    return قاسم(ب, أ % ب)
# apl-source:11

# apl-source:12
print("ق.م.أ(48, 18) =", قاسم(48, 18))
# apl-source:13
print("ق.م.أ(100, 75) =", قاسم(100, 75))
# apl-source:14
print("ق.م.أ(17, 5) =", قاسم(17, 5))
# apl-source:15
