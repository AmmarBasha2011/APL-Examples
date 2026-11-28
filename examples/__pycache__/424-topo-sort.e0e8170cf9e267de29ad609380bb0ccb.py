
# apl-source:1
# مثال 424 — الترتيب الطوبولوجي
# apl-source:2
# Topological sort
# apl-source:3
# Demonstrates: خوارزمية كان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/424-topo-sort.apl
# apl-source:6

# apl-source:7
جيران = {
    # apl-source:8
    "ملابس داخلية": ["بنطلون"],
    # apl-source:9
    "قميص": ["جاكيت"],
    # apl-source:10
    "بنطلون": ["حذاء", "جاكيت"],
    # apl-source:11
    "حذاء": [],
    # apl-source:12
    "جاكيت": []
# apl-source:13
}
# apl-source:14

# apl-source:15
درجة = {}
# apl-source:16
for عقدة in جيران.keys():
    # apl-source:17
    درجة[عقدة] = 0
# apl-source:18
for عقدة in جيران.keys():
    # apl-source:19
    for جار in جيران[عقدة]:
        # apl-source:20
        درجة[جار] = درجة[جار] + 1
# apl-source:21

# apl-source:22
جاهزة = []
# apl-source:23
for عقدة in جيران.keys():
    # apl-source:24
    if درجة[عقدة] == 0:
        # apl-source:25
        جاهزة.append(عقدة)
# apl-source:26

# apl-source:27
ترتيب = []
# apl-source:28
while len(جاهزة) > 0:
    # apl-source:29
    عقدة = جاهزة.pop()
    # apl-source:30
    ترتيب.append(عقدة)
    # apl-source:31
    for جار in جيران[عقدة]:
        # apl-source:32
        درجة[جار] = درجة[جار] - 1
        # apl-source:33
        if درجة[جار] == 0:
            # apl-source:34
            جاهزة.append(جار)
# apl-source:35

# apl-source:36
print("ترتيب اللبس:", ترتيب)
# apl-source:37
