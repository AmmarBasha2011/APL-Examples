
# apl-source:1
# مثال 2347 — عدد القمم المحلية
# apl-source:2
# Count local peaks
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2347-list-count-local-peaks-strict.apl
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
  ع = 0
  # apl-source:20
  for ي in range(1, len(ق) - 1):
    # apl-source:21
    if ق[ي] > ق[ي - 1] and ق[ي] > ق[ي + 1]:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([1, 3, 2, 4, 1]), 2, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3]), 0, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([3, 1, 3]), 0, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([1, 5, 1, 5, 1, 5, 1]), 3, "حالة 4")
# apl-source:29
