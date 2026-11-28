
# apl-source:1
# مثال 573 — مكونات تارجان القوية
# apl-source:2
# Tarjan strongly connected components
# apl-source:3
# Demonstrates: تارجان، مكونات قوية، رسم موجه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/573-tarjan-scc.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# مكونات تارجان المتصلة قوياً (رسم موجه)
# apl-source:15
رسم = {"أ": ["ب"], "ب": ["ج"], "ج": ["أ", "د"], "د": ["هـ"], "هـ": ["د"]}
# apl-source:16
فهارس = dict()
# apl-source:17
منخفض = dict()
# apl-source:18
مكدس = list()
# apl-source:19
على_مكدس = dict()
# apl-source:20
عداد = [0]
# apl-source:21
مكونات = list()
# apl-source:22

# apl-source:23
def قوي(عقدة):
    # apl-source:24
    فهارس[عقدة] = عداد[0]
    # apl-source:25
    منخفض[عقدة] = عداد[0]
    # apl-source:26
    عداد[0] = عداد[0] + 1
    # apl-source:27
    مكدس.append(عقدة)
    # apl-source:28
    على_مكدس[عقدة] = True
    # apl-source:29
    for جار in رسم[عقدة]:
        # apl-source:30
        if جار not in فهارس:
            # apl-source:31
            قوي(جار)
            # apl-source:32
            منخفض[عقدة] = min(منخفض[عقدة], منخفض[جار])
        # apl-source:33
        elif جار in على_مكدس:
            # apl-source:34
            منخفض[عقدة] = min(منخفض[عقدة], فهارس[جار])
    # apl-source:35
    if منخفض[عقدة] == فهارس[عقدة]:
        # apl-source:36
        مكون = list()
        # apl-source:37
        قمة = ""
        # apl-source:38
        while قمة != عقدة:
            # apl-source:39
            قمة = مكدس.pop()
            # apl-source:40
            مكون.append(قمة)
            # apl-source:41
            على_مكدس[قمة] = False
        # apl-source:42
        مكونات.append(sorted(مكون))
# apl-source:43

# apl-source:44
for عقدة in رسم:
    # apl-source:45
    if عقدة not in فهارس:
        # apl-source:46
        قوي(عقدة)
# apl-source:47

# apl-source:48
print("المكونات:", مكونات)
# apl-source:49
تأكد_يساوي(len(مكونات), 2, "مكونان")
# apl-source:50
تأكد_يساوي(مكونات[0], ["د", "هـ"], "دورة د-هـ")
# apl-source:51
تأكد_يساوي(مكونات[1], ["أ", "ب", "ج"], "دورة أ-ب-ج")
# apl-source:52
