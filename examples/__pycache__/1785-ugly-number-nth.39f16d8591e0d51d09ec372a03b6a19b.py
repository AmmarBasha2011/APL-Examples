
# apl-source:1
# مثال 1785 — العدد القبيح رقم ن
# apl-source:2
# Nth ugly number
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1785-ugly-number-nth.apl
# apl-source:6

# apl-source:7
# ثلاثة مؤشرات للمضاعفات
# apl-source:8
# نأخذ الأصغر في كل خطوة
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
  أعداد = [1]
  # apl-source:20
  أ = 0
  # apl-source:21
  ب = 0
  # apl-source:22
  ج = 0
  # apl-source:23
  while len(أعداد) < ن:
    # apl-source:24
    ت = min(min(أعداد[أ] * 2, أعداد[ب] * 3), أعداد[ج] * 5)
    # apl-source:25
    أعداد.append(ت)
    # apl-source:26
    if أعداد[أ] * 2 == ت:
      # apl-source:27
      أ = أ + 1
    # apl-source:28
    if أعداد[ب] * 3 == ت:
      # apl-source:29
      ب = ب + 1
    # apl-source:30
    if أعداد[ج] * 5 == ت:
      # apl-source:31
      ج = ج + 1
  # apl-source:32
  return أعداد[ن - 1]
# apl-source:33

# apl-source:34
تأكد_يساوي(قبيح(1), 1, "الأول")
# apl-source:35
تأكد_يساوي(قبيح(10), 12, "العاشر")
# apl-source:36
تأكد_يساوي(قبيح(15), 24, "الخامس عشر")
# apl-source:37
