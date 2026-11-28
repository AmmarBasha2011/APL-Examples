
# apl-source:1
# مثال 1865 — صف من جدول الضرب
# apl-source:2
# Multiplication table row
# apl-source:3
# Demonstrates: حساب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1865-multiplication-table-row-list.apl
# apl-source:6

# apl-source:7
# نضرب العدد في 1 حتى 10
# apl-source:8
# نجمع الناتج في قائمة
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
def صف_الضرب(ن):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ك in range(1, 11):
    # apl-source:21
    ناتج.append(ن * ك)
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
تأكد_يساوي(صف_الضرب(3), [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], "ثلاثة")
# apl-source:25
تأكد_يساوي(صف_الضرب(1)[9], 10, "واحد")
# apl-source:26
تأكد_يساوي(صف_الضرب(0), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "صفر")
# apl-source:27
