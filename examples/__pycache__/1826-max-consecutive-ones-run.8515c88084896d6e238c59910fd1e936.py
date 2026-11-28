
# apl-source:1
# مثال 1826 — أطول سلسلة آحاد
# apl-source:2
# Maximum consecutive ones
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1826-max-consecutive-ones-run.apl
# apl-source:6

# apl-source:7
# نصفر العداد عند الصفر
# apl-source:8
# نحتفظ بالأعلى
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
def أطول_آحاد(ق):
  # apl-source:19
  أعلى = 0
  # apl-source:20
  حالي = 0
  # apl-source:21
  for ع in ق:
    # apl-source:22
    if ع == 1:
      # apl-source:23
      حالي = حالي + 1
      # apl-source:24
      أعلى = max(أعلى, حالي)
    # apl-source:25
    else:
      # apl-source:26
      حالي = 0
  # apl-source:27
  return أعلى
# apl-source:28

# apl-source:29
تأكد_يساوي(أطول_آحاد([1, 1, 0, 1, 1, 1]), 3, "ثلاثة")
# apl-source:30
تأكد_يساوي(أطول_آحاد([0, 0]), 0, "أصفار")
# apl-source:31
تأكد_يساوي(أطول_آحاد([1]), 1, "واحد")
# apl-source:32
