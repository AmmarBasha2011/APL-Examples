
# apl-source:1
# مثال 1229 — عدد قبيح
# apl-source:2
# Nth ugly number
# apl-source:3
# Demonstrates: ثلاثة مؤشرات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1229-ugly-number-two.apl
# apl-source:6

# apl-source:7
# الأعداد القبيحة عواملها 2 و3 و5 فقط
# apl-source:8
# ننتجها بالترتيب بثلاثة مؤشرات
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
  أ = [1]
  # apl-source:20
  ي2 = 0
  # apl-source:21
  ي3 = 0
  # apl-source:22
  ي5 = 0
  # apl-source:23
  while len(أ) < ن:
    # apl-source:24
    ب2 = أ[ي2] * 2
    # apl-source:25
    ب3 = أ[ي3] * 3
    # apl-source:26
    ب5 = أ[ي5] * 5
    # apl-source:27
    ت = min(ب2, min(ب3, ب5))
    # apl-source:28
    أ = أ + [ت]
    # apl-source:29
    if ت == ب2:
      # apl-source:30
      ي2 = ي2 + 1
    # apl-source:31
    if ت == ب3:
      # apl-source:32
      ي3 = ي3 + 1
    # apl-source:33
    if ت == ب5:
      # apl-source:34
      ي5 = ي5 + 1
  # apl-source:35
  return أ[ن - 1]
# apl-source:36

# apl-source:37
تأكد_يساوي(قبيح(1), 1, "الأول")
# apl-source:38
تأكد_يساوي(قبيح(10), 12, "العاشر")
# apl-source:39
تأكد_يساوي(قبيح(15), 24, "الخامس عشر")
# apl-source:40
تأكد_يساوي(قبيح(100), 1536, "المئة")
# apl-source:41
