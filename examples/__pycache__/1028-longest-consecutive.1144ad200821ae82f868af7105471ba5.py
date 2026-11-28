
# apl-source:1
# مثال 1028 — أطول متتالية
# apl-source:2
# Longest consecutive sequence
# apl-source:3
# Demonstrates: بداية المتتالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1028-longest-consecutive.apl
# apl-source:6

# apl-source:7
# نبدأ العد فقط من عدد لا يسبقه عدد في القائمة
# apl-source:8
# فكل متتالية تُعد مرة واحدة
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
def اطول_متتالية(ق):
  # apl-source:19
  افضل = 0
  # apl-source:20
  for س in ق:
    # apl-source:21
    if (س - 1) not in ق:
      # apl-source:22
      ط = 1
      # apl-source:23
      while (س + ط) in ق:
        # apl-source:24
        ط = ط + 1
      # apl-source:25
      if ط > افضل:
        # apl-source:26
        افضل = ط
  # apl-source:27
  return افضل
# apl-source:28

# apl-source:29
تأكد_يساوي(اطول_متتالية([100, 4, 200, 1, 3, 2]), 4, "من 1 إلى 4")
# apl-source:30
تأكد_يساوي(اطول_متتالية([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9, "تسعة")
# apl-source:31
تأكد_يساوي(اطول_متتالية([]), 0, "فارغة")
# apl-source:32
