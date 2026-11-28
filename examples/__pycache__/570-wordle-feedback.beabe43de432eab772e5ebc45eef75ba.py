
# apl-source:1
# مثال 570 — تقييم ووردل
# apl-source:2
# Wordle feedback
# apl-source:3
# Demonstrates: ووردل، تقييم حروف، مروران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/570-wordle-feedback.apl
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
# تقييم ووردل: أخضر/أصفر/رمادي بمرورين
# apl-source:15
def قيّم(سر, تخمين):
    # apl-source:16
    نتيجة = ["رمادي"] * 5
    # apl-source:17
    متبقي = dict()
    # apl-source:18
    for i in range(5):
        # apl-source:19
        if تخمين[i] == سر[i]:
            # apl-source:20
            نتيجة[i] = "أخضر"
        # apl-source:21
        else:
            # apl-source:22
            if سر[i] in متبقي:
                # apl-source:23
                متبقي[سر[i]] = متبقي[سر[i]] + 1
            # apl-source:24
            else:
                # apl-source:25
                متبقي[سر[i]] = 1
    # apl-source:26
    for i in range(5):
        # apl-source:27
        if نتيجة[i] == "رمادي" and تخمين[i] in متبقي and متبقي[تخمين[i]] > 0:
            # apl-source:28
            نتيجة[i] = "أصفر"
            # apl-source:29
            متبقي[تخمين[i]] = متبقي[تخمين[i]] - 1
    # apl-source:30
    return نتيجة
# apl-source:31

# apl-source:32
تأكد_يساوي(قيّم("crane", "cigar"), ["أخضر", "رمادي", "رمادي", "أصفر", "أصفر"], "cigar")
# apl-source:33
تأكد_يساوي(قيّم("crane", "crane"), ["أخضر", "أخضر", "أخضر", "أخضر", "أخضر"], "مطابقة تامة")
# apl-source:34
تأكد_يساوي(قيّم("aabbc", "bbaaa"), ["أصفر", "أصفر", "أصفر", "أصفر", "رمادي"], "تكرارات")
# apl-source:35
