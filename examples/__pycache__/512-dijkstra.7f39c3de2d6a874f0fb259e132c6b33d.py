
# apl-source:1
# مثال 512 — خوارزمية ديكسترا لأقصر مسار
# apl-source:2
# Dijkstra shortest path
# apl-source:3
# Demonstrates: أقصر مسار، رسم بياني موزون، اختيار الحد الأدنى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/512-dijkstra.apl
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
# أقصر مسار بخوارزمية ديكسترا (رسم موزون)
# apl-source:15
ج = dict()
# apl-source:16
ج["أ"] = {"ب": 4, "ج": 2}
# apl-source:17
ج["ب"] = {"ج": 1, "د": 5}
# apl-source:18
ج["ج"] = {"د": 8, "هـ": 10}
# apl-source:19
ج["د"] = {"هـ": 2}
# apl-source:20
ج["هـ"] = dict()
# apl-source:21

# apl-source:22
مسافات = dict()
# apl-source:23
for عقدة in ج:
    # apl-source:24
    مسافات[عقدة] = 999999
# apl-source:25
مسافات["أ"] = 0
# apl-source:26
مزارة = list()
# apl-source:27

# apl-source:28
while len(مزارة) < len(ج):
    # apl-source:29
    أقرب = ""
    # apl-source:30
    أقل = 999999
    # apl-source:31
    for عقدة in ج:
        # apl-source:32
        if عقدة not in مزارة and مسافات[عقدة] < أقل:
            # apl-source:33
            أقل = مسافات[عقدة]
            # apl-source:34
            أقرب = عقدة
    # apl-source:35
    if أقرب == "":
        # apl-source:36
        break
    # apl-source:37
    مزارة.append(أقرب)
    # apl-source:38
    for جار in ج[أقرب]:
        # apl-source:39
        بديل = مسافات[أقرب] + ج[أقرب][جار]
        # apl-source:40
        if بديل < مسافات[جار]:
            # apl-source:41
            مسافات[جار] = بديل
# apl-source:42

# apl-source:43
print("المسافات من أ:", مسافات)
# apl-source:44
تأكد_يساوي(مسافات["هـ"], 11, "ديكسترا: أ إلى هـ")
# apl-source:45
تأكد_يساوي(مسافات["د"], 9, "ديكسترا: أ إلى د")
# apl-source:46
