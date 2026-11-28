
# apl-source:1
# مثال 4557 — عدد نتيجة ناقص 3 للأعداد الأكبر من 10
# apl-source:2
# Count of minus 3 over the greater than 10 numbers
# apl-source:3
# Demonstrates: قوائم وتصفية وتحويل وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4557-pipeline-big-minus3-count.apl
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
    if خ > 10:
      # apl-source:22
      ن = ن + [خ - 3]
  # apl-source:23
  return len(ن)
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([1, 1, 2, 3, 5, 8, 13]), 1, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([-5, 10, 25, 2, 2]), 1, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([30, 17, 8, -9, 5, 12, 6]), 3, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([20, 11, 6, 4, 3, 1]), 2, "حالة 4")
# apl-source:29
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:30
