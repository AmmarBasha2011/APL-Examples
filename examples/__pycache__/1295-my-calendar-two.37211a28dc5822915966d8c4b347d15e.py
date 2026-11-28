
# apl-source:1
# مثال 1295 — تقويم بحجز مزدوج
# apl-source:2
# My calendar II double booking allowed
# apl-source:3
# Demonstrates: مجالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1295-my-calendar-two.apl
# apl-source:6

# apl-source:7
# نحتفظ بالحجوزات المفردة والتقاطعات المزدوجة
# apl-source:8
# ونرفض الحجز الذي يقطع تقاطعاً
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
class تقويم_ثان:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.مفردة = []
    # apl-source:21
    ذات.مزدوجة = []
# apl-source:22

  # apl-source:23
  def احجز(ذات, ب, ن):
    # apl-source:24
    for م in ذات.مزدوجة:
      # apl-source:25
      if (ب < م[1]) and (ن > م[0]):
        # apl-source:26
        return False
    # apl-source:27
    for م in ذات.مفردة:
      # apl-source:28
      if (ب < م[1]) and (ن > م[0]):
        # apl-source:29
        ذات.مزدوجة = ذات.مزدوجة + [[max(ب, م[0]), min(ن, م[1])]]
    # apl-source:30
    ذات.مفردة = ذات.مفردة + [[ب, ن]]
    # apl-source:31
    return True
# apl-source:32

# apl-source:33
ت = تقويم_ثان()
# apl-source:34
تأكد_يساوي(ت.احجز(10, 20), True, "أول")
# apl-source:35
تأكد_يساوي(ت.احجز(50, 60), True, "ثان")
# apl-source:36
تأكد_يساوي(ت.احجز(10, 40), True, "مزدوج")
# apl-source:37
تأكد_يساوي(ت.احجز(5, 15), False, "ثلاثي")
# apl-source:38
تأكد_يساوي(ت.احجز(5, 10), True, "قبل")
# apl-source:39
تأكد_يساوي(ت.احجز(25, 55), True, "مزدوج آخر")
# apl-source:40
