
# apl-source:1
# مثال 4917 — أكبر قيمة في كل نافذة بحجم 4
# apl-source:2
# Sliding window max size 4
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4917-window-max-4.apl
# apl-source:6

# apl-source:7
# نأخذ max لكل شريحة
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
    ر = ر + [max(ق[ي:ي + 4])]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [4, 5, 9, 9, 9, 9, 6, 6], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [9, 8, 7, 6, 5, 4, 3], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([13, 31, 43, 34, 27, 49, 20, 29, 37, 29, 23, 19]), [43, 43, 49, 49, 49, 49, 37, 37, 37], "حالة 3")
# apl-source:26
تأكد_يساوي(ف([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, 1], "حالة 4")
# apl-source:27
