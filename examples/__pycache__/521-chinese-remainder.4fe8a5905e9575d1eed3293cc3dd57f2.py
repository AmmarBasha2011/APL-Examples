
# apl-source:1
# مثال 521 — مبرهنة الباقي الصينية
# apl-source:2
# Chinese remainder theorem
# apl-source:3
# Demonstrates: باقي صيني، توافقيات عددية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/521-chinese-remainder.apl
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
# مبرهنة الباقي الصينية ببحث مباشر
# apl-source:15
def باقي_صيني(بقايا, مقسومات, حد):
    # apl-source:16
    for س in range(1, حد + 1):
        # apl-source:17
        كلها = True
        # apl-source:18
        for i in range(len(بقايا)):
            # apl-source:19
            if س % مقسومات[i] != بقايا[i]:
                # apl-source:20
                كلها = False
        # apl-source:21
        if كلها:
            # apl-source:22
            return س
    # apl-source:23
    return -1
# apl-source:24

# apl-source:25
تأكد_يساوي(باقي_صيني([2, 3, 2], [3, 5, 7], 105), 23, "النظام الكلاسيكي")
# apl-source:26
تأكد_يساوي(باقي_صيني([1, 1], [2, 3], 6), 1, "نظام بسيط")
# apl-source:27
تأكد_يساوي(باقي_صيني([1, 2], [2, 4], 8), -1, "نظام متناقض")
# apl-source:28
