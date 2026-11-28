
# apl-source:1
# مثال 4918 — مجاميع نافذة بحجم 5
# apl-source:2
# Sliding window sums of size 5
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4918-window-sum-5.apl
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
  for ي in range(len(ق) - 5 + 1):
    # apl-source:20
    ر = ر + [sum(ق[ي:ي + 5])]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), [15, 20, 25, 30, 35, 40, 45], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([5, 1, 4, 2, 8, 3, 9, 7, 6, 0]), [20, 18, 26, 29, 33, 25], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), [10, 10, 10, 10, 10, 10], "حالة 3")
# apl-source:26
تأكد_يساوي(ف([7, 5, 7, 2, 18, 9, 16, 15, 10, 14, 9, 19]), [39, 41, 52, 60, 68, 64, 64, 67], "حالة 4")
# apl-source:27
