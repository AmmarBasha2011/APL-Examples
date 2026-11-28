
# apl-source:1
# مثال 271 — أكبر مجموع متتالي (كادان)
# apl-source:2
# Kadane's algorithm
# apl-source:3
# Demonstrates: أقصى مجموع لمصفوفة فرعية متصلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/271-kadane.apl
# apl-source:6

# apl-source:7
def كادان(قائمة):
    # apl-source:8
    أفضل = قائمة[0]
    # apl-source:9
    حالي = قائمة[0]
    # apl-source:10
    for ي in range(1, len(قائمة)):
        # apl-source:11
        if حالي + قائمة[ي] > قائمة[ي]:
            # apl-source:12
            حالي = حالي + قائمة[ي]
        # apl-source:13
        else:
            # apl-source:14
            حالي = قائمة[ي]
        # apl-source:15
        if حالي > أفضل:
            # apl-source:16
            أفضل = حالي
    # apl-source:17
    return أفضل
# apl-source:18

# apl-source:19
print(كادان([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# apl-source:20
print(كادان([1, 2, 3, 4]))
# apl-source:21
print(كادان([-5, -1, -3]))
# apl-source:22
