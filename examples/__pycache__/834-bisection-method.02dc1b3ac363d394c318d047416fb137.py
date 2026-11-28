
# apl-source:1
# مثال 834 — طريقة التنصيف
# apl-source:2
# Bisection method
# apl-source:3
# Demonstrates: قيمة وسيطة، تقارب مضمون
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/834-bisection-method.apl
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
# طريقة التنصيف لإيجاد الجذور: تقييد الجذر بين علامتين متعاكستين
# apl-source:25
# Demonstrates: نظرية القيمة الوسيطة, تنصيف متكرر, تقارب مضمون
# apl-source:26

# apl-source:27
def كثيرة(س):
  # apl-source:28
  return س * س * س - س - 2
# apl-source:29

# apl-source:30
def تنصيف(أدنى, أعلى, خطوات):
  # apl-source:31
  أ = أدنى * 1.0
  # apl-source:32
  ب = أعلى * 1.0
  # apl-source:33
  for ي in range(خطوات):
    # apl-source:34
    منتصف = (أ + ب) / 2
    # apl-source:35
    if كثيرة(أ) * كثيرة(منتصف) <= 0:
      # apl-source:36
      ب = منتصف
    # apl-source:37
    else:
      # apl-source:38
      أ = منتصف
  # apl-source:39
  return (أ + ب) / 2
# apl-source:40

# apl-source:41
تأكد_يساوي(round(تنصيف(1, 2, 30), 6), 1.52138, "جذر كثيرة الحدود")
# apl-source:42
تأكد_يساوي(round(كثيرة(1.5213797), 4), 0.0, "التحقق من الجذر")
# apl-source:43
تأكد_يساوي(round(تنصيف(1, 2, 10), 4), 1.521, "عشر خطوات")
# apl-source:44
تأكد_يساوي(round(تنصيف(1, 2, 40), 8), 1.52137971, "أربعون خطوة")
# apl-source:45
