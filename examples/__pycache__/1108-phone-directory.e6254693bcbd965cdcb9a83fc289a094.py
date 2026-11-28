
# apl-source:1
# مثال 1108 — دليل أرقام الهاتف
# apl-source:2
# Phone directory
# apl-source:3
# Demonstrates: قائمة الأرقام الحرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1108-phone-directory.apl
# apl-source:6

# apl-source:7
# قائمة بالأرقام المتاحة نأخذ منها أول رقم
# apl-source:8
# ونعيد الرقم المحرر لنهاية القائمة
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
class دليل:
    # apl-source:19
    def __init__(ذات, سعة):
        # apl-source:20
        ذات.حرة = list(range(سعة))
# apl-source:21

    # apl-source:22
    def هات(ذات):
        # apl-source:23
        if len(ذات.حرة) == 0:
            # apl-source:24
            return -1
        # apl-source:25
        return ذات.حرة.pop(0)
# apl-source:26

    # apl-source:27
    def متاح(ذات, رقم):
        # apl-source:28
        return رقم in ذات.حرة
# apl-source:29

    # apl-source:30
    def حرر(ذات, رقم):
        # apl-source:31
        if رقم not in ذات.حرة:
            # apl-source:32
            ذات.حرة = ذات.حرة + [رقم]
# apl-source:33

# apl-source:34
د = دليل(3)
# apl-source:35
تأكد_يساوي(د.هات(), 0, "أول رقم")
# apl-source:36
تأكد_يساوي(د.هات(), 1, "ثاني رقم")
# apl-source:37
تأكد_يساوي(د.متاح(2), True, "2 متاح")
# apl-source:38
تأكد_يساوي(د.هات(), 2, "ثالث رقم")
# apl-source:39
تأكد_يساوي(د.متاح(2), False, "2 محجوز")
# apl-source:40
تأكد_يساوي(د.هات(), -1, "نفدت الأرقام")
# apl-source:41
د.حرر(2)
# apl-source:42
تأكد_يساوي(د.متاح(2), True, "2 عاد")
# apl-source:43
