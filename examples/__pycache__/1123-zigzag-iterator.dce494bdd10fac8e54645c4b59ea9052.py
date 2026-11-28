
# apl-source:1
# مثال 1123 — مكرر متعرج
# apl-source:2
# Zigzag iterator
# apl-source:3
# Demonstrates: تناوب بين قائمتين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1123-zigzag-iterator.apl
# apl-source:6

# apl-source:7
# نأخذ عنصراً من القائمة الأولى ثم الثانية ثم نعود
# apl-source:8
# ولو انتهت قائمة أكملنا من الأخرى
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class متعرج:
    # apl-source:19
    def __init__(ذات, أ, ب):
        # apl-source:20
        ذات.قوائم = [أ, ب]
        # apl-source:21
        ذات.مواضع = [0, 0]
        # apl-source:22
        ذات.دور = 0
# apl-source:23

    # apl-source:24
    def لديه_تالي(ذات):
        # apl-source:25
        return (ذات.مواضع[0] < len(ذات.قوائم[0])) or (ذات.مواضع[1] < len(ذات.قوائم[1]))
# apl-source:26

    # apl-source:27
    def تالي(ذات):
        # apl-source:28
        if ذات.مواضع[ذات.دور] >= len(ذات.قوائم[ذات.دور]):
            # apl-source:29
            ذات.دور = 1 - ذات.دور
        # apl-source:30
        س = ذات.قوائم[ذات.دور][ذات.مواضع[ذات.دور]]
        # apl-source:31
        ذات.مواضع[ذات.دور] = ذات.مواضع[ذات.دور] + 1
        # apl-source:32
        ذات.دور = 1 - ذات.دور
        # apl-source:33
        return س
# apl-source:34

# apl-source:35
م = متعرج([1, 2], [3, 4, 5, 6])
# apl-source:36
ناتج = []
# apl-source:37
while م.لديه_تالي():
    # apl-source:38
    ناتج = ناتج + [م.تالي()]
# apl-source:39
تأكد_يساوي(ناتج, [1, 3, 2, 4, 5, 6], "قائمتان مختلفتا الطول")
# apl-source:40
ن = متعرج([], [7, 8])
# apl-source:41
ناتج2 = []
# apl-source:42
while ن.لديه_تالي():
    # apl-source:43
    ناتج2 = ناتج2 + [ن.تالي()]
# apl-source:44
تأكد_يساوي(ناتج2, [7, 8], "الأولى فارغة")
# apl-source:45
