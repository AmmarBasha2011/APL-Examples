
# apl-source:1
# مثال 252 — الفائدة المركبة
# apl-source:2
# Compound interest
# apl-source:3
# Demonstrates: نمو سنوي مركب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/252-compound-interest.apl
# apl-source:6

# apl-source:7
def فائدة_مركبة(أصل, نسبة, سنوات):
    # apl-source:8
    مبلغ = أصل
    # apl-source:9
    for سنة in range(1, سنوات + 1):
        # apl-source:10
        مبلغ = مبلغ * (1 + نسبة / 100)
        # apl-source:11
        print("سنة", سنة, ":", round(مبلغ, 2))
    # apl-source:12
    return مبلغ
# apl-source:13

# apl-source:14
نهائي = فائدة_مركبة(1000, 5, 5)
# apl-source:15
print("ربحت:", round(نهائي - 1000, 2))
# apl-source:16
