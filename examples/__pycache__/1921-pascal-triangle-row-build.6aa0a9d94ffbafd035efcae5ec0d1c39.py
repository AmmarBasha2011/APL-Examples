
# apl-source:1
# مثال 1921 — صف من مثلث باسكال
# apl-source:2
# Build a row of Pascal triangle
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1921-pascal-triangle-row-build.apl
# apl-source:6

# apl-source:7
# نبدأ بصف فيه واحد
# apl-source:8
# نبني الصف الجديد من السابق
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
def صف_باسكال(ن):
  # apl-source:19
  ص = [1]
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    جديد = [1]
    # apl-source:22
    for ي in range(len(ص) - 1):
      # apl-source:23
      جديد = جديد + [ص[ي] + ص[ي + 1]]
    # apl-source:24
    جديد = جديد + [1]
    # apl-source:25
    ص = جديد
  # apl-source:26
  return ص
# apl-source:27

# apl-source:28
تأكد_يساوي(صف_باسكال(0), [1], "الصف ٠")
# apl-source:29
تأكد_يساوي(صف_باسكال(4), [1, 4, 6, 4, 1], "الصف ٤")
# apl-source:30
تأكد_يساوي(صف_باسكال(5), [1, 5, 10, 10, 5, 1], "الصف ٥")
# apl-source:31
