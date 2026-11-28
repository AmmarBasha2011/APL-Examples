
# apl-source:1
# مثال 4789 — مجموع كل العناصر
# apl-source:2
# total of all cells
# apl-source:3
# Demonstrates: مصفوفات وقوائم متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4789-matrix-total.apl
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
  ج = 0
  # apl-source:20
  for ص in م:
    # apl-source:21
    for خ in ص:
      # apl-source:22
      ج = ج + خ
  # apl-source:23
  return ج
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([[1, 2], [3, 4]]), 10, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([[5, 0, 2], [1, 9, 3], [4, 4, 4]]), 32, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([[2, -1, 7], [0, 3, -5]]), 6, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([[1], [2], [3]]), 6, "حالة 4")
# apl-source:29
تأكد_يساوي(ف([[6, 5, 4, 3], [2, 1, 0, -1]]), 20, "حالة 5")
# apl-source:30
