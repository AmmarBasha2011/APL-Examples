
# apl-source:1
# مثال 693 — ضوضاء بيرلين أحادية
# apl-source:2
# 1D Perlin-style value noise
# apl-source:3
# Demonstrates: هاش حتمي، smoothstep، أوكتافات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/693-perlin-noise-1d.apl
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
# ضوضاء قيم أحادية البعد بأسلوب بيرلين
# apl-source:25
# Demonstrates: هاش حتمي, تلطيف smoothstep, أوكتافات متراكبة
# apl-source:26
# لا مولد عشوائي: التجزئة تعطي نفس القيمة دائما
# apl-source:27

# apl-source:28
def هاش(ي):
  # apl-source:29
  ح = (ي * 374761393 + 668265263) % 4294967296
  # apl-source:30
  ح = (ح * 2246822519) % 4294967296
  # apl-source:31
  return (ح % 2000) / 1000.0 - 1.0
# apl-source:32

# apl-source:33
def تلطيف(ت):
  # apl-source:34
  return ت * ت * (3.0 - 2.0 * ت)
# apl-source:35

# apl-source:36
def ضوضاء(س):
  # apl-source:37
  ي = int(س)
  # apl-source:38
  ف = س - ي
  # apl-source:39
  أ = هاش(ي)
  # apl-source:40
  ب = هاش(ي + 1)
  # apl-source:41
  return أ + (ب - أ) * تلطيف(ف)
# apl-source:42

# apl-source:43
def أوكتاف(س):
  # apl-source:44
  return ضوضاء(س) * 0.75 + ضوضاء(س * 2.0) * 0.25
# apl-source:45

# apl-source:46
تأكد_يساوي(round(هاش(0), 3), -0.495, "هاش الصفر")
# apl-source:47
تأكد_يساوي(هاش(7), هاش(7), "الهاش حتمي")
# apl-source:48
تأكد_يساوي(تلطيف(0.5), 0.5, "منتصف التلطيف")
# apl-source:49
تأكد_يساوي(round(ضوضاء(2.5), 4), round(هاش(2) * 0.5 + هاش(3) * 0.5, 4), "استيفاء المنتصف")
# apl-source:50
عينة = أوكتاف(3.25)
# apl-source:51
تأكد_يساوي(عينة > -1.0 and عينة < 1.0, True, "الناتج ضمن المدى")
# apl-source:52
تأكد_يساوي(round(أوكتاف(3.25), 6), round(عينة, 6), "أوكتاف حتمي")
# apl-source:53
print("أوكتاف(3.25):", round(عينة, 4))
# apl-source:54
