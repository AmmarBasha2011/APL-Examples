
# apl-source:1
# مثال 576 — أطول سلسلة مشتركة
# apl-source:2
# Longest common substring
# apl-source:3
# Demonstrates: سلسلة مشتركة، برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/576-longest-common-substring.apl
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
# أطول سلسلة مشتركة (متصلة) — تقابل أطول تتابع مشترك
# apl-source:15
def أطول_مشتركة(أ, ب):
    # apl-source:16
    أقصى = 0
    # apl-source:17
    نهاية = 0
    # apl-source:18
    سابق = [0] * (len(ب) + 1)
    # apl-source:19
    for i in range(1, len(أ) + 1):
        # apl-source:20
        حالي = [0] * (len(ب) + 1)
        # apl-source:21
        for j in range(1, len(ب) + 1):
            # apl-source:22
            if أ[i - 1] == ب[j - 1]:
                # apl-source:23
                حالي[j] = سابق[j - 1] + 1
                # apl-source:24
                if حالي[j] > أقصى:
                    # apl-source:25
                    أقصى = حالي[j]
                    # apl-source:26
                    نهاية = i
        # apl-source:27
        سابق = حالي
    # apl-source:28
    return أ[نهاية - أقصى:نهاية]
# apl-source:29

# apl-source:30
تأكد_يساوي(أطول_مشتركة("abcdef", "zbcdf"), "bcd", "bcd المشتركة")
# apl-source:31
تأكد_يساوي(أطول_مشتركة("programming", "gram"), "gram", "gram كاملة")
# apl-source:32
تأكد_يساوي(أطول_مشتركة("abc", "xyz"), "", "لا شيء")
# apl-source:33
