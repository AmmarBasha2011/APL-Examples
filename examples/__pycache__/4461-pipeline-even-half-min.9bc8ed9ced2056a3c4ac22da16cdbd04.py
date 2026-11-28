
# apl-source:1
# مثال 4461 — أصغر نتيجة نصفها بالقسمة الصحيحة للأعداد الزوجية
# apl-source:2
# Smallest (or 0) of integer half over the even numbers
# apl-source:3
# Demonstrates: قوائم وتصفية وتحويل وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4461-pipeline-even-half-min.apl
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
    if خ % 2 == 0:
      # apl-source:22
      ن = ن + [خ // 2]
  # apl-source:23
  if len(ن) == 0:
    # apl-source:24
    return 0
  # apl-source:25
  return min(ن)
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([20, 11, 6, 4, 3, 1]), 2, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([12, 7, 0, -4, 9, 15]), -2, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([3, 1, 2, 8, 5]), 1, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([7, 14, 21, 28, 35, 42]), 7, "حالة 4")
# apl-source:31
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:32
