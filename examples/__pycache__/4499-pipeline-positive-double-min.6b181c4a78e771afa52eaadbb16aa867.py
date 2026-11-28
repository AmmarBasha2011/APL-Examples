
# apl-source:1
# مثال 4499 — أصغر نتيجة ضعفها للأعداد الموجبة
# apl-source:2
# Smallest (or 0) of double over the positive numbers
# apl-source:3
# Demonstrates: قوائم وتصفية وتحويل وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4499-pipeline-positive-double-min.apl
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
    if خ > 0:
      # apl-source:22
      ن = ن + [خ * 2]
  # apl-source:23
  if len(ن) == 0:
    # apl-source:24
    return 0
  # apl-source:25
  return min(ن)
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([30, 17, 8, -9, 5, 12, 6]), 10, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([3, 1, 2, 8, 5]), 2, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([7, 14, 21, 28, 35, 42]), 14, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([1, 1, 2, 3, 5, 8, 13]), 2, "حالة 4")
# apl-source:31
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:32
