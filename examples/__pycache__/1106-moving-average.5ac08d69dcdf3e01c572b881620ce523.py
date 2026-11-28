
# apl-source:1
# مثال 1106 — المتوسط المتحرك
# apl-source:2
# Moving average from a data stream
# apl-source:3
# Demonstrates: نافذة بمجموع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1106-moving-average.apl
# apl-source:6

# apl-source:7
# نحتفظ بنافذة من آخر ك قيم ومجموعها
# apl-source:8
# القيمة الجديدة تدخل والأقدم تخرج عند الامتلاء
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
class متوسط_متحرك:
    # apl-source:19
    def __init__(ذات, حجم_نافذة):
        # apl-source:20
        ذات.حد = حجم_نافذة
        # apl-source:21
        ذات.نافذة = []
        # apl-source:22
        ذات.مجموع_ن = 0
# apl-source:23

    # apl-source:24
    def قيمة_جديدة(ذات, س):
        # apl-source:25
        ذات.نافذة = ذات.نافذة + [س]
        # apl-source:26
        ذات.مجموع_ن = ذات.مجموع_ن + س
        # apl-source:27
        if len(ذات.نافذة) > ذات.حد:
            # apl-source:28
            ذات.مجموع_ن = ذات.مجموع_ن - ذات.نافذة[0]
            # apl-source:29
            ذات.نافذة = ذات.نافذة[1:]
        # apl-source:30
        return ذات.مجموع_ن / len(ذات.نافذة)
# apl-source:31

# apl-source:32
م = متوسط_متحرك(3)
# apl-source:33
تأكد_يساوي(م.قيمة_جديدة(1), 1.0, "قيمة واحدة")
# apl-source:34
تأكد_يساوي(م.قيمة_جديدة(10), 5.5, "قيمتان")
# apl-source:35
تأكد_يساوي(round(م.قيمة_جديدة(3), 4), 4.6667, "ثلاث قيم")
# apl-source:36
تأكد_يساوي(م.قيمة_جديدة(5), 6.0, "النافذة تنزلق")
# apl-source:37
