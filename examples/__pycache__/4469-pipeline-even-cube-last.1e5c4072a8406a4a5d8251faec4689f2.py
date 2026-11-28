
# apl-source:1
# مثال 4469 — آخر نتيجة مكعبها للأعداد الزوجية
# apl-source:2
# Last (or -1) of cube over the even numbers
# apl-source:3
# Demonstrates: قوائم وتصفية وتحويل وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4469-pipeline-even-cube-last.apl
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
      ن = ن + [خ * خ * خ]
  # apl-source:23
  if len(ن) == 0:
    # apl-source:24
    return -1
  # apl-source:25
  return ن[len(ن) - 1]
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([1, 1, 2, 3, 5, 8, 13]), 512, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([3, 1, 2, 8, 5]), 512, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([9, 0, 0, 4, 16]), 4096, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([20, 11, 6, 4, 3, 1]), 64, "حالة 4")
# apl-source:31
تأكد_يساوي(ف([]), -1, "حالة 5")
# apl-source:32
