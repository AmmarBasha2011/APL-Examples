
# apl-source:1
# مثال 302 — الأعداد الكاملة
# apl-source:2
# Perfect numbers
# apl-source:3
# Demonstrates: مجموع القواسم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/302-perfect-numbers.apl
# apl-source:6

# apl-source:7
def كامل(عدد):
    # apl-source:8
    مجموع = 0
    # apl-source:9
    for ق in range(1, عدد):
        # apl-source:10
        if عدد % ق == 0:
            # apl-source:11
            مجموع = مجموع + ق
    # apl-source:12
    return مجموع == عدد
# apl-source:13

# apl-source:14
print("6:", كامل(6))
# apl-source:15
print("28:", كامل(28))
# apl-source:16
print("12:", كامل(12))
# apl-source:17

# apl-source:18
قائمة = [ن for ن in range(1, 10000) if كامل(ن)]
# apl-source:19
print("الكاملة حتى 10000:", قائمة)
# apl-source:20
