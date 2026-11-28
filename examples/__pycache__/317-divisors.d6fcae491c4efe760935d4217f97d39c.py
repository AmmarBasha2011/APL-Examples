
# apl-source:1
# مثال 317 — قواسم العدد
# apl-source:2
# Divisors of a number
# apl-source:3
# Demonstrates: إيجاد كل القواسم بكفاءة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/317-divisors.apl
# apl-source:6

# apl-source:7
def قواسم(عدد):
    # apl-source:8
    صغار = []
    # apl-source:9
    كبار = []
    # apl-source:10
    ق = 1
    # apl-source:11
    while ق * ق <= عدد:
        # apl-source:12
        if عدد % ق == 0:
            # apl-source:13
            صغار.append(ق)
            # apl-source:14
            if ق * ق != عدد:
                # apl-source:15
                كبار.append(عدد // ق)
        # apl-source:16
        ق = ق + 1
    # apl-source:17
    نتيجة = صغار
    # apl-source:18
    for ي in range(len(كبار)):
        # apl-source:19
        نتيجة.append(كبار[len(كبار) - 1 - ي])
    # apl-source:20
    return نتيجة
# apl-source:21

# apl-source:22
print("قواسم 28:", قواسم(28))
# apl-source:23
print("قواسم 36:", قواسم(36))
# apl-source:24
print("عدد قواسم 100:", len(قواسم(100)))
# apl-source:25
