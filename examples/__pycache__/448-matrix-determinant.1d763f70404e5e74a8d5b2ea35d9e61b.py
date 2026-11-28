
# apl-source:1
# مثال 448 — محدد المصفوفة
# apl-source:2
# Matrix determinant
# apl-source:3
# Demonstrates: 2x2 و 3x3
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/448-matrix-determinant.apl
# apl-source:6

# apl-source:7
def محدد2(م):
    # apl-source:8
    return م[0][0] * م[1][1] - م[0][1] * م[1][0]
# apl-source:9

# apl-source:10
def محدد3(م):
    # apl-source:11
    أ = م[0][0] * (م[1][1] * م[2][2] - م[1][2] * م[2][1])
    # apl-source:12
    ب = م[0][1] * (م[1][0] * م[2][2] - م[1][2] * م[2][0])
    # apl-source:13
    ج = م[0][2] * (م[1][0] * م[2][1] - م[1][1] * م[2][0])
    # apl-source:14
    return أ - ب + ج
# apl-source:15

# apl-source:16
print(محدد2([[1, 2], [3, 4]]))
# apl-source:17
print(محدد3([[1, 2, 3], [0, 1, 4], [5, 6, 0]]))
# apl-source:18
