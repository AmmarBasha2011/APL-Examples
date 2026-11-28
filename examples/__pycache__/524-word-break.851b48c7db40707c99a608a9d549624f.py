
# apl-source:1
# مثال 524 — تقطيع الكلمات
# apl-source:2
# Word break DP
# apl-source:3
# Demonstrates: برمجة ديناميكية، تقطيع كلمات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/524-word-break.apl
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
# تقطيع جملة إلى كلمات قاموس (برمجة ديناميكية)
# apl-source:15
def قابل_للتقطيع(نص, قاموس_كلمات):
    # apl-source:16
    ممكن = [True]
    # apl-source:17
    for i in range(1, len(نص) + 1):
        # apl-source:18
        ممكن.append(False)
    # apl-source:19
    for i in range(1, len(نص) + 1):
        # apl-source:20
        for كلمة in قاموس_كلمات:
            # apl-source:21
            ط = len(كلمة)
            # apl-source:22
            if i >= ط and ممكن[i - ط] and نص[i - ط:i] == كلمة:
                # apl-source:23
                ممكن[i] = True
    # apl-source:24
    return ممكن[len(نص)]
# apl-source:25

# apl-source:26
قاموس_كلمات = ["cat", "cats", "and", "sand", "dog"]
# apl-source:27
تأكد_يساوي(قابل_للتقطيع("catsanddog", قاموس_كلمات), True, "قابل")
# apl-source:28
تأكد_يساوي(قابل_للتقطيع("catsandog", قاموس_كلمات), False, "غير قابل")
# apl-source:29
