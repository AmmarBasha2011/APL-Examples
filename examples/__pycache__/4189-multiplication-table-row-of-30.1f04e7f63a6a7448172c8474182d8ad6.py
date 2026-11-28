
# apl-source:1
# مثال 4189 — صف جدول ضرب 30
# apl-source:2
# Multiplication row of 30
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4189-multiplication-table-row-of-30.apl
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
  ر = []
  # apl-source:20
  for ي in range(1, ن + 1):
    # apl-source:21
    ر = ر + [ي * 30]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), [30], "حالة 1")
# apl-source:25
تأكد_يساوي(ف(5), [30, 60, 90, 120, 150], "حالة 2")
# apl-source:26
تأكد_يساوي(ف(10), [30, 60, 90, 120, 150, 180, 210, 240, 270, 300], "حالة 3")
# apl-source:27
