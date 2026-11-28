
# apl-source:1
# مثال 2117 — أولي صوفي جيرمان
# apl-source:2
# Sophie Germain prime v2
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2117-sophie-germain-prime-double-plus-one.apl
# apl-source:6

# apl-source:7
# # نختبر العددين
# apl-source:8
# # 11 مثال لأن 23 أولي
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  د = 2
  # apl-source:22
  while د * د <= ن:
    # apl-source:23
    if ن % د == 0:
      # apl-source:24
      return False
    # apl-source:25
    د = د + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def صوفي(ن):
  # apl-source:29
  return اولي(ن) and اولي(2 * ن + 1)
# apl-source:30

# apl-source:31
تأكد_يساوي(صوفي(2), True, "٢")
# apl-source:32
تأكد_يساوي(صوفي(3), True, "٣")
# apl-source:33
تأكد_يساوي(صوفي(5), True, "٥")
# apl-source:34
تأكد_يساوي(صوفي(7), False, "٧")
# apl-source:35
تأكد_يساوي(صوفي(11), True, "١١")
# apl-source:36
تأكد_يساوي(صوفي(13), False, "١٣")
# apl-source:37
