
# apl-source:1
# مثال 567 — مقارنة semver
# apl-source:2
# Semver comparison
# apl-source:3
# Demonstrates: semver، إصدارات، مقارنة رقمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/567-semver-compare.apl
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
# مقارنة إصدارات دلالية semver
# apl-source:15
def قارن(أ, ب):
    # apl-source:16
    أجزاء_أ = [int(ج) for ج in أ.split(".")]
    # apl-source:17
    أجزاء_ب = [int(ج) for ج in ب.split(".")]
    # apl-source:18
    for i in range(3):
        # apl-source:19
        if أجزاء_أ[i] > أجزاء_ب[i]:
            # apl-source:20
            return 1
        # apl-source:21
        if أجزاء_أ[i] < أجزاء_ب[i]:
            # apl-source:22
            return -1
    # apl-source:23
    return 0
# apl-source:24

# apl-source:25
تأكد_يساوي(قارن("1.10.2", "1.9.9"), 1, "1.10.2 أحدث")
# apl-source:26
تأكد_يساوي(قارن("2.0.0", "10.0.0"), -1, "2 أقدم من 10")
# apl-source:27
تأكد_يساوي(قارن("3.4.5", "3.4.5"), 0, "متساويان")
# apl-source:28
تأكد_يساوي(قارن("1.0.1", "1.0.0"), 1, "تصحيح أحدث")
# apl-source:29
