
# apl-source:1
# مثال 582 — تدوير مصفوفة
# apl-source:2
# Rotate matrix
# apl-source:3
# Demonstrates: تدوير 90، تبديل، طبقات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/582-rotate-matrix.apl
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
# تدوير مصفوفة 90 درجة في المكان (تبديل ثم عكس)
# apl-source:15
def دوّر(مصفوفة):
    # apl-source:16
    ن = len(مصفوفة)
    # apl-source:17
    for i in range(ن):
        # apl-source:18
        for j in range(i + 1, ن):
            # apl-source:19
            م = مصفوفة[i][j]
            # apl-source:20
            مصفوفة[i][j] = مصفوفة[j][i]
            # apl-source:21
            مصفوفة[j][i] = م
    # apl-source:22
    for i in range(ن):
        # apl-source:23
        مصفوفة[i] = مصفوفة[i][::-1]
    # apl-source:24
    return مصفوفة
# apl-source:25

# apl-source:26
تأكد_يساوي(دوّر([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "تدوير 3×3")
# apl-source:27
تأكد_يساوي(دوّر([[1, 2], [3, 4]]), [[3, 1], [4, 2]], "تدوير 2×2")
# apl-source:28
