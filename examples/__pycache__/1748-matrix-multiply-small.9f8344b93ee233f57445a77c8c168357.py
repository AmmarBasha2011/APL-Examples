
# apl-source:1
# مثال 1748 — ضرب مصفوفتين
# apl-source:2
# Multiply two matrices
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1748-matrix-multiply-small.apl
# apl-source:6

# apl-source:7
# العنصر مجموع حاصل ضرب صف في عمود
# apl-source:8
# الأبعاد يجب أن تتوافق
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
def اضرب(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ي in range(len(أ)):
    # apl-source:21
    صف = []
    # apl-source:22
    for ك in range(len(ب[0])):
      # apl-source:23
      مجموع = 0
      # apl-source:24
      for ج in range(len(ب)):
        # apl-source:25
        مجموع = مجموع + أ[ي][ج] * ب[ج][ك]
      # apl-source:26
      صف.append(مجموع)
    # apl-source:27
    ناتج.append(صف)
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(اضرب([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]], "اثنان")
# apl-source:31
تأكد_يساوي(اضرب([[1, 0], [0, 1]], [[9, 8], [7, 6]]), [[9, 8], [7, 6]], "الوحدة")
# apl-source:32
تأكد_يساوي(اضرب([[1, 2, 3]], [[1], [1], [1]]), [[6]], "صف في عمود")
# apl-source:33
