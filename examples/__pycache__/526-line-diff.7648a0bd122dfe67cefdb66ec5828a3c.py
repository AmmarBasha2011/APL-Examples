
# apl-source:1
# مثال 526 — مقارنة نصين سطرياً
# apl-source:2
# Line diff via LCS
# apl-source:3
# Demonstrates: أطول تتابع مشترك، فرق سطور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/526-line-diff.apl
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
# مقارنة نصين سطرياً بأطول تتابع مشترك
# apl-source:15
def فرق_سطور(قديم, جديد):
    # apl-source:16
    ن = len(قديم)
    # apl-source:17
    م = len(جديد)
    # apl-source:18
    جدول = list()
    # apl-source:19
    for i in range(ن + 1):
        # apl-source:20
        صف = [0]
        # apl-source:21
        for j in range(م):
            # apl-source:22
            صف.append(0)
        # apl-source:23
        جدول.append(صف)
    # apl-source:24
    for i in range(1, ن + 1):
        # apl-source:25
        for j in range(1, م + 1):
            # apl-source:26
            if قديم[i - 1] == جديد[j - 1]:
                # apl-source:27
                جدول[i][j] = جدول[i - 1][j - 1] + 1
            # apl-source:28
            else:
                # apl-source:29
                جدول[i][j] = max(جدول[i - 1][j], جدول[i][j - 1])
    # apl-source:30
    تغييرات = list()
    # apl-source:31
    i = ن
    # apl-source:32
    j = م
    # apl-source:33
    while i > 0 or j > 0:
        # apl-source:34
        if i > 0 and j > 0 and قديم[i - 1] == جديد[j - 1]:
            # apl-source:35
            تغييرات.append("  " + قديم[i - 1])
            # apl-source:36
            i = i - 1
            # apl-source:37
            j = j - 1
        # apl-source:38
        elif j > 0 and (i == 0 or جدول[i][j - 1] >= جدول[i - 1][j]):
            # apl-source:39
            تغييرات.append("+ " + جديد[j - 1])
            # apl-source:40
            j = j - 1
        # apl-source:41
        else:
            # apl-source:42
            تغييرات.append("- " + قديم[i - 1])
            # apl-source:43
            i = i - 1
    # apl-source:44
    return تغييرات[::-1]
# apl-source:45

# apl-source:46
نتيجة = فرق_سطور(["أ", "ب", "ج"], ["أ", "ج", "د"])
# apl-source:47
for سطر in نتيجة:
    # apl-source:48
    print(سطر)
# apl-source:49
تأكد_يساوي(نتيجة, ["  أ", "- ب", "  ج", "+ د"], "فرق سطور")
# apl-source:50
