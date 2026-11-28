
# apl-source:1
# مثال 2297 — تدوير المصفوفة مع عقارب الساعة
# apl-source:2
# Rotate clockwise
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2297-matrix-rotate-clockwise-square.apl
# apl-source:6

# apl-source:7
# # مصفوفة من قوائم
# apl-source:8
# # ونتحقق من الناتج
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
  ن = len(م)
  # apl-source:20
  ر = []
  # apl-source:21
  for ي in range(ن):
    # apl-source:22
    ص = []
    # apl-source:23
    for ك in range(ن - 1, -1, -1):
      # apl-source:24
      ص = ص + [م[ك][ي]]
    # apl-source:25
    ر = ر + [ص]
  # apl-source:26
  return ر
# apl-source:27

# apl-source:28
تأكد_يساوي(ف([[1, 2], [3, 4]]), [[3, 1], [4, 2]], "حالة 1")
# apl-source:29
تأكد_يساوي(ف([[5]]), [[5]], "حالة 2")
# apl-source:30
تأكد_يساوي(ف([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "حالة 3")
# apl-source:31
تأكد_يساوي(ف([[0, 1], [1, 0]]), [[1, 0], [0, 1]], "حالة 4")
# apl-source:32
تأكد_يساوي(ف([[2, -1, 0], [0, 3, 1], [1, 1, 1]]), [[1, 0, 2], [1, 3, -1], [1, 1, 0]], "حالة 5")
# apl-source:33
