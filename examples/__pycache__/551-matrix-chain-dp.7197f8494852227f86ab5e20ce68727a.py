
# apl-source:1
# مثال 551 — ترتيب ضرب المصفوفات
# apl-source:2
# Matrix chain multiplication DP
# apl-source:3
# Demonstrates: برمجة ديناميكية، ضرب مصفوفات، أقل كلفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/551-matrix-chain-dp.apl
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
# ترتيب ضرب المصفوفات بأقل كلفة (برمجة ديناميكية)
# apl-source:15
def أقل_كلفة(أبعاد):
    # apl-source:16
    ن = len(أبعاد) - 1
    # apl-source:17
    جدول = list()
    # apl-source:18
    for i in range(ن):
        # apl-source:19
        جدول.append([0] * ن)
    # apl-source:20
    for طول_سلسلة in range(2, ن + 1):
        # apl-source:21
        for i in range(ن - طول_سلسلة + 1):
            # apl-source:22
            j = i + طول_سلسلة - 1
            # apl-source:23
            جدول[i][j] = 999999999
            # apl-source:24
            for ك in range(i, j):
                # apl-source:25
                كلفة = جدول[i][ك] + جدول[ك + 1][j] + أبعاد[i] * أبعاد[ك + 1] * أبعاد[j + 1]
                # apl-source:26
                if كلفة < جدول[i][j]:
                    # apl-source:27
                    جدول[i][j] = كلفة
    # apl-source:28
    return جدول[0][ن - 1]
# apl-source:29

# apl-source:30
تأكد_يساوي(أقل_كلفة([40, 20, 30, 10, 30]), 26000, "المثال الكلاسيكي")
# apl-source:31
تأكد_يساوي(أقل_كلفة([10, 20, 30]), 6000, "مصفوفتان")
# apl-source:32
