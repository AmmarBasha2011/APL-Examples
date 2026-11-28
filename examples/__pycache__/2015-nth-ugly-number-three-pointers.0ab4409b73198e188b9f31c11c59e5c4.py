
# apl-source:1
# مثال 2015 — العدد القبيح رقم ن
# apl-source:2
# Nth ugly number
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2015-nth-ugly-number-three-pointers.apl
# apl-source:6

# apl-source:7
# # ثلاثة مؤشرات للضرب في 2 و3 و5
# apl-source:8
# # نأخذ الأصغر في كل مرة
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
def قبيح(ن):
  # apl-source:19
  ق = [1]
  # apl-source:20
  ا = 0
  # apl-source:21
  ب = 0
  # apl-source:22
  ج = 0
  # apl-source:23
  while len(ق) < ن:
    # apl-source:24
    ت = min(ق[ا] * 2, ق[ب] * 3, ق[ج] * 5)
    # apl-source:25
    ق = ق + [ت]
    # apl-source:26
    if ت == ق[ا] * 2:
      # apl-source:27
      ا = ا + 1
    # apl-source:28
    if ت == ق[ب] * 3:
      # apl-source:29
      ب = ب + 1
    # apl-source:30
    if ت == ق[ج] * 5:
      # apl-source:31
      ج = ج + 1
  # apl-source:32
  return ق[ن - 1]
# apl-source:33

# apl-source:34
تأكد_يساوي(قبيح(1), 1, "الأول")
# apl-source:35
تأكد_يساوي(قبيح(10), 12, "العاشر")
# apl-source:36
تأكد_يساوي(قبيح(15), 24, "الخامس عشر")
# apl-source:37
