
# apl-source:1
# مثال 4783 — خطوات البحث الثنائي (سالبة لو غير موجود)
# apl-source:2
# Binary search step count (negative if missing)
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4783-binary-search-steps.apl
# apl-source:6

# apl-source:7
# نقسم المدى للنصف في كل خطوة
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
def ف(ق, ه):
  # apl-source:18
  ن = 0
  # apl-source:19
  ع = len(ق) - 1
  # apl-source:20
  خ = 0
  # apl-source:21
  while ن <= ع:
    # apl-source:22
    خ = خ + 1
    # apl-source:23
    م = (ن + ع) // 2
    # apl-source:24
    if ق[م] == ه:
      # apl-source:25
      return خ
    # apl-source:26
    if ق[م] < ه:
      # apl-source:27
      ن = م + 1
    # apl-source:28
    else:
      # apl-source:29
      ع = م - 1
  # apl-source:30
  return 0 - خ
# apl-source:31

# apl-source:32
تأكد_يساوي(ف([1, 3, 5, 7, 9, 11], 7), 3, "حالة 1")
# apl-source:33
تأكد_يساوي(ف([1, 3, 5, 7, 9, 11], 1), 2, "حالة 2")
# apl-source:34
تأكد_يساوي(ف([1, 3, 5, 7, 9, 11], 4), -3, "حالة 3")
# apl-source:35
تأكد_يساوي(ف([2, 4, 6, 8], 8), 3, "حالة 4")
# apl-source:36
تأكد_يساوي(ف([], 5), 0, "حالة 5")
# apl-source:37
