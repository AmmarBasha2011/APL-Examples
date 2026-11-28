
# apl-source:1
# مثال 4782 — عدد التبديلات في الترتيب بالاختيار
# apl-source:2
# Selection sort swap count
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4782-selection-swaps.apl
# apl-source:6

# apl-source:7
# نختار الأصغر ونبدله مع مكانه
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
  ق = ق + []
  # apl-source:19
  ع = 0
  # apl-source:20
  for ر in range(len(ق)):
    # apl-source:21
    م = ر
    # apl-source:22
    for ي in range(ر + 1, len(ق)):
      # apl-source:23
      if ق[ي] < ق[م]:
        # apl-source:24
        م = ي
    # apl-source:25
    if م != ر:
      # apl-source:26
      ق[ر], ق[م] = ق[م], ق[ر]
      # apl-source:27
      ع = ع + 1
  # apl-source:28
  return ع
# apl-source:29

# apl-source:30
تأكد_يساوي(ف([3, 1, 2]), 2, "حالة 1")
# apl-source:31
تأكد_يساوي(ف([1, 2, 3]), 0, "حالة 2")
# apl-source:32
تأكد_يساوي(ف([4, 3, 2, 1]), 2, "حالة 3")
# apl-source:33
تأكد_يساوي(ف([5, 1, 4, 2, 3]), 4, "حالة 4")
# apl-source:34
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:35
