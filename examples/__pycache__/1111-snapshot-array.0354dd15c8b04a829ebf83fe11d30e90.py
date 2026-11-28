
# apl-source:1
# مثال 1111 — مصفوفة اللقطات
# apl-source:2
# Snapshot array
# apl-source:3
# Demonstrates: تاريخ لكل فهرس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1111-snapshot-array.apl
# apl-source:6

# apl-source:7
# لكل فهرس قائمة أزواج (رقم اللقطة، القيمة)
# apl-source:8
# والقراءة تأخذ آخر قيمة رقم لقطتها لا يتجاوز المطلوب
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
class مصفوفة_لقطات:
    # apl-source:19
    def __init__(ذات, ن):
        # apl-source:20
        ذات.تاريخ = []
        # apl-source:21
        for ع in range(ن):
            # apl-source:22
            ذات.تاريخ = ذات.تاريخ + [[[0, 0]]]
        # apl-source:23
        ذات.رقم = 0
# apl-source:24

    # apl-source:25
    def ضع(ذات, فهرس, قيمة):
        # apl-source:26
        ذات.تاريخ[فهرس] = ذات.تاريخ[فهرس] + [[ذات.رقم, قيمة]]
# apl-source:27

    # apl-source:28
    def لقطة(ذات):
        # apl-source:29
        ذات.رقم = ذات.رقم + 1
        # apl-source:30
        return ذات.رقم - 1
# apl-source:31

    # apl-source:32
    def اقرأ(ذات, فهرس, رقم_لقطة):
        # apl-source:33
        نتيجة = 0
        # apl-source:34
        for زوج in ذات.تاريخ[فهرس]:
            # apl-source:35
            if زوج[0] <= رقم_لقطة:
                # apl-source:36
                نتيجة = زوج[1]
        # apl-source:37
        return نتيجة
# apl-source:38

# apl-source:39
م = مصفوفة_لقطات(3)
# apl-source:40
م.ضع(0, 5)
# apl-source:41
تأكد_يساوي(م.لقطة(), 0, "اللقطة الأولى")
# apl-source:42
م.ضع(0, 6)
# apl-source:43
تأكد_يساوي(م.اقرأ(0, 0), 5, "القيمة في اللقطة 0")
# apl-source:44
تأكد_يساوي(م.لقطة(), 1, "اللقطة الثانية")
# apl-source:45
تأكد_يساوي(م.اقرأ(0, 1), 6, "القيمة في اللقطة 1")
# apl-source:46
تأكد_يساوي(م.اقرأ(2, 1), 0, "فهرس لم يتغير")
# apl-source:47
