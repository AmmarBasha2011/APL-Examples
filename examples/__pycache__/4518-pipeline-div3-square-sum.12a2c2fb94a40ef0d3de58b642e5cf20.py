
# apl-source:1
# مثال 4518 — مجموع نتيجة مربعها للأعداد التقبل القسمة على 3
# apl-source:2
# Sum of square over the divisible by 3 numbers
# apl-source:3
# Demonstrates: قوائم وتصفية وتحويل وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4518-pipeline-div3-square-sum.apl
# apl-source:6

# apl-source:7
# نختار من القائمة الأعداد التي تحقق الشرط
# apl-source:8
# ثم نحوّلها ونجمع النتيجة
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
def ف(ق):
  # apl-source:19
  ن = []
  # apl-source:20
  for خ in ق:
    # apl-source:21
    if خ % 3 == 0:
      # apl-source:22
      ن = ن + [خ * خ]
  # apl-source:23
  ج = 0
  # apl-source:24
  for ي in ن:
    # apl-source:25
    ج = ج + ي
  # apl-source:26
  return ج
# apl-source:27

# apl-source:28
تأكد_يساوي(ف([9, 0, 0, 4, 16]), 81, "حالة 1")
# apl-source:29
تأكد_يساوي(ف([7, 14, 21, 28, 35, 42]), 2205, "حالة 2")
# apl-source:30
تأكد_يساوي(ف([3, 1, 2, 8, 5]), 9, "حالة 3")
# apl-source:31
تأكد_يساوي(ف([-5, 10, 25, 2, 2]), 0, "حالة 4")
# apl-source:32
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:33
