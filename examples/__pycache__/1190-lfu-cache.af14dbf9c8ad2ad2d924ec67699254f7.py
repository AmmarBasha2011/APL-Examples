
# apl-source:1
# مثال 1190 — ذاكرة الأقل استخداماً
# apl-source:2
# LFU cache
# apl-source:3
# Demonstrates: عدّاد تكرار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1190-lfu-cache.apl
# apl-source:6

# apl-source:7
# نعد استخدام كل مفتاح
# apl-source:8
# وعند الامتلاء نطرد الأقل عدداً والأقدم عند التعادل
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
class ذاكرة_تكرار:
  # apl-source:19
  def __init__(ذات, سعة):
    # apl-source:20
    ذات.سعة = سعة
    # apl-source:21
    ذات.قيم = {}
    # apl-source:22
    ذات.عدادات = {}
    # apl-source:23
    ذات.اخر = {}
    # apl-source:24
    ذات.ساعة = 0
# apl-source:25

  # apl-source:26
  def قرأ(ذات, م):
    # apl-source:27
    if م not in ذات.قيم:
      # apl-source:28
      return -1
    # apl-source:29
    ذات.ساعة = ذات.ساعة + 1
    # apl-source:30
    ذات.عدادات[م] = ذات.عدادات[م] + 1
    # apl-source:31
    ذات.اخر[م] = ذات.ساعة
    # apl-source:32
    return ذات.قيم[م]
# apl-source:33

  # apl-source:34
  def ضع(ذات, م, ق):
    # apl-source:35
    if ذات.سعة == 0:
      # apl-source:36
      return 0
    # apl-source:37
    ذات.ساعة = ذات.ساعة + 1
    # apl-source:38
    if م in ذات.قيم:
      # apl-source:39
      ذات.قيم[م] = ق
      # apl-source:40
      ذات.عدادات[م] = ذات.عدادات[م] + 1
      # apl-source:41
      ذات.اخر[م] = ذات.ساعة
      # apl-source:42
      return 0
    # apl-source:43
    if len(ذات.قيم) >= ذات.سعة:
      # apl-source:44
      ضحية = ""
      # apl-source:45
      افضل = []
      # apl-source:46
      for ك in ذات.قيم:
        # apl-source:47
        مرشح = [ذات.عدادات[ك], ذات.اخر[ك], ك]
        # apl-source:48
        if (len(افضل) == 0) or (مرشح < افضل):
          # apl-source:49
          افضل = مرشح
      # apl-source:50
      ضحية = افضل[2]
      # apl-source:51
      ذات.قيم.pop(ضحية)
      # apl-source:52
      ذات.عدادات.pop(ضحية)
      # apl-source:53
      ذات.اخر.pop(ضحية)
    # apl-source:54
    ذات.قيم[م] = ق
    # apl-source:55
    ذات.عدادات[م] = 1
    # apl-source:56
    ذات.اخر[م] = ذات.ساعة
    # apl-source:57
    return 0
# apl-source:58

# apl-source:59
ذ = ذاكرة_تكرار(2)
# apl-source:60
ذ.ضع(1, 1)
# apl-source:61
ذ.ضع(2, 2)
# apl-source:62
تأكد_يساوي(ذ.قرأ(1), 1, "قراءة")
# apl-source:63
ذ.ضع(3, 3)
# apl-source:64
تأكد_يساوي(ذ.قرأ(2), -1, "طُرد الأقل")
# apl-source:65
تأكد_يساوي(ذ.قرأ(3), 3, "موجود")
# apl-source:66
ذ.ضع(4, 4)
# apl-source:67
تأكد_يساوي(ذ.قرأ(1), -1, "طُرد الأقدم")
# apl-source:68
تأكد_يساوي(ذ.قرأ(3), 3, "ثلاثة باقٍ")
# apl-source:69
تأكد_يساوي(ذ.قرأ(4), 4, "أربعة")
# apl-source:70
