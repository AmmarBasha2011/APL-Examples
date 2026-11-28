
# apl-source:1
# مثال 518 — شجرة المقاطع
# apl-source:2
# Segment tree
# apl-source:3
# Demonstrates: شجرة مقاطع، استعلام مجال، تحديث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/518-segment-tree.apl
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
# شجرة المقاطع لمجاميع المجالات مع تحديث
# apl-source:15
مصدر = [1, 3, 5, 7, 9, 11]
# apl-source:16
ن = len(مصدر)
# apl-source:17
شجرة = [0] * 24
# apl-source:18

# apl-source:19
def ابن(عقدة, ب, ن):
    # apl-source:20
    if ب == ن:
        # apl-source:21
        شجرة[عقدة] = مصدر[ب]
        # apl-source:22
        return
    # apl-source:23
    وسط = (ب + ن) // 2
    # apl-source:24
    ابن(عقدة * 2, ب, وسط)
    # apl-source:25
    ابن(عقدة * 2 + 1, وسط + 1, ن)
    # apl-source:26
    شجرة[عقدة] = شجرة[عقدة * 2] + شجرة[عقدة * 2 + 1]
# apl-source:27

# apl-source:28
def استعلم(عقدة, ب, ن, من, الى):
    # apl-source:29
    if من > ن or الى < ب:
        # apl-source:30
        return 0
    # apl-source:31
    if من <= ب and ن <= الى:
        # apl-source:32
        return شجرة[عقدة]
    # apl-source:33
    وسط = (ب + ن) // 2
    # apl-source:34
    return استعلم(عقدة * 2, ب, وسط, من, الى) + استعلم(عقدة * 2 + 1, وسط + 1, ن, من, الى)
# apl-source:35

# apl-source:36
def حدث(عقدة, ب, ن, موضع, قيمة):
    # apl-source:37
    if ب == ن:
        # apl-source:38
        شجرة[عقدة] = قيمة
        # apl-source:39
        return
    # apl-source:40
    وسط = (ب + ن) // 2
    # apl-source:41
    if موضع <= وسط:
        # apl-source:42
        حدث(عقدة * 2, ب, وسط, موضع, قيمة)
    # apl-source:43
    else:
        # apl-source:44
        حدث(عقدة * 2 + 1, وسط + 1, ن, موضع, قيمة)
    # apl-source:45
    شجرة[عقدة] = شجرة[عقدة * 2] + شجرة[عقدة * 2 + 1]
# apl-source:46

# apl-source:47
ابن(1, 0, ن - 1)
# apl-source:48
تأكد_يساوي(استعلم(1, 0, ن - 1, 1, 3), 15, "مجموع [1..3]")
# apl-source:49
تأكد_يساوي(استعلم(1, 0, ن - 1, 0, 5), 36, "المجموع الكلي")
# apl-source:50
حدث(1, 0, ن - 1, 2, 10)
# apl-source:51
تأكد_يساوي(استعلم(1, 0, ن - 1, 1, 3), 20, "بعد التحديث")
# apl-source:52
