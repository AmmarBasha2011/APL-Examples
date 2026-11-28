
# apl-source:1
# مثال 425 — شجرة كروسكال الممتدة
# apl-source:2
# Kruskal's MST
# apl-source:3
# Demonstrates: دمج المجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/425-kruskal-mst.apl
# apl-source:6

# apl-source:7
def جذر(أصل, عقدة):
    # apl-source:8
    while أصل[عقدة] != عقدة:
        # apl-source:9
        عقدة = أصل[عقدة]
    # apl-source:10
    return عقدة
# apl-source:11

# apl-source:12
حواف = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2], [2, 3, 4]]
# apl-source:13
مرتبة = []
# apl-source:14
for حافة in حواف:
    # apl-source:15
    مرتبة.append(حافة)
# apl-source:16
for ي in range(len(مرتبة)):
    # apl-source:17
    for ز in range(ي + 1, len(مرتبة)):
        # apl-source:18
        if مرتبة[ز][2] < مرتبة[ي][2]:
            # apl-source:19
            بدل = مرتبة[ي]
            # apl-source:20
            مرتبة[ي] = مرتبة[ز]
            # apl-source:21
            مرتبة[ز] = بدل
# apl-source:22

# apl-source:23
أصل = {0: 0, 1: 1, 2: 2, 3: 3}
# apl-source:24
تكلفة = 0
# apl-source:25
مختارة = []
# apl-source:26
for حافة in مرتبة:
    # apl-source:27
    ج1 = جذر(أصل, حافة[0])
    # apl-source:28
    ج2 = جذر(أصل, حافة[1])
    # apl-source:29
    if ج1 != ج2:
        # apl-source:30
        أصل[ج1] = ج2
        # apl-source:31
        تكلفة = تكلفة + حافة[2]
        # apl-source:32
        مختارة.append(حافة)
# apl-source:33

# apl-source:34
print("الحواف المختارة:", مختارة)
# apl-source:35
print("التكلفة:", تكلفة)
# apl-source:36
