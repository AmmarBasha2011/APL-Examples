
# apl-source:1
# مثال 556 — جذر نيوتن-رافسون
# apl-source:2
# Newton-Raphson square root
# apl-source:3
# Demonstrates: نيوتن، جذر تربيعي، تقارب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/556-newton-sqrt.apl
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
# الجذر التربيعي بطريقة نيوتن-رافسون
# apl-source:15
def جذر_نيوتن(س, تكرارات):
    # apl-source:16
    if س == 0:
        # apl-source:17
        return 0
    # apl-source:18
    تخمين = س / 2
    # apl-source:19
    for i in range(تكرارات):
        # apl-source:20
        تخمين = (تخمين + س / تخمين) / 2
    # apl-source:21
    return تخمين
# apl-source:22

# apl-source:23
ن2 = جذر_نيوتن(2, 12)
# apl-source:24
print("جذر 2:", ن2)
# apl-source:25
تأكد_يساوي(round(ن2, 10), round(1.4142135623730951, 10), "جذر 2 بدقة")
# apl-source:26
تأكد_يساوي(round(جذر_نيوتن(144, 12), 6), 12, "جذر 144")
# apl-source:27
تأكد_يساوي(جذر_نيوتن(0, 5), 0, "جذر صفر")
# apl-source:28
