
# apl-source:1
# مثال 1652 — عدد تجزئات العدد
# apl-source:2
# Integer partition count
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1652-integer-partition-count.apl
# apl-source:6

# apl-source:7
# نضيف الأجزاء من الأصغر
# apl-source:8
# ن(ك) تزيد بـ ن(ك-جزء) لكل جزء
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
def تجزئات(ن):
  # apl-source:19
  طرق = [1]
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    طرق.append(0)
  # apl-source:22
  for جزء in range(1, ن + 1):
    # apl-source:23
    for ك in range(جزء, ن + 1):
      # apl-source:24
      طرق[ك] = طرق[ك] + طرق[ك - جزء]
  # apl-source:25
  return طرق[ن]
# apl-source:26

# apl-source:27
تأكد_يساوي(تجزئات(1), 1, "واحد")
# apl-source:28
تأكد_يساوي(تجزئات(4), 5, "أربعة")
# apl-source:29
تأكد_يساوي(تجزئات(7), 15, "سبعة")
# apl-source:30
تأكد_يساوي(تجزئات(10), 42, "عشرة")
# apl-source:31
