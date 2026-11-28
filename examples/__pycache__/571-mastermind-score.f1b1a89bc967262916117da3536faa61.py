
# apl-source:1
# مثال 571 — تقييم ماسترمايند
# apl-source:2
# Mastermind scoring
# apl-source:3
# Demonstrates: ماسترمايند، دقيق ولوني، تكرارات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/571-mastermind-score.apl
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
# تقييم ماسترمايند: دقيق ولون فقط
# apl-source:15
def قيّم(سر, تخمين):
    # apl-source:16
    دقيق = 0
    # apl-source:17
    بقايا_سر = list()
    # apl-source:18
    بقايا_تخمين = list()
    # apl-source:19
    for i in range(len(سر)):
        # apl-source:20
        if سر[i] == تخمين[i]:
            # apl-source:21
            دقيق = دقيق + 1
        # apl-source:22
        else:
            # apl-source:23
            بقايا_سر.append(سر[i])
            # apl-source:24
            بقايا_تخمين.append(تخمين[i])
    # apl-source:25
    لوني = 0
    # apl-source:26
    for عنصر in بقايا_تخمين:
        # apl-source:27
        if عنصر in بقايا_سر:
            # apl-source:28
            لوني = لوني + 1
            # apl-source:29
            بقايا_سر.remove(عنصر)
    # apl-source:30
    return [دقيق, لوني]
# apl-source:31

# apl-source:32
تأكد_يساوي(قيّم([1, 2, 3, 4], [1, 3, 2, 4]), [2, 2], "اثنان دقيق واثنان لوني")
# apl-source:33
تأكد_يساوي(قيّم([1, 1, 2, 2], [1, 2, 3, 4]), [1, 1], "مع تكرار")
# apl-source:34
تأكد_يساوي(قيّم([5, 6, 7, 8], [5, 6, 7, 8]), [4, 0], "مطابقة تامة")
# apl-source:35
