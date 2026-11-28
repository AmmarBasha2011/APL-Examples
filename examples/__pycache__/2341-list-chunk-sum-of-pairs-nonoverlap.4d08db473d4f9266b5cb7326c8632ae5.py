
# apl-source:1
# مثال 2341 — مجموع أزواج غير متداخلة
# apl-source:2
# Non overlapping pair sums
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2341-list-chunk-sum-of-pairs-nonoverlap.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
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
def ف(ق):
  # apl-source:19
  ر = []
  # apl-source:20
  for ي in range(0, len(ق), 2):
    # apl-source:21
    if ي + 1 < len(ق):
      # apl-source:22
      ر = ر + [ق[ي] + ق[ي + 1]]
    # apl-source:23
    else:
      # apl-source:24
      ر = ر + [ق[ي]]
  # apl-source:25
  return ر
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([1, 2, 3, 4]), [3, 7], "حالة 1")
# apl-source:28
تأكد_يساوي(ف([1, 2, 3]), [3, 3], "حالة 2")
# apl-source:29
تأكد_يساوي(ف([5]), [5], "حالة 3")
# apl-source:30
تأكد_يساوي(ف([]), [], "حالة 4")
# apl-source:31
