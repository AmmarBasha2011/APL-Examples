
# apl-source:1
# مثال 3413 — صف جدول ضرب 19
# apl-source:2
# Multiplication row of 19
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3413-multiplication-table-row-of-19.apl
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
    ر = ر + [ي * 19]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), [19], "حالة 1")
# apl-source:25
تأكد_يساوي(ف(5), [19, 38, 57, 76, 95], "حالة 2")
# apl-source:26
تأكد_يساوي(ف(10), [19, 38, 57, 76, 95, 114, 133, 152, 171, 190], "حالة 3")
# apl-source:27
