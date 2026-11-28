
# apl-source:1
# مثال 444 — صحة المثلث ونوعه
# apl-source:2
# Triangle validity and type
# apl-source:3
# Demonstrates: متباينة المثلث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/444-triangle-check.apl
# apl-source:6

# apl-source:7
def نوع_مثلث(أ, ب, ج):
    # apl-source:8
    if أ + ب <= ج or أ + ج <= ب or ب + ج <= أ:
        # apl-source:9
        return "غير صالح"
    # apl-source:10
    if أ == ب and ب == ج:
        # apl-source:11
        return "متساوي الأضلاع"
    # apl-source:12
    if أ == ب or ب == ج or أ == ج:
        # apl-source:13
        return "متساوي الساقين"
    # apl-source:14
    return "مختلف الأضلاع"
# apl-source:15

# apl-source:16
print(نوع_مثلث(3, 4, 5))
# apl-source:17
print(نوع_مثلث(5, 5, 5))
# apl-source:18
print(نوع_مثلث(5, 5, 8))
# apl-source:19
print(نوع_مثلث(1, 2, 10))
# apl-source:20
