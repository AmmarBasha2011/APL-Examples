
# apl-source:1
# مثال 1070 — آحاد متتالية مع قلب
# apl-source:2
# Max consecutive ones with k flips
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1070-ones-with-flips.apl
# apl-source:6

# apl-source:7
# نافذة تحوي ك صفراً على الأكثر
# apl-source:8
# نضيقها من اليسار كلما زادت الأصفار عن المسموح
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
def اطول_آحاد(ق, ك):
  # apl-source:19
  ي = 0
  # apl-source:20
  اصفار = 0
  # apl-source:21
  افضل = 0
  # apl-source:22
  for ع in range(len(ق)):
    # apl-source:23
    if ق[ع] == 0:
      # apl-source:24
      اصفار = اصفار + 1
    # apl-source:25
    while اصفار > ك:
      # apl-source:26
      if ق[ي] == 0:
        # apl-source:27
        اصفار = اصفار - 1
      # apl-source:28
      ي = ي + 1
    # apl-source:29
    if ((ع - ي) + 1) > افضل:
      # apl-source:30
      افضل = (ع - ي) + 1
  # apl-source:31
  return افضل
# apl-source:32

# apl-source:33
تأكد_يساوي(اطول_آحاد([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6, "ك اثنان")
# apl-source:34
تأكد_يساوي(اطول_آحاد([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10, "ك ثلاثة")
# apl-source:35
تأكد_يساوي(اطول_آحاد([0, 0], 0), 0, "بلا قلب")
# apl-source:36
