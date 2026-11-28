
# apl-source:1
# مثال 4784 — مجموع كل صف
# apl-source:2
# sum of each row
# apl-source:3
# Demonstrates: مصفوفات وقوائم متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4784-matrix-row-sums.apl
# apl-source:6

# apl-source:7
# المصفوفة قائمة من القوائم
# apl-source:8
# كل قائمة صغيرة هي صف
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
def ف(م):
  # apl-source:19
  ن = []
  # apl-source:20
  for ص in م:
    # apl-source:21
    ج = 0
    # apl-source:22
    for خ in ص:
      # apl-source:23
      ج = ج + خ
    # apl-source:24
    ن = ن + [ج]
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([[1, 2], [3, 4]]), [3, 7], "حالة 1")
# apl-source:28
تأكد_يساوي(ف([[5, 0, 2], [1, 9, 3], [4, 4, 4]]), [7, 13, 12], "حالة 2")
# apl-source:29
تأكد_يساوي(ف([[2, -1, 7], [0, 3, -5]]), [8, -2], "حالة 3")
# apl-source:30
تأكد_يساوي(ف([[1], [2], [3]]), [1, 2, 3], "حالة 4")
# apl-source:31
تأكد_يساوي(ف([[6, 5, 4, 3], [2, 1, 0, -1]]), [18, 2], "حالة 5")
# apl-source:32
