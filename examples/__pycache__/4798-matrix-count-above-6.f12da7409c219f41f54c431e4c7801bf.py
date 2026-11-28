
# apl-source:1
# مثال 4798 — عدد العناصر الأكبر من 6
# apl-source:2
# Cells greater than 6
# apl-source:3
# Demonstrates: مصفوفات وقوائم متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4798-matrix-count-above-6.apl
# apl-source:6

# apl-source:7
# نعد الخلايا اللي قيمتها فوق حد معين
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(م):
  # apl-source:18
  ع = 0
  # apl-source:19
  for ص in م:
    # apl-source:20
    for خ in ص:
      # apl-source:21
      if خ > 6:
        # apl-source:22
        ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([[1, 2], [3, 4]]), 0, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([[5, 0, 2], [1, 9, 3], [4, 4, 4]]), 1, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([[2, -1, 7], [0, 3, -5]]), 1, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([[1], [2], [3]]), 0, "حالة 4")
# apl-source:29
تأكد_يساوي(ف([[6, 5, 4, 3], [2, 1, 0, -1]]), 0, "حالة 5")
# apl-source:30
