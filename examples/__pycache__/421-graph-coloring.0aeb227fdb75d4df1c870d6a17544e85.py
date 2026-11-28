
# apl-source:1
# مثال 421 — تلوين الرسم البياني
# apl-source:2
# Graph coloring (greedy)
# apl-source:3
# Demonstrates: خوارزمية جشعة للتلوين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/421-graph-coloring.apl
# apl-source:6

# apl-source:7
جيران = {
    # apl-source:8
    0: [1, 2],
    # apl-source:9
    1: [0, 2, 3],
    # apl-source:10
    2: [0, 1, 3],
    # apl-source:11
    3: [1, 2]
# apl-source:12
}
# apl-source:13

# apl-source:14
ألوان = {}
# apl-source:15
for عقدة in جيران.keys():
    # apl-source:16
    مستخدمة = []
    # apl-source:17
    for جار in جيران[عقدة]:
        # apl-source:18
        if ألوان.get(جار) != None:
            # apl-source:19
            مستخدمة.append(ألوان[جار])
    # apl-source:20
    لون = 0
    # apl-source:21
    while مستخدمة.count(لون) > 0:
        # apl-source:22
        لون = لون + 1
    # apl-source:23
    ألوان[عقدة] = لون
# apl-source:24

# apl-source:25
print("التلوين:", ألوان)
# apl-source:26
