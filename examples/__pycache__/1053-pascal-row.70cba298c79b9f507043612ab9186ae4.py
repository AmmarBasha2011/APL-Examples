
# apl-source:1
# مثال 1053 — صف من مثلث باسكال
# apl-source:2
# Pascal row by index
# apl-source:3
# Demonstrates: صف واحد في مكانه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1053-pascal-row.apl
# apl-source:6

# apl-source:7
# نحدث صفاً واحداً من اليمين لليسار
# apl-source:8
# فلا نحتاج المثلث كله
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
def صف_باسكال(ك):
  # apl-source:19
  صف = [1] * (ك + 1)
  # apl-source:20
  for ر in range(2, ك + 1):
    # apl-source:21
    for ج in range(ر - 1, 0, -1):
      # apl-source:22
      صف[ج] = صف[ج] + صف[ج - 1]
  # apl-source:23
  return صف
# apl-source:24

# apl-source:25
تأكد_يساوي(صف_باسكال(0), [1], "صف الصفر")
# apl-source:26
تأكد_يساوي(صف_باسكال(3), [1, 3, 3, 1], "صف ثلاثة")
# apl-source:27
تأكد_يساوي(صف_باسكال(5), [1, 5, 10, 10, 5, 1], "صف خمسة")
# apl-source:28
