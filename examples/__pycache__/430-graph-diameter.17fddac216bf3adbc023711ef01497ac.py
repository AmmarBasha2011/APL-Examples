
# apl-source:1
# مثال 430 — قطر الشجرة
# apl-source:2
# Tree diameter
# apl-source:3
# Demonstrates: مسحان متتاليان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/430-graph-diameter.apl
# apl-source:6

# apl-source:7
def أبعد(جيران, بداية):
    # apl-source:8
    مسافات = {بداية: 0}
    # apl-source:9
    قائمة = [بداية]
    # apl-source:10
    أبعد_عقدة = بداية
    # apl-source:11
    while len(قائمة) > 0:
        # apl-source:12
        عقدة = قائمة.pop(0)
        # apl-source:13
        for جار in جيران[عقدة]:
            # apl-source:14
            if مسافات.get(جار) == None:
                # apl-source:15
                مسافات[جار] = مسافات[عقدة] + 1
                # apl-source:16
                قائمة.append(جار)
                # apl-source:17
                if مسافات[جار] > مسافات[أبعد_عقدة]:
                    # apl-source:18
                    أبعد_عقدة = جار
    # apl-source:19
    return [أبعد_عقدة, مسافات[أبعد_عقدة]]
# apl-source:20

# apl-source:21
جيران = {0: [1], 1: [0, 2, 3], 2: [1, 4], 3: [1], 4: [2]}
# apl-source:22
أول = أبعد(جيران, 0)
# apl-source:23
ثان = أبعد(جيران, أول[0])
# apl-source:24
print("القطر:", ثان[1])
# apl-source:25
