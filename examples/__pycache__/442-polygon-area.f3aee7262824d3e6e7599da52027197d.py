
# apl-source:1
# مثال 442 — مساحة مضلع
# apl-source:2
# Polygon area (shoelace)
# apl-source:3
# Demonstrates: صيغة شوليس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/442-polygon-area.apl
# apl-source:6

# apl-source:7
def مساحة_مضلع(نقاط):
    # apl-source:8
    ن = len(نقاط)
    # apl-source:9
    مجموع = 0
    # apl-source:10
    for ي in range(ن):
        # apl-source:11
        ز = (ي + 1) % ن
        # apl-source:12
        مجموع = مجموع + نقاط[ي][0] * نقاط[ز][1] - نقاط[ز][0] * نقاط[ي][1]
    # apl-source:13
    return abs(مجموع) / 2
# apl-source:14

# apl-source:15
print("مربع 4x4:", مساحة_مضلع([[0, 0], [4, 0], [4, 4], [0, 4]]))
# apl-source:16
print("مثلث:", مساحة_مضلع([[0, 0], [4, 0], [2, 3]]))
# apl-source:17
