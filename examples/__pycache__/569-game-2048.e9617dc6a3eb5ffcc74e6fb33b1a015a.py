
# apl-source:1
# مثال 569 — منطق لعبة 2048
# apl-source:2
# 2048 merge logic
# apl-source:3
# Demonstrates: 2048، دمج صفوف، انزلاق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/569-game-2048.apl
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
# منطق دمج 2048: انزلاق ودمج صف
# apl-source:15
def دمج_صف(صف):
    # apl-source:16
    مضغوط = [خ for خ in صف if خ != 0]
    # apl-source:17
    ناتج = list()
    # apl-source:18
    نقاط = 0
    # apl-source:19
    i = 0
    # apl-source:20
    while i < len(مضغوط):
        # apl-source:21
        if i + 1 < len(مضغوط) and مضغوط[i] == مضغوط[i + 1]:
            # apl-source:22
            ناتج.append(مضغوط[i] * 2)
            # apl-source:23
            نقاط = نقاط + مضغوط[i] * 2
            # apl-source:24
            i = i + 2
        # apl-source:25
        else:
            # apl-source:26
            ناتج.append(مضغوط[i])
            # apl-source:27
            i = i + 1
    # apl-source:28
    while len(ناتج) < len(صف):
        # apl-source:29
        ناتج.append(0)
    # apl-source:30
    return [ناتج, نقاط]
# apl-source:31

# apl-source:32
def حرك_يسار(لوحة):
    # apl-source:33
    جديدة = list()
    # apl-source:34
    إجمالي = 0
    # apl-source:35
    for صف in لوحة:
        # apl-source:36
        نتيجة = دمج_صف(صف)
        # apl-source:37
        جديدة.append(نتيجة[0])
        # apl-source:38
        إجمالي = إجمالي + نتيجة[1]
    # apl-source:39
    return [جديدة, إجمالي]
# apl-source:40

# apl-source:41
تأكد_يساوي(دمج_صف([2, 2, 4, 4])[0], [4, 8, 0, 0], "دمج مزدوج")
# apl-source:42
تأكد_يساوي(دمج_صف([2, 2, 2, 0])[0], [4, 2, 0, 0], "ثلاثة متشابهة")
# apl-source:43
تأكد_يساوي(دمج_صف([4, 0, 4, 8])[0], [8, 8, 0, 0], "انزلاق ثم دمج")
# apl-source:44
تأكد_يساوي(دمج_صف([2, 2, 4, 4])[1], 12, "النقاط")
# apl-source:45
لوحة = [[2, 2, 0, 0], [4, 4, 4, 4], [0, 0, 2, 2], [2, 4, 8, 16]]
# apl-source:46
تأكد_يساوي(حرك_يسار(لوحة)[1], 24, "نقاط الحركة")
# apl-source:47
