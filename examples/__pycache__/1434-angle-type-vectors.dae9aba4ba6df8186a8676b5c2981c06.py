
# apl-source:1
# مثال 1434 — نوع الزاوية بين متجهين
# apl-source:2
# Angle type between two vectors
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1434-angle-type-vectors.apl
# apl-source:6

# apl-source:7
# نشير إلى الجداء الداخلي
# apl-source:8
# موجب حادة وصفر قائمة وسالب منفرجة
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
def نوع_الزاوية(أ, ب):
  # apl-source:19
  داخلي = أ[0] * ب[0] + أ[1] * ب[1]
  # apl-source:20
  if داخلي > 0:
    # apl-source:21
    return "حادة"
  # apl-source:22
  if داخلي == 0:
    # apl-source:23
    return "قائمة"
  # apl-source:24
  return "منفرجة"
# apl-source:25

# apl-source:26
تأكد_يساوي(نوع_الزاوية([1,0], [0,1]), "قائمة", "عمودان")
# apl-source:27
تأكد_يساوي(نوع_الزاوية([1,1], [1,0]), "حادة", "حادة")
# apl-source:28
تأكد_يساوي(نوع_الزاوية([-1,0], [1,1]), "منفرجة", "منفرجة")
# apl-source:29
