
# apl-source:1
# مثال 547 — العنصر الأكبر التالي
# apl-source:2
# Next greater element
# apl-source:3
# Demonstrates: مكدس رتيب، عنصر أكبر تالٍ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/547-next-greater-element.apl
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
# العنصر الأكبر التالي بمكدس رتيب
# apl-source:15
def الأكبر_التالي(ق):
    # apl-source:16
    نتائج = [-1] * len(ق)
    # apl-source:17
    مكدس = list()
    # apl-source:18
    for i in range(len(ق)):
        # apl-source:19
        while len(مكدس) > 0 and ق[مكدس[len(مكدس) - 1]] < ق[i]:
            # apl-source:20
            نتائج[مكدس.pop()] = ق[i]
        # apl-source:21
        مكدس.append(i)
    # apl-source:22
    return نتائج
# apl-source:23

# apl-source:24
تأكد_يساوي(الأكبر_التالي([4, 5, 2, 25]), [5, 25, 25, -1], "المثال")
# apl-source:25
تأكد_يساوي(الأكبر_التالي([13, 7, 6, 12]), [-1, 12, 12, -1], "مثال ثان")
# apl-source:26
تأكد_يساوي(الأكبر_التالي([3, 2, 1]), [-1, -1, -1], "تنازلي")
# apl-source:27
