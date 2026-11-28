
# apl-source:1
# مثال 540 — مصفوفة Z
# apl-source:2
# Z-algorithm
# apl-source:3
# Demonstrates: مصفوفة Z، مطابقة أنماط خطية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/540-z-algorithm.apl
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
# مصفوفة Z للبحث عن نمط
# apl-source:15
def مصفوفة_زد(نص):
    # apl-source:16
    ن = len(نص)
    # apl-source:17
    ز = [0] * ن
    # apl-source:18
    ب = 0
    # apl-source:19
    ي = 0
    # apl-source:20
    for i in range(1, ن):
        # apl-source:21
        if i <= ي:
            # apl-source:22
            ز[i] = min(ي - i + 1, ز[i - ب])
        # apl-source:23
        while i + ز[i] < ن and نص[ز[i]] == نص[i + ز[i]]:
            # apl-source:24
            ز[i] = ز[i] + 1
        # apl-source:25
        if i + ز[i] - 1 > ي:
            # apl-source:26
            ب = i
            # apl-source:27
            ي = i + ز[i] - 1
    # apl-source:28
    return ز
# apl-source:29

# apl-source:30
def بحث_زد(نص, نمط):
    # apl-source:31
    مدمج = نمط + "#" + نص
    # apl-source:32
    ز = مصفوفة_زد(مدمج)
    # apl-source:33
    مواضع = list()
    # apl-source:34
    for i in range(len(نمط) + 1, len(مدمج)):
        # apl-source:35
        if ز[i] == len(نمط):
            # apl-source:36
            مواضع.append(i - len(نمط) - 1)
    # apl-source:37
    return مواضع
# apl-source:38

# apl-source:39
تأكد_يساوي(مصفوفة_زد("aabxaab"), [0, 1, 0, 0, 3, 1, 0], "مصفوفة Z")
# apl-source:40
تأكد_يساوي(بحث_زد("abxabcabcaby", "abc"), [3, 6], "مواضع التطابق")
# apl-source:41
