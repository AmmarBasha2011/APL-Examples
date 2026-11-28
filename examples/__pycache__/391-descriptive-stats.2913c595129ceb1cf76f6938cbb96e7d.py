
# apl-source:1
# مثال 391 — إحصاءات وصفية
# apl-source:2
# Descriptive statistics
# apl-source:3
# Demonstrates: المتوسط، الوسيط، المنوال يدويا
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/391-descriptive-stats.apl
# apl-source:6

# apl-source:7
def متوسط(قائمة):
    # apl-source:8
    مجموع = 0
    # apl-source:9
    for ق in قائمة:
        # apl-source:10
        مجموع = مجموع + ق
    # apl-source:11
    return مجموع / len(قائمة)
# apl-source:12

# apl-source:13
def وسيط_قائمة(قائمة):
    # apl-source:14
    م = sorted(قائمة)
    # apl-source:15
    ن = len(م)
    # apl-source:16
    if ن % 2 == 1:
        # apl-source:17
        return م[ن // 2]
    # apl-source:18
    return (م[ن // 2 - 1] + م[ن // 2]) / 2
# apl-source:19

# apl-source:20
def منوال(قائمة):
    # apl-source:21
    تكرار = {}
    # apl-source:22
    for ق in قائمة:
        # apl-source:23
        قديم = تكرار.get(ق, 0)
        # apl-source:24
        تكرار[ق] = قديم + 1
    # apl-source:25
    أفضل = قائمة[0]
    # apl-source:26
    for مفتاح in تكرار.keys():
        # apl-source:27
        if تكرار[مفتاح] > تكرار[أفضل]:
            # apl-source:28
            أفضل = مفتاح
    # apl-source:29
    return أفضل
# apl-source:30

# apl-source:31
بيانات = [12, 15, 12, 18, 20, 15, 12, 22, 25]
# apl-source:32
print("المتوسط:", متوسط(بيانات))
# apl-source:33
print("الوسيط:", وسيط_قائمة(بيانات))
# apl-source:34
print("المنوال:", منوال(بيانات))
# apl-source:35
