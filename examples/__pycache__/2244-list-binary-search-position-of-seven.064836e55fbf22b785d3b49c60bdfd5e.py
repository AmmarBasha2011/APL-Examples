
# apl-source:1
# مثال 2244 — موضع سبعة بالبحث الثنائي
# apl-source:2
# Binary search for seven
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2244-list-binary-search-position-of-seven.apl
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
  د = 0
  # apl-source:20
  ع = len(ق) - 1
  # apl-source:21
  while د <= ع:
    # apl-source:22
    و2 = (د + ع) // 2
    # apl-source:23
    if ق[و2] == 7:
      # apl-source:24
      return و2
    # apl-source:25
    elif ق[و2] < 7:
      # apl-source:26
      د = و2 + 1
    # apl-source:27
    else:
      # apl-source:28
      ع = و2 - 1
  # apl-source:29
  return -1
# apl-source:30

# apl-source:31
تأكد_يساوي(ف([1, 3, 5, 7, 9]), 3, "حالة 1")
# apl-source:32
تأكد_يساوي(ف([7]), 0, "حالة 2")
# apl-source:33
تأكد_يساوي(ف([1, 2, 3]), -1, "حالة 3")
# apl-source:34
تأكد_يساوي(ف([2, 4, 6, 7, 8, 10]), 3, "حالة 4")
# apl-source:35
