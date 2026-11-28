
# apl-source:1
# مثال 559 — التباديل المُخلّة
# apl-source:2
# Derangements
# apl-source:3
# Demonstrates: تباديل مُخلّة، توافيق، متكررة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/559-derangements.apl
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
# التباديل المُخلّة: لا عنصر في موضعه
# apl-source:15
def إخلالات(ن):
    # apl-source:16
    if ن == 1:
        # apl-source:17
        return 0
    # apl-source:18
    سابق2 = 1
    # apl-source:19
    سابق1 = 0
    # apl-source:20
    حالي = 0
    # apl-source:21
    for i in range(2, ن + 1):
        # apl-source:22
        حالي = (i - 1) * (سابق1 + سابق2)
        # apl-source:23
        سابق2 = سابق1
        # apl-source:24
        سابق1 = حالي
    # apl-source:25
    return حالي
# apl-source:26

# apl-source:27
تأكد_يساوي(إخلالات(4), 9, "!4")
# apl-source:28
تأكد_يساوي(إخلالات(5), 44, "!5")
# apl-source:29
تأكد_يساوي(إخلالات(6), 265, "!6")
# apl-source:30
تأكد_يساوي(إخلالات(1), 0, "!1")
# apl-source:31
