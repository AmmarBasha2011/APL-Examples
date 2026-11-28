
# apl-source:1
# مثال 2065 — الفرز المتعرج بتبديل الجيران
# apl-source:2
# Wiggle sort adjacent swaps
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2065-wiggle-sort-adjacent-swaps.apl
# apl-source:6

# apl-source:7
# # في المواضع الزوجية نريد الأصغر
# apl-source:8
# # وفي الفردية الأكبر
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
def تعرج(ق):
  # apl-source:19
  ق = ق[:]
  # apl-source:20
  for ك in range(len(ق) - 1):
    # apl-source:21
    if (ك % 2 == 0 and ق[ك] > ق[ك + 1]) or (ك % 2 == 1 and ق[ك] < ق[ك + 1]):
      # apl-source:22
      ت = ق[ك]
      # apl-source:23
      ق[ك] = ق[ك + 1]
      # apl-source:24
      ق[ك + 1] = ت
  # apl-source:25
  return ق
# apl-source:26

# apl-source:27
تأكد_يساوي(تعرج([1, 5, 1, 1, 6, 4]), [1, 5, 1, 6, 1, 4], "ستة")
# apl-source:28
تأكد_يساوي(تعرج([3, 5, 2, 1, 6, 4]), [3, 5, 1, 6, 2, 4], "ستة ثانية")
# apl-source:29
تأكد_يساوي(تعرج([1]), [1], "واحد")
# apl-source:30
