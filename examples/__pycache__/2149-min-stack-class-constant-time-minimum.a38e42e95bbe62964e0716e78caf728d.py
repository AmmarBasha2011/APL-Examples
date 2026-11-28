
# apl-source:1
# مثال 2149 — مكدس يعرف أصغر عنصر فيه
# apl-source:2
# Min stack class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2149-min-stack-class-constant-time-minimum.apl
# apl-source:6

# apl-source:7
# # كل دفع يحدث الأصغر عند الحاجة
# apl-source:8
# # والسحب يحدثه عند الإزالة
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
class مكدس_ادنى:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.عناصر = []
        # apl-source:21
        ذات.ادنى = []
# apl-source:22

    # apl-source:23
    def ادفع(ذات, ع):
        # apl-source:24
        ذات.عناصر = ذات.عناصر + [ع]
        # apl-source:25
        if len(ذات.ادنى) == 0 or ع <= ذات.ادنى[len(ذات.ادنى) - 1]:
            # apl-source:26
            ذات.ادنى = ذات.ادنى + [ع]
# apl-source:27

    # apl-source:28
    def اسحب(ذات):
        # apl-source:29
        ع = ذات.عناصر.pop()
        # apl-source:30
        if ع == ذات.ادنى[len(ذات.ادنى) - 1]:
            # apl-source:31
            ذات.ادنى.pop()
        # apl-source:32
        return ع
# apl-source:33

    # apl-source:34
    def اقل(ذات):
        # apl-source:35
        return ذات.ادنى[len(ذات.ادنى) - 1]
# apl-source:36

# apl-source:37
م = مكدس_ادنى()
# apl-source:38
م.ادفع(5)
# apl-source:39
م.ادفع(3)
# apl-source:40
م.ادفع(7)
# apl-source:41
م.ادفع(3)
# apl-source:42
تأكد_يساوي(م.اقل(), 3, "الأصغر ٣")
# apl-source:43
تأكد_يساوي(م.اسحب(), 3, "سحب ٣")
# apl-source:44
تأكد_يساوي(م.اقل(), 3, "ما زال ٣")
# apl-source:45
تأكد_يساوي(م.اسحب(), 7, "سحب ٧")
# apl-source:46
تأكد_يساوي(م.اسحب(), 3, "سحب ٣ ثانية")
# apl-source:47
تأكد_يساوي(م.اقل(), 5, "الأصغر ٥")
# apl-source:48
