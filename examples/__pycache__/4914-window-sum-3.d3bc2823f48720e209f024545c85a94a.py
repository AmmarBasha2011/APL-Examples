
# apl-source:1
# مثال 4914 — مجاميع نافذة بحجم 3
# apl-source:2
# Sliding window sums of size 3
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4914-window-sum-3.apl
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
  for ي in range(len(ق) - 3 + 1):
    # apl-source:20
    ر = ر + [sum(ق[ي:ي + 3])]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), [6, 9, 12, 15, 18, 21, 24, 27, 30], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([5, 1, 4, 2, 8, 3, 9, 7, 6, 0]), [10, 7, 14, 13, 20, 19, 22, 13], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), [6, 6, 6, 6, 6, 6, 6, 6], "حالة 3")
# apl-source:26
تأكد_يساوي(ف([3, 7, 20, 20, 18, 1, 18, 18, 12, 1, 7, 1]), [30, 47, 58, 39, 37, 37, 48, 31, 20, 9], "حالة 4")
# apl-source:27
