
# apl-source:1
# مثال 1747 — تبديل صفوف وأعمدة المصفوفة
# apl-source:2
# Transpose a rectangular matrix
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1747-matrix-transpose-rectangular.apl
# apl-source:6

# apl-source:7
# العنصر [ي][ك] ينتقل إلى [ك][ي]
# apl-source:8
# الأبعاد تنقلب
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
def بدّل(م):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ك in range(len(م[0])):
    # apl-source:21
    صف = []
    # apl-source:22
    for ي in range(len(م)):
      # apl-source:23
      صف.append(م[ي][ك])
    # apl-source:24
    ناتج.append(صف)
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(بدّل([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]], "مستطيلة")
# apl-source:28
تأكد_يساوي(بدّل([[1]]), [[1]], "خلية")
# apl-source:29
تأكد_يساوي(بدّل([[1, 2]]), [[1], [2]], "صف")
# apl-source:30
