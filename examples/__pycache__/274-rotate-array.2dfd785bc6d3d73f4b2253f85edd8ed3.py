
# apl-source:1
# مثال 274 — تدوير المصفوفة
# apl-source:2
# Array rotation
# apl-source:3
# Demonstrates: تدوير يمين بخطوات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/274-rotate-array.apl
# apl-source:6

# apl-source:7
def دور(قائمة, خطوات):
    # apl-source:8
    ن = len(قائمة)
    # apl-source:9
    خطوات = خطوات % ن
    # apl-source:10
    return قائمة[ن - خطوات:] + قائمة[0:ن - خطوات]
# apl-source:11

# apl-source:12
print(دور([1, 2, 3, 4, 5, 6, 7], 3))
# apl-source:13
print(دور([1, 2, 3], 4))
# apl-source:14
print(دور([10, 20], 0))
# apl-source:15
