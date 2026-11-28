
# apl-source:1
# مثال 1782 — أطول متتالية عددية
# apl-source:2
# Longest consecutive sequence
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1782-longest-consecutive-run-set.apl
# apl-source:6

# apl-source:7
# قاموس كمجموعة
# apl-source:8
# نعد من العنصر الذي لا سابق له
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
def أطول_متتالية(ق):
  # apl-source:19
  مجموعة = {}
  # apl-source:20
  for ع in ق:
    # apl-source:21
    مجموعة[str(ع)] = 1
  # apl-source:22
  أفضل = 0
  # apl-source:23
  for ع in ق:
    # apl-source:24
    if (str(ع - 1) in مجموعة) == False:
      # apl-source:25
      طول_حالي = 1
      # apl-source:26
      while str(ع + طول_حالي) in مجموعة:
        # apl-source:27
        طول_حالي = طول_حالي + 1
      # apl-source:28
      أفضل = max(أفضل, طول_حالي)
  # apl-source:29
  return أفضل
# apl-source:30

# apl-source:31
تأكد_يساوي(أطول_متتالية([100, 4, 200, 1, 3, 2]), 4, "أربعة")
# apl-source:32
تأكد_يساوي(أطول_متتالية([]), 0, "فارغة")
# apl-source:33
تأكد_يساوي(أطول_متتالية([5, 5, 5]), 1, "مكررة")
# apl-source:34
