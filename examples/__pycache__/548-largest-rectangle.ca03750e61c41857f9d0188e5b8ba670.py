
# apl-source:1
# مثال 548 — أكبر مستطيل في هيستوجرام
# apl-source:2
# Largest rectangle in histogram
# apl-source:3
# Demonstrates: هيستوجرام، مكدس، مساحة قصوى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/548-largest-rectangle.apl
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
# أكبر مستطيل في هيستوجرام بمكدس
# apl-source:15
def أكبر_مستطيل(ارتفاعات):
    # apl-source:16
    مكدس = list()
    # apl-source:17
    أقصى = 0
    # apl-source:18
    ن = len(ارتفاعات)
    # apl-source:19
    for i in range(ن + 1):
        # apl-source:20
        حالي = 0
        # apl-source:21
        if i < ن:
            # apl-source:22
            حالي = ارتفاعات[i]
        # apl-source:23
        while len(مكدس) > 0 and ارتفاعات[مكدس[len(مكدس) - 1]] > حالي:
            # apl-source:24
            ارتفاع = ارتفاعات[مكدس.pop()]
            # apl-source:25
            عرض = i
            # apl-source:26
            if len(مكدس) > 0:
                # apl-source:27
                عرض = i - مكدس[len(مكدس) - 1] - 1
            # apl-source:28
            if ارتفاع * عرض > أقصى:
                # apl-source:29
                أقصى = ارتفاع * عرض
        # apl-source:30
        مكدس.append(i)
    # apl-source:31
    return أقصى
# apl-source:32

# apl-source:33
تأكد_يساوي(أكبر_مستطيل([2, 1, 5, 6, 2, 3]), 10, "الكلاسيكي")
# apl-source:34
تأكد_يساوي(أكبر_مستطيل([2, 4]), 4, "شريطتان")
# apl-source:35
