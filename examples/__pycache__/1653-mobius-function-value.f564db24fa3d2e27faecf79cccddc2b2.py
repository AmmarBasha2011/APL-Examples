
# apl-source:1
# مثال 1653 — دالة موبيوس
# apl-source:2
# Mobius function
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1653-mobius-function-value.apl
# apl-source:6

# apl-source:7
# نحلل العدد إلى عوامل أولية
# apl-source:8
# مربع عامل يعطي صفراً والعدد الزوجي يعطي واحداً
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
def موبيوس(ن):
  # apl-source:19
  عوامل = 0
  # apl-source:20
  ك = 2
  # apl-source:21
  while ك * ك <= ن:
    # apl-source:22
    if ن % ك == 0:
      # apl-source:23
      ن = ن // ك
      # apl-source:24
      if ن % ك == 0:
        # apl-source:25
        return 0
      # apl-source:26
      عوامل = عوامل + 1
    # apl-source:27
    ك = ك + 1
  # apl-source:28
  if ن > 1:
    # apl-source:29
    عوامل = عوامل + 1
  # apl-source:30
  if عوامل % 2 == 0:
    # apl-source:31
    return 1
  # apl-source:32
  return -1
# apl-source:33

# apl-source:34
تأكد_يساوي(موبيوس(1), 1, "واحد")
# apl-source:35
تأكد_يساوي(موبيوس(6), 1, "عاملان")
# apl-source:36
تأكد_يساوي(موبيوس(30), -1, "ثلاثة عوامل")
# apl-source:37
تأكد_يساوي(موبيوس(12), 0, "مربع")
# apl-source:38
