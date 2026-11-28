
# apl-source:1
# مثال 1481 — صف من مثلث باسكال
# apl-source:2
# Single Pascal triangle row
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1481-pascal-triangle-row.apl
# apl-source:6

# apl-source:7
# كل عنصر من الذي قبله بضرب وقسمة
# apl-source:8
# ج(ن,ك+1) = ج(ن,ك) × (ن-ك) ÷ (ك+1)
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
  for ك in range(ن):
    # apl-source:21
    صف.append(صف[ك] * (ن - ك) // (ك + 1))
  # apl-source:22
  return صف
# apl-source:23

# apl-source:24
تأكد_يساوي(صف_باسكال(0), [1], "صفر")
# apl-source:25
تأكد_يساوي(صف_باسكال(4), [1, 4, 6, 4, 1], "أربعة")
# apl-source:26
تأكد_يساوي(صف_باسكال(6), [1, 6, 15, 20, 15, 6, 1], "ستة")
# apl-source:27
