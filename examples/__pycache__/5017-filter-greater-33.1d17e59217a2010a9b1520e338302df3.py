
# apl-source:1
# مثال 5017 — العناصر الأكبر من 33
# apl-source:2
# Items greater than 33
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5017-filter-greater-33.apl
# apl-source:6

# apl-source:7
# نبني قائمة جديدة بالشرط
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
  ر = []
  # apl-source:19
  for خ in ق:
    # apl-source:20
    if خ > 33:
      # apl-source:21
      ر = ر + [خ]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]), [36, 39], "حالة 1")
# apl-source:25
تأكد_يساوي(ف([1, 2]), [], "حالة 2")
# apl-source:26
تأكد_يساوي(ف([100, 5, 50]), [100, 50], "حالة 3")
# apl-source:27
