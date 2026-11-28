
# apl-source:1
# مثال 2258 — أول موجب مفقود
# apl-source:2
# First missing positive
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2258-list-first-missing-positive-small.apl
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
  ك = 1
  # apl-source:20
  while ق.count(ك) > 0:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([1, 2, 0]), 3, "حالة 1")
# apl-source:25
تأكد_يساوي(ف([3, 4, -1, 1]), 2, "حالة 2")
# apl-source:26
تأكد_يساوي(ف([7, 8]), 1, "حالة 3")
# apl-source:27
تأكد_يساوي(ف([1, 2, 3]), 4, "حالة 4")
# apl-source:28
