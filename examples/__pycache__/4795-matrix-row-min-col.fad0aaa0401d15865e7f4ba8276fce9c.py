
# apl-source:1
# مثال 4795 — أصغر عنصر في كل عمود
# apl-source:2
# min of each column
# apl-source:3
# Demonstrates: مصفوفات وقوائم متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4795-matrix-row-min-col.apl
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
  for ع in range(len(م[0])):
    # apl-source:21
    ق = []
    # apl-source:22
    for ص in م:
      # apl-source:23
      ق = ق + [ص[ع]]
    # apl-source:24
    ن = ن + [min(ق)]
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([[1, 2], [3, 4]]), [1, 2], "حالة 1")
# apl-source:28
تأكد_يساوي(ف([[5, 0, 2], [1, 9, 3], [4, 4, 4]]), [1, 0, 2], "حالة 2")
# apl-source:29
تأكد_يساوي(ف([[2, -1, 7], [0, 3, -5]]), [0, -1, -5], "حالة 3")
# apl-source:30
تأكد_يساوي(ف([[1], [2], [3]]), [1], "حالة 4")
# apl-source:31
تأكد_يساوي(ف([[6, 5, 4, 3], [2, 1, 0, -1]]), [2, 1, 0, -1], "حالة 5")
# apl-source:32
