
# apl-source:1
# مثال 558 — الحذف الجاوسي
# apl-source:2
# Gaussian elimination
# apl-source:3
# Demonstrates: جاوس، نظام خطي، تعويض خلفي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/558-gaussian-elimination.apl
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
# حذف جاوس لحل نظام معادلات خطية
# apl-source:15
def حل_نظام(مصفوفة, ثوابت):
    # apl-source:16
    ن = len(ثوابت)
    # apl-source:17
    for عمود in range(ن):
        # apl-source:18
        أقصى_صف = عمود
        # apl-source:19
        for صف in range(عمود + 1, ن):
            # apl-source:20
            if abs(مصفوفة[صف][عمود]) > abs(مصفوفة[أقصى_صف][عمود]):
                # apl-source:21
                أقصى_صف = صف
        # apl-source:22
        مؤقت = مصفوفة[عمود]
        # apl-source:23
        مصفوفة[عمود] = مصفوفة[أقصى_صف]
        # apl-source:24
        مصفوفة[أقصى_صف] = مؤقت
        # apl-source:25
        ع = ثوابت[عمود]
        # apl-source:26
        ثوابت[عمود] = ثوابت[أقصى_صف]
        # apl-source:27
        ثوابت[أقصى_صف] = ع
        # apl-source:28
        for صف in range(عمود + 1, ن):
            # apl-source:29
            عامل = مصفوفة[صف][عمود] / مصفوفة[عمود][عمود]
            # apl-source:30
            for ك in range(عمود, ن):
                # apl-source:31
                مصفوفة[صف][ك] = مصفوفة[صف][ك] - عامل * مصفوفة[عمود][ك]
            # apl-source:32
            ثوابت[صف] = ثوابت[صف] - عامل * ثوابت[عمود]
    # apl-source:33
    حل = [0] * ن
    # apl-source:34
    for i in range(ن - 1, -1, -1):
        # apl-source:35
        م = ثوابت[i]
        # apl-source:36
        for ك in range(i + 1, ن):
            # apl-source:37
            م = م - مصفوفة[i][ك] * حل[ك]
        # apl-source:38
        حل[i] = م / مصفوفة[i][i]
    # apl-source:39
    return حل
# apl-source:40

# apl-source:41
حل = حل_نظام([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3])
# apl-source:42
print("الحل:", حل)
# apl-source:43
تأكد_يساوي(round(حل[0], 9), 2, "س")
# apl-source:44
تأكد_يساوي(round(حل[1], 9), 3, "ص")
# apl-source:45
تأكد_يساوي(round(حل[2], 9), -1, "ع")
# apl-source:46
