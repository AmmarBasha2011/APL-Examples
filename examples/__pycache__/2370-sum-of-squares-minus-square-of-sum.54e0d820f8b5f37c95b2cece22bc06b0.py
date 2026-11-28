
# apl-source:1
# مثال 2370 — فرق مجموع المربعات ومربع المجموع
# apl-source:2
# Square of sum minus sum of squares
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2370-sum-of-squares-minus-square-of-sum.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  أ = 0
  # apl-source:20
  ب = 0
  # apl-source:21
  for ي in range(1, ن + 1):
    # apl-source:22
    أ = أ + ي
    # apl-source:23
    ب = ب + ي * ي
  # apl-source:24
  return أ * أ - ب
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(1), 0, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(3), 22, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(10), 2640, "حالة 3")
# apl-source:29
تأكد_يساوي(ف(100), 25164150, "حالة 4")
# apl-source:30
