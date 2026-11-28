
# apl-source:1
# مثال 218 — المسح بالعمق وإيجاد مسار
# apl-source:2
# Graph DFS and path finding
# apl-source:3
# Demonstrates: عودية مع مجموعة زيارات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/218-graph-dfs.apl
# apl-source:6

# apl-source:7
def مسح_عمق(رسم, عقدة, مزارة, نتيجة):
    # apl-source:8
    مزارة[عقدة] = True
    # apl-source:9
    نتيجة.append(عقدة)
    # apl-source:10
    for جار in رسم[عقدة]:
        # apl-source:11
        if جار not in مزارة:
            # apl-source:12
            مسح_عمق(رسم, جار, مزارة, نتيجة)
# apl-source:13

# apl-source:14
def جد_مسار(رسم, من, إلى, مزارة, مسار):
    # apl-source:15
    مزارة[من] = True
    # apl-source:16
    مسار.append(من)
    # apl-source:17
    if من == إلى:
        # apl-source:18
        return True
    # apl-source:19
    for جار in رسم[من]:
        # apl-source:20
        if جار not in مزارة:
            # apl-source:21
            if جد_مسار(رسم, جار, إلى, مزارة, مسار):
                # apl-source:22
                return True
    # apl-source:23
    مسار.pop()
    # apl-source:24
    return False
# apl-source:25

# apl-source:26
رسم = {
    # apl-source:27
    "أ": ["ب", "ج"],
    # apl-source:28
    "ب": ["أ", "د"],
    # apl-source:29
    "ج": ["أ", "د"],
    # apl-source:30
    "د": ["ب", "ج", "ه"],
    # apl-source:31
    "ه": ["د"]
# apl-source:32
}
# apl-source:33
نتيجة = []
# apl-source:34
مسح_عمق(رسم, "أ", {}, نتيجة)
# apl-source:35
print("المسح بالعمق:", نتيجة)
# apl-source:36

# apl-source:37
مسار = []
# apl-source:38
جد_مسار(رسم, "أ", "ه", {}, مسار)
# apl-source:39
print("مسار من أ إلى ه:", مسار)
# apl-source:40
