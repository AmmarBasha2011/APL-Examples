
# apl-source:1
# مثال 549 — حصر مياه الأمطار
# apl-source:2
# Trapping rain water
# apl-source:3
# Demonstrates: مؤشران، حصر مياه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/549-trapping-rain-water.apl
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
# حصر مياه الأمطار بين الحواجز بمؤشرين
# apl-source:15
def مياه_محصورة(ارتفاعات):
    # apl-source:16
    يسار = 0
    # apl-source:17
    يمين = len(ارتفاعات) - 1
    # apl-source:18
    أقصى_يسار = 0
    # apl-source:19
    أقصى_يمين = 0
    # apl-source:20
    مياه = 0
    # apl-source:21
    while يسار < يمين:
        # apl-source:22
        if ارتفاعات[يسار] < ارتفاعات[يمين]:
            # apl-source:23
            if ارتفاعات[يسار] >= أقصى_يسار:
                # apl-source:24
                أقصى_يسار = ارتفاعات[يسار]
            # apl-source:25
            else:
                # apl-source:26
                مياه = مياه + أقصى_يسار - ارتفاعات[يسار]
            # apl-source:27
            يسار = يسار + 1
        # apl-source:28
        else:
            # apl-source:29
            if ارتفاعات[يمين] >= أقصى_يمين:
                # apl-source:30
                أقصى_يمين = ارتفاعات[يمين]
            # apl-source:31
            else:
                # apl-source:32
                مياه = مياه + أقصى_يمين - ارتفاعات[يمين]
            # apl-source:33
            يمين = يمين - 1
    # apl-source:34
    return مياه
# apl-source:35

# apl-source:36
تأكد_يساوي(مياه_محصورة([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6, "المثال الكلاسيكي")
# apl-source:37
تأكد_يساوي(مياه_محصورة([4, 2, 0, 3, 2, 5]), 9, "مثال ثان")
# apl-source:38
