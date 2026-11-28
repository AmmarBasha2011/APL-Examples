
# apl-source:1
# مثال 581 — مصفوفة حلزونية
# apl-source:2
# Spiral matrix
# apl-source:3
# Demonstrates: حلزوني، حدود، اتجاهات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/581-spiral-matrix.apl
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
# اجتياز حلزوني لمصفوفة
# apl-source:15
def حلزوني(مصفوفة):
    # apl-source:16
    نتيجة = list()
    # apl-source:17
    أعلى = 0
    # apl-source:18
    أسفل = len(مصفوفة) - 1
    # apl-source:19
    يسار = 0
    # apl-source:20
    يمين = len(مصفوفة[0]) - 1
    # apl-source:21
    while أعلى <= أسفل and يسار <= يمين:
        # apl-source:22
        for ك in range(يسار, يمين + 1):
            # apl-source:23
            نتيجة.append(مصفوفة[أعلى][ك])
        # apl-source:24
        أعلى = أعلى + 1
        # apl-source:25
        for ك in range(أعلى, أسفل + 1):
            # apl-source:26
            نتيجة.append(مصفوفة[ك][يمين])
        # apl-source:27
        يمين = يمين - 1
        # apl-source:28
        if أعلى <= أسفل:
            # apl-source:29
            for ك in range(يمين, يسار - 1, -1):
                # apl-source:30
                نتيجة.append(مصفوفة[أسفل][ك])
            # apl-source:31
            أسفل = أسفل - 1
        # apl-source:32
        if يسار <= يمين:
            # apl-source:33
            for ك in range(أسفل, أعلى - 1, -1):
                # apl-source:34
                نتيجة.append(مصفوفة[ك][يسار])
        # apl-source:35
        يسار = يسار + 1
    # apl-source:36
    return نتيجة
# apl-source:37

# apl-source:38
تأكد_يساوي(حلزوني([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5], "3×3")
# apl-source:39
تأكد_يساوي(حلزوني([[1, 2], [3, 4]]), [1, 2, 4, 3], "2×2")
# apl-source:40
