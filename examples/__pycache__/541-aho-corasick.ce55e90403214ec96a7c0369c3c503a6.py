
# apl-source:1
# مثال 541 — أتمتة أهو-كوراسيك
# apl-source:2
# Aho-Corasick automaton
# apl-source:3
# Demonstrates: أنماط متعددة، أتمتة، روابط فشل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/541-aho-corasick.apl
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
# أتمتة أهو-كوراسيك للبحث بعدة أنماط معاً
# apl-source:15
أنماط = ["he", "she", "his", "hers"]
# apl-source:16
عقد = [dict()]
# apl-source:17
فشل = [0]
# apl-source:18
مخرجات = [list()]
# apl-source:19

# apl-source:20
for نمط in أنماط:
    # apl-source:21
    عقدة = 0
    # apl-source:22
    for حرف in نمط:
        # apl-source:23
        if حرف not in عقد[عقدة]:
            # apl-source:24
            عقد[عقدة][حرف] = len(عقد)
            # apl-source:25
            عقد.append(dict())
            # apl-source:26
            فشل.append(0)
            # apl-source:27
            مخرجات.append(list())
        # apl-source:28
        عقدة = عقد[عقدة][حرف]
    # apl-source:29
    مخرجات[عقدة].append(نمط)
# apl-source:30

# apl-source:31
طابور = list()
# apl-source:32
for حرف in عقد[0]:
    # apl-source:33
    طابور.append(عقد[0][حرف])
# apl-source:34
while len(طابور) > 0:
    # apl-source:35
    حالية = طابور.pop(0)
    # apl-source:36
    for حرف in عقد[حالية]:
        # apl-source:37
        تالية = عقد[حالية][حرف]
        # apl-source:38
        طابور.append(تالية)
        # apl-source:39
        ج = فشل[حالية]
        # apl-source:40
        while ج != 0 and حرف not in عقد[ج]:
            # apl-source:41
            ج = فشل[ج]
        # apl-source:42
        if حرف in عقد[ج]:
            # apl-source:43
            فشل[تالية] = عقد[ج][حرف]
        # apl-source:44
        مخرجات[تالية] = مخرجات[تالية] + مخرجات[فشل[تالية]]
# apl-source:45

# apl-source:46
نص = "ushers"
# apl-source:47
عقدة = 0
# apl-source:48
نتائج = list()
# apl-source:49
for حرف in نص:
    # apl-source:50
    while عقدة != 0 and حرف not in عقد[عقدة]:
        # apl-source:51
        عقدة = فشل[عقدة]
    # apl-source:52
    if حرف in عقد[عقدة]:
        # apl-source:53
        عقدة = عقد[عقدة][حرف]
    # apl-source:54
    for نمط in مخرجات[عقدة]:
        # apl-source:55
        نتائج.append(نمط)
# apl-source:56

# apl-source:57
print("التطابقات:", نتائج)
# apl-source:58
تأكد_يساوي(نتائج, ["she", "he", "hers"], "أهو-كوراسيك: ثلاثة تطابقات")
# apl-source:59
