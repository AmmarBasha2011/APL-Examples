
# apl-source:1
# مثال 810 — ألوان ANSI
# apl-source:2
# ANSI colors
# apl-source:3
# Demonstrates: محرف هروب، SGR، مؤشر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/810-ansi-color.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# تسلسلات ANSI للطرفية: ألوان وأنماط وتحريك المؤشر
# apl-source:25
# Demonstrates: محرف الهروب 27, رموز SGR المركبة, أوامر المؤشر
# apl-source:26

# apl-source:27
هروب = chr(27)
# apl-source:28

# apl-source:29
def نمط(رموز):
  # apl-source:30
  أجزاء = []
  # apl-source:31
  for رمز in رموز:
    # apl-source:32
    أجزاء.append(str(رمز))
  # apl-source:33
  return هروب + "[" + ";".join(أجزاء) + "m"
# apl-source:34

# apl-source:35
def ملون(نص, لون):
  # apl-source:36
  return نمط([لون]) + نص + نمط([0])
# apl-source:37

# apl-source:38
def مؤشر_أعلى(عدد):
  # apl-source:39
  return هروب + "[" + str(عدد) + "A"
# apl-source:40

# apl-source:41
تأكد_يساوي(نمط([31]), هروب + "[31m", "أحمر")
# apl-source:42
تأكد_يساوي(نمط([1, 34]), هروب + "[1;34m", "أزرق غامق")
# apl-source:43
تأكد_يساوي(نمط([0]), هروب + "[0m", "إعادة ضبط")
# apl-source:44
تأكد_يساوي(ملون("خطر", 31), هروب + "[31mخطر" + هروب + "[0m", "نص ملون")
# apl-source:45
تأكد_يساوي(مؤشر_أعلى(3), هروب + "[3A", "مؤشر أعلى ثلاثة")
# apl-source:46
تأكد_يساوي(هروب + "[2J", chr(27) + "[2J", "مسح الشاشة")
# apl-source:47
تأكد_يساوي(len(ملون("س", 32)), len("س") + 9, "طول مع الغلاف")
# apl-source:48
