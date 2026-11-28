
# apl-source:1
# مثال 2290 — مجاميع الأعمدة
# apl-source:2
# Column sums
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2290-matrix-column-sums-list.apl
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
  ر = []
  # apl-source:20
  for ك in range(len(م[0])):
    # apl-source:21
    ت = 0
    # apl-source:22
    for ص in م:
      # apl-source:23
      ت = ت + ص[ك]
    # apl-source:24
    ر = ر + [ت]
  # apl-source:25
  return ر
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([[1, 2], [3, 4]]), [4, 6], "حالة 1")
# apl-source:28
تأكد_يساوي(ف([[5]]), [5], "حالة 2")
# apl-source:29
تأكد_يساوي(ف([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [12, 15, 18], "حالة 3")
# apl-source:30
تأكد_يساوي(ف([[0, 1], [1, 0]]), [1, 1], "حالة 4")
# apl-source:31
تأكد_يساوي(ف([[2, -1, 0], [0, 3, 1], [1, 1, 1]]), [3, 3, 2], "حالة 5")
# apl-source:32
