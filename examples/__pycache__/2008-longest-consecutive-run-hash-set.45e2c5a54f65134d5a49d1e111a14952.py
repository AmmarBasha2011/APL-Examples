
# apl-source:1
# مثال 2008 — أطول متتالية أعداد صحيحة
# apl-source:2
# Longest consecutive sequence
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2008-longest-consecutive-run-hash-set.apl
# apl-source:6

# apl-source:7
# # نضع الأعداد في قاموس
# apl-source:8
# # ثم نمشي من بداية كل متتالية
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
def متتالية(ق):
  # apl-source:19
  م = {}
  # apl-source:20
  for ع in ق:
    # apl-source:21
    م[ع] = 1
  # apl-source:22
  افضل = 0
  # apl-source:23
  for ع in م:
    # apl-source:24
    if ((ع - 1) in م) == False:
      # apl-source:25
      ن = ع
      # apl-source:26
      while (ن + 1) in م:
        # apl-source:27
        ن = ن + 1
      # apl-source:28
      افضل = max(افضل, ن - ع + 1)
  # apl-source:29
  return افضل
# apl-source:30

# apl-source:31
تأكد_يساوي(متتالية([100, 4, 200, 1, 3, 2]), 4, "أربعة")
# apl-source:32
تأكد_يساوي(متتالية([]), 0, "فارغة")
# apl-source:33
تأكد_يساوي(متتالية([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9, "تسعة")
# apl-source:34
