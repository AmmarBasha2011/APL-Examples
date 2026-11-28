
# apl-source:1
# مثال 422 — المكونات المتصلة
# apl-source:2
# Connected components
# apl-source:3
# Demonstrates: DFS لعد المكونات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/422-graph-components.apl
# apl-source:6

# apl-source:7
جيران = {
    # apl-source:8
    0: [1],
    # apl-source:9
    1: [0],
    # apl-source:10
    2: [3],
    # apl-source:11
    3: [2],
    # apl-source:12
    4: []
# apl-source:13
}
# apl-source:14

# apl-source:15
def امسح(عقدة, جيران, مزارة):
    # apl-source:16
    مزارة.append(عقدة)
    # apl-source:17
    for جار in جيران[عقدة]:
        # apl-source:18
        if مزارة.count(جار) == 0:
            # apl-source:19
            امسح(جار, جيران, مزارة)
# apl-source:20

# apl-source:21
مزارة = []
# apl-source:22
مكونات = 0
# apl-source:23
for عقدة in جيران.keys():
    # apl-source:24
    if مزارة.count(عقدة) == 0:
        # apl-source:25
        امسح(عقدة, جيران, مزارة)
        # apl-source:26
        مكونات = مكونات + 1
# apl-source:27

# apl-source:28
print("عدد المكونات:", مكونات)
# apl-source:29
