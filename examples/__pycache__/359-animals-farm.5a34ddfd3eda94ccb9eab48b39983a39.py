
# apl-source:1
# مثال 359 — مزرعة حيوانات
# apl-source:2
# Animal farm
# apl-source:3
# Demonstrates: عد وتجميع بالفصيلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/359-animals-farm.apl
# apl-source:6

# apl-source:7
class حيوان_مزرعة:
    # apl-source:8
    def __init__(ذات, فصيلة, اسم, عمر):
        # apl-source:9
        ذات.فصيلة = فصيلة
        # apl-source:10
        ذات.اسم = اسم
        # apl-source:11
        ذات.عمر = عمر
# apl-source:12

# apl-source:13
مزرعة = [
    # apl-source:14
    حيوان_مزرعة("بقرة", "بهيمة", 5),
    # apl-source:15
    حيوان_مزرعة("دجاجة", "كوكو", 1),
    # apl-source:16
    حيوان_مزرعة("بقرة", "زبيدة", 3),
    # apl-source:17
    حيوان_مزرعة("حصان", "صقر", 7),
    # apl-source:18
    حيوان_مزرعة("دجاجة", "بيبي", 2)
# apl-source:19
]
# apl-source:20

# apl-source:21
بالفصيلة = {}
# apl-source:22
for ح in مزرعة:
    # apl-source:23
    if ح.فصيلة in بالفصيلة:
        # apl-source:24
        بالفصيلة[ح.فصيلة] = بالفصيلة[ح.فصيلة] + 1
    # apl-source:25
    else:
        # apl-source:26
        بالفصيلة[ح.فصيلة] = 1
# apl-source:27

# apl-source:28
for فصيلة in بالفصيلة:
    # apl-source:29
    print(فصيلة, ":", بالفصيلة[فصيلة])
# apl-source:30

# apl-source:31
أكبر_عمر = مزرعة[0]
# apl-source:32
for ح in مزرعة:
    # apl-source:33
    if ح.عمر > أكبر_عمر.عمر:
        # apl-source:34
        أكبر_عمر = ح
# apl-source:35
print("الأكبر سنا:", أكبر_عمر.اسم, "(", أكبر_عمر.عمر, "سنوات)")
# apl-source:36
