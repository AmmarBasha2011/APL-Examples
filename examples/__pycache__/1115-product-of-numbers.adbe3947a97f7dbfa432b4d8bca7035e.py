
# apl-source:1
# مثال 1115 — حاصل ضرب آخر الأعداد
# apl-source:2
# Product of the last K numbers
# apl-source:3
# Demonstrates: ضرب تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1115-product-of-numbers.apl
# apl-source:6

# apl-source:7
# نحفظ حاصل الضرب التراكمي ونعيد البناء عند الصفر
# apl-source:8
# وحاصل الآخر ك قسمة تراكميين
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
class حاصل_ضرب:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.تراكمي = [1]
# apl-source:21

    # apl-source:22
    def اضف_عدد(ذات, س):
        # apl-source:23
        if س == 0:
            # apl-source:24
            ذات.تراكمي = [1]
        # apl-source:25
        else:
            # apl-source:26
            ذات.تراكمي = ذات.تراكمي + [ذات.تراكمي[-1] * س]
# apl-source:27

    # apl-source:28
    def اخر(ذات, ك):
        # apl-source:29
        if ك >= len(ذات.تراكمي):
            # apl-source:30
            return 0
        # apl-source:31
        return ذات.تراكمي[-1] // ذات.تراكمي[-1 - ك]
# apl-source:32

# apl-source:33
ح = حاصل_ضرب()
# apl-source:34
for س in [3, 0, 2, 5, 4]:
    # apl-source:35
    ح.اضف_عدد(س)
# apl-source:36
تأكد_يساوي(ح.اخر(2), 20, "آخر اثنين")
# apl-source:37
تأكد_يساوي(ح.اخر(3), 40, "آخر ثلاثة")
# apl-source:38
تأكد_يساوي(ح.اخر(4), 0, "يشمل الصفر")
# apl-source:39
ح.اضف_عدد(8)
# apl-source:40
تأكد_يساوي(ح.اخر(2), 32, "بعد إضافة 8")
# apl-source:41
