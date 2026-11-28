
# apl-source:1
# مثال 353 — صنف مصفوفة
# apl-source:2
# Matrix class
# apl-source:3
# Demonstrates: جمع وضرب مصفوفات 2x2
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/353-matrix-class.apl
# apl-source:6

# apl-source:7
class مصفوفة:
    # apl-source:8
    def __init__(ذات, خلايا):
        # apl-source:9
        ذات.خلايا = خلايا
# apl-source:10

    # apl-source:11
    def اجمع(ذات, أخرى):
        # apl-source:12
        نتيجة = []
        # apl-source:13
        for ي in range(2):
            # apl-source:14
            سطر = []
            # apl-source:15
            for ز in range(2):
                # apl-source:16
                سطر.append(ذات.خلايا[ي][ز] + أخرى.خلايا[ي][ز])
            # apl-source:17
            نتيجة.append(سطر)
        # apl-source:18
        return مصفوفة(نتيجة)
# apl-source:19

    # apl-source:20
    def محدد(ذات):
        # apl-source:21
        return ذات.خلايا[0][0] * ذات.خلايا[1][1] - ذات.خلايا[0][1] * ذات.خلايا[1][0]
# apl-source:22

    # apl-source:23
    def اطبعها(ذات):
        # apl-source:24
        for سطر in ذات.خلايا:
            # apl-source:25
            print(سطر)
# apl-source:26

# apl-source:27
أ = مصفوفة([[1, 2], [3, 4]])
# apl-source:28
ب = مصفوفة([[5, 6], [7, 8]])
# apl-source:29
أ.اجمع(ب).اطبعها()
# apl-source:30
print("محدد أ:", أ.محدد())
# apl-source:31
