
# apl-source:1
# مثال 4794 — ضرب كل عنصر في 3
# apl-source:2
# multiply every cell by 3
# apl-source:3
# Demonstrates: مصفوفات وقوائم متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4794-matrix-scale.apl
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
    ر = []
    # apl-source:22
    for خ in ص:
      # apl-source:23
      ر = ر + [خ * 3]
    # apl-source:24
    ن = ن + [ر]
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([[1, 2], [3, 4]]), [[3, 6], [9, 12]], "حالة 1")
# apl-source:28
تأكد_يساوي(ف([[5, 0, 2], [1, 9, 3], [4, 4, 4]]), [[15, 0, 6], [3, 27, 9], [12, 12, 12]], "حالة 2")
# apl-source:29
تأكد_يساوي(ف([[2, -1, 7], [0, 3, -5]]), [[6, -3, 21], [0, 9, -15]], "حالة 3")
# apl-source:30
تأكد_يساوي(ف([[1], [2], [3]]), [[3], [6], [9]], "حالة 4")
# apl-source:31
تأكد_يساوي(ف([[6, 5, 4, 3], [2, 1, 0, -1]]), [[18, 15, 12, 9], [6, 3, 0, -3]], "حالة 5")
# apl-source:32
