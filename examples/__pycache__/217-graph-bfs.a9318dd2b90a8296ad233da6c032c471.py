
# apl-source:1
# مثال 217 — المسح بالعرض للرسم البياني
# apl-source:2
# Graph BFS
# apl-source:3
# Demonstrates: طابور + مجموعة زيارات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/217-graph-bfs.apl
# apl-source:6

# apl-source:7
def مسح_عرض(رسم, بداية):
    # apl-source:8
    مزارة = []
    # apl-source:9
    طابور = [بداية]
    # apl-source:10
    في_الطابور = {بداية: True}
    # apl-source:11
    while len(طابور) > 0:
        # apl-source:12
        عقدة = طابور.pop(0)
        # apl-source:13
        مزارة.append(عقدة)
        # apl-source:14
        for جار in رسم[عقدة]:
            # apl-source:15
            if جار not in في_الطابور:
                # apl-source:16
                في_الطابور[جار] = True
                # apl-source:17
                طابور.append(جار)
    # apl-source:18
    return مزارة
# apl-source:19

# apl-source:20
رسم = {
    # apl-source:21
    "أ": ["ب", "ج"],
    # apl-source:22
    "ب": ["أ", "د", "ه"],
    # apl-source:23
    "ج": ["أ", "د"],
    # apl-source:24
    "د": ["ب", "ج", "ه"],
    # apl-source:25
    "ه": ["ب", "د"]
# apl-source:26
}
# apl-source:27
print("المسح بالعرض من أ:", مسح_عرض(رسم, "أ"))
# apl-source:28
