
# apl-source:1
# مثال 328 — دمج قائمتين يدويا (zip)
# apl-source:2
# Manual zip
# apl-source:3
# Demonstrates: أزواج من قائمتين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/328-zip-manual.apl
# apl-source:6

# apl-source:7
def ازدوج(أ, ب):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    أقل = len(أ)
    # apl-source:10
    if len(ب) < أقل:
        # apl-source:11
        أقل = len(ب)
    # apl-source:12
    for ي in range(أقل):
        # apl-source:13
        نتيجة.append([أ[ي], ب[ي]])
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
print(ازدوج(["أحمد", "سارة"], [25, 30]))
# apl-source:17

# apl-source:18
قاموس = {}
# apl-source:19
for زوج in ازدوج(["مفتاح1", "مفتاح2"], ["قيمة1", "قيمة2"]):
    # apl-source:20
    قاموس[زوج[0]] = زوج[1]
# apl-source:21
print(قاموس)
# apl-source:22
