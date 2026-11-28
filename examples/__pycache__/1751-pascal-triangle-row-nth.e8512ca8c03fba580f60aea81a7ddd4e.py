
# apl-source:1
# مثال 1751 — صف مثلث باسكال
# apl-source:2
# Nth row of Pascal triangle
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1751-pascal-triangle-row-nth.apl
# apl-source:6

# apl-source:7
# نبني الصف من الصف السابق
# apl-source:8
# الأطراف دائماً واحد
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
  صف = [1]
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    جديد = [1]
    # apl-source:22
    for ك in range(1, len(صف)):
      # apl-source:23
      جديد.append(صف[ك - 1] + صف[ك])
    # apl-source:24
    جديد.append(1)
    # apl-source:25
    صف = جديد
  # apl-source:26
  return صف
# apl-source:27

# apl-source:28
تأكد_يساوي(صف_باسكال(0), [1], "الأول")
# apl-source:29
تأكد_يساوي(صف_باسكال(4), [1, 4, 6, 4, 1], "الخامس")
# apl-source:30
تأكد_يساوي(صف_باسكال(5), [1, 5, 10, 10, 5, 1], "السادس")
# apl-source:31
