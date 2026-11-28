
# apl-source:1
# مثال 4780 — عدد التبديلات في ترتيب الفقاعات (تنازلي)
# apl-source:2
# Bubble sort swap count (descending)
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4780-bubble-swaps-desc.apl
# apl-source:6

# apl-source:7
# نقارن كل عنصرين متجاورين
# apl-source:8
# ونبدّلهم لو ترتيبهم غلط
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
  ق = ق + []
  # apl-source:20
  ع = 0
  # apl-source:21
  for ر in range(len(ق)):
    # apl-source:22
    for ي in range(len(ق) - 1 - ر):
      # apl-source:23
      if ق[ي] < ق[ي + 1]:
        # apl-source:24
        ق[ي], ق[ي + 1] = ق[ي + 1], ق[ي]
        # apl-source:25
        ع = ع + 1
  # apl-source:26
  return ع
# apl-source:27

# apl-source:28
تأكد_يساوي(ف([3, 1, 2]), 1, "حالة 1")
# apl-source:29
تأكد_يساوي(ف([1, 2, 3, 4]), 6, "حالة 2")
# apl-source:30
تأكد_يساوي(ف([5, 4, 3, 2, 1]), 0, "حالة 3")
# apl-source:31
تأكد_يساوي(ف([2, 2, 1, 1]), 0, "حالة 4")
# apl-source:32
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:33
