
# apl-source:1
# مثال 2046 — هل العدد قوة للأساس
# apl-source:2
# Power of base check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2046-power-of-base-check-by-division.apl
# apl-source:6

# apl-source:7
# # القوة تنتهي إلى 1 بعد القسمة المتكررة
# apl-source:8
# # الأعداد غير الموجبة مرفوضة
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
def قوة(ن, ا):
  # apl-source:19
  if ن < 1:
    # apl-source:20
    return False
  # apl-source:21
  while ن % ا == 0:
    # apl-source:22
    ن = ن // ا
  # apl-source:23
  return ن == 1
# apl-source:24

# apl-source:25
تأكد_يساوي(قوة(27, 3), True, "٢٧")
# apl-source:26
تأكد_يساوي(قوة(45, 3), False, "٤٥")
# apl-source:27
تأكد_يساوي(قوة(64, 4), True, "٦٤")
# apl-source:28
تأكد_يساوي(قوة(8, 4), False, "٨")
# apl-source:29
تأكد_يساوي(قوة(1, 5), True, "١")
# apl-source:30
تأكد_يساوي(قوة(0, 2), False, "صفر")
# apl-source:31
