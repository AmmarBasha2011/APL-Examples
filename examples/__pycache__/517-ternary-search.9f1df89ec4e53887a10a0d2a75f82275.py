
# apl-source:1
# مثال 517 — البحث الثلاثي
# apl-source:2
# Ternary search
# apl-source:3
# Demonstrates: بحث ثلاثي، تقسيم ثلاثي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/517-ternary-search.apl
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
# بحث ثلاثي في قائمة مفرزة
# apl-source:15
def بحث_ثلاثي(ق, هدف):
    # apl-source:16
    ب = 0
    # apl-source:17
    ن = len(ق) - 1
    # apl-source:18
    while ب <= ن:
        # apl-source:19
        ث1 = ب + (ن - ب) // 3
        # apl-source:20
        ث2 = ن - (ن - ب) // 3
        # apl-source:21
        if ق[ث1] == هدف:
            # apl-source:22
            return ث1
        # apl-source:23
        if ق[ث2] == هدف:
            # apl-source:24
            return ث2
        # apl-source:25
        if هدف < ق[ث1]:
            # apl-source:26
            ن = ث1 - 1
        # apl-source:27
        elif هدف > ق[ث2]:
            # apl-source:28
            ب = ث2 + 1
        # apl-source:29
        else:
            # apl-source:30
            ب = ث1 + 1
            # apl-source:31
            ن = ث2 - 1
    # apl-source:32
    return -1
# apl-source:33

# apl-source:34
ق = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# apl-source:35
تأكد_يساوي(بحث_ثلاثي(ق, 23), 5, "ثلاثي: 23")
# apl-source:36
تأكد_يساوي(بحث_ثلاثي(ق, 91), 9, "ثلاثي: الأخير")
# apl-source:37
تأكد_يساوي(بحث_ثلاثي(ق, 4), -1, "ثلاثي: غائب")
# apl-source:38
