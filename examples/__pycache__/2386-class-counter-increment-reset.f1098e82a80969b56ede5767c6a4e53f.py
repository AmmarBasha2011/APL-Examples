
# apl-source:1
# مثال 2386 — صنف عداد بزيادة وتصفير
# apl-source:2
# Counter class with reset
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2386-class-counter-increment-reset.apl
# apl-source:6

# apl-source:7
# # نعرف صنفا
# apl-source:8
# # ونختبر سلوكه
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
class عداد:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.ق = 0
# apl-source:21

    # apl-source:22
    def زد(ذات):
        # apl-source:23
        ذات.ق = ذات.ق + 1
# apl-source:24

    # apl-source:25
    def صفر(ذات):
        # apl-source:26
        ذات.ق = 0
# apl-source:27

# apl-source:28
ع = عداد()
# apl-source:29
ع.زد()
# apl-source:30
ع.زد()
# apl-source:31
تأكد_يساوي(ع.ق, 2, "بعد زيادتين")
# apl-source:32
ع.صفر()
# apl-source:33
تأكد_يساوي(ع.ق, 0, "بعد التصفير")
# apl-source:34
