
# apl-source:1
# مثال 4916 — مجاميع نافذة بحجم 4
# apl-source:2
# Sliding window sums of size 4
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4916-window-sum-4.apl
# apl-source:6

# apl-source:7
# نحرك نافذة على القائمة ونجمع عناصرها
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
def ف(ق):
  # apl-source:18
  ر = []
  # apl-source:19
  for ي in range(len(ق) - 4 + 1):
    # apl-source:20
    ر = ر + [sum(ق[ي:ي + 4])]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), [10, 14, 18, 22, 26, 30, 34, 38], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([5, 1, 4, 2, 8, 3, 9, 7, 6, 0]), [12, 15, 17, 22, 27, 25, 22], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), [8, 8, 8, 8, 8, 8, 8], "حالة 3")
# apl-source:26
تأكد_يساوي(ف([3, 18, 18, 20, 6, 11, 3, 17, 2, 18, 1, 19]), [59, 62, 55, 40, 37, 33, 40, 38, 40], "حالة 4")
# apl-source:27
