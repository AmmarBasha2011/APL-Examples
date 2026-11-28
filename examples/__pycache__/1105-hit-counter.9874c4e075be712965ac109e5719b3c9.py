
# apl-source:1
# مثال 1105 — عداد الزيارات
# apl-source:2
# Hit counter over five minutes
# apl-source:3
# Demonstrates: نافذة زمنية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1105-hit-counter.apl
# apl-source:6

# apl-source:7
# نسجل وقت كل زيارة
# apl-source:8
# ونعد منها ما حدث خلال آخر 300 ثانية من وقت الاستعلام
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
class عداد_زيارات:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.ازمنة = []
# apl-source:21

    # apl-source:22
    def زيارة(ذات, ث):
        # apl-source:23
        ذات.ازمنة = ذات.ازمنة + [ث]
# apl-source:24

    # apl-source:25
    def زيارات(ذات, ث):
        # apl-source:26
        ن = 0
        # apl-source:27
        for ز in ذات.ازمنة:
            # apl-source:28
            if ز > (ث - 300):
                # apl-source:29
                ن = ن + 1
        # apl-source:30
        return ن
# apl-source:31

# apl-source:32
ع = عداد_زيارات()
# apl-source:33
ع.زيارة(1)
# apl-source:34
ع.زيارة(2)
# apl-source:35
ع.زيارة(3)
# apl-source:36
تأكد_يساوي(ع.زيارات(4), 3, "ثلاث زيارات")
# apl-source:37
ع.زيارة(300)
# apl-source:38
تأكد_يساوي(ع.زيارات(300), 4, "عند 300")
# apl-source:39
تأكد_يساوي(ع.زيارات(301), 3, "بعد 301 تسقط الأولى")
# apl-source:40
