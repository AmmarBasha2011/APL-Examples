
# apl-source:1
# مثال 2066 — تبديل صفوف وأعمدة مصفوفة مستطيلة
# apl-source:2
# Transpose rectangular matrix
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2066-transpose-rectangular-matrix.apl
# apl-source:6

# apl-source:7
# # عدد الصفوف الجديد هو عدد الأعمدة القديم
# apl-source:8
# # نبني الصفوف عمودا عمودا
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
def بدل(م):
  # apl-source:19
  if len(م) == 0:
    # apl-source:20
    return []
  # apl-source:21
  خرج = []
  # apl-source:22
  for ج in range(len(م[0])):
    # apl-source:23
    صف = []
    # apl-source:24
    for ي in range(len(م)):
      # apl-source:25
      صف = صف + [م[ي][ج]]
    # apl-source:26
    خرج = خرج + [صف]
  # apl-source:27
  return خرج
# apl-source:28

# apl-source:29
تأكد_يساوي(بدل([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]], "٢×٣")
# apl-source:30
تأكد_يساوي(بدل([[1], [2]]), [[1, 2]], "عمود")
# apl-source:31
تأكد_يساوي(بدل([]), [], "فارغة")
# apl-source:32
