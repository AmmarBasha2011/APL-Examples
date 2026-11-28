
# apl-source:1
# مثال 423 — فحص الرسم الثنائي
# apl-source:2
# Bipartite graph check
# apl-source:3
# Demonstrates: تلوين بلونين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/423-graph-bipartite.apl
# apl-source:6

# apl-source:7
def ثنائي(جيران):
    # apl-source:8
    لون = {}
    # apl-source:9
    for بداية in جيران.keys():
        # apl-source:10
        if لون.get(بداية) == None:
            # apl-source:11
            لون[بداية] = 0
            # apl-source:12
            قائمة = [بداية]
            # apl-source:13
            while len(قائمة) > 0:
                # apl-source:14
                عقدة = قائمة.pop()
                # apl-source:15
                for جار in جيران[عقدة]:
                    # apl-source:16
                    if لون.get(جار) == None:
                        # apl-source:17
                        لون[جار] = 1 - لون[عقدة]
                        # apl-source:18
                        قائمة.append(جار)
                    # apl-source:19
                    elif لون[جار] == لون[عقدة]:
                        # apl-source:20
                        return False
    # apl-source:21
    return True
# apl-source:22

# apl-source:23
رسم1 = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
# apl-source:24
print("مربع:", ثنائي(رسم1))
# apl-source:25
رسم2 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
# apl-source:26
print("مثلث:", ثنائي(رسم2))
# apl-source:27
