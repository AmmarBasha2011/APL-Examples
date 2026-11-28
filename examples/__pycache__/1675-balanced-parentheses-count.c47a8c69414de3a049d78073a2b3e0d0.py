
# apl-source:1
# مثال 1675 — عدد الأقواس المتوازنة
# apl-source:2
# Count balanced parentheses strings
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1675-balanced-parentheses-count.apl
# apl-source:6

# apl-source:7
# نعد المسارات بعدد المفتوح الزائد
# apl-source:8
# نستخدم جدولاً من ن والمفتوح
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
def عد_أقواس(ن):
  # apl-source:19
  حالات = [1]
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    حالات.append(0)
  # apl-source:22
  for خطوة in range(2 * ن):
    # apl-source:23
    جديد = []
    # apl-source:24
    for ك in range(ن + 1):
      # apl-source:25
      جديد.append(0)
    # apl-source:26
    for ك in range(ن + 1):
      # apl-source:27
      if حالات[ك] > 0:
        # apl-source:28
        if ك < ن:
          # apl-source:29
          جديد[ك + 1] = جديد[ك + 1] + حالات[ك]
        # apl-source:30
        if ك > 0:
          # apl-source:31
          جديد[ك - 1] = جديد[ك - 1] + حالات[ك]
    # apl-source:32
    حالات = جديد
  # apl-source:33
  return حالات[0]
# apl-source:34

# apl-source:35
تأكد_يساوي(عد_أقواس(1), 1, "زوج")
# apl-source:36
تأكد_يساوي(عد_أقواس(3), 5, "ثلاثة")
# apl-source:37
تأكد_يساوي(عد_أقواس(4), 14, "أربعة")
# apl-source:38
