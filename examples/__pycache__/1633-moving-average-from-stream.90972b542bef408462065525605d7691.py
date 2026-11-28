
# apl-source:1
# مثال 1633 — متوسط متحرك من تدفق
# apl-source:2
# Moving average from a data stream
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1633-moving-average-from-stream.apl
# apl-source:6

# apl-source:7
# نحتفظ بقائمة النافذة ومجموعها
# apl-source:8
# القيمة الأقدم تخرج عند الامتلاء
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
def متوسطات_متحركة(قيم, حجم):
  # apl-source:19
  نافذة = []
  # apl-source:20
  مجموع = 0
  # apl-source:21
  ناتج = []
  # apl-source:22
  for ق in قيم:
    # apl-source:23
    نافذة.append(ق)
    # apl-source:24
    مجموع = مجموع + ق
    # apl-source:25
    if len(نافذة) > حجم:
      # apl-source:26
      مجموع = مجموع - نافذة[0]
      # apl-source:27
      نافذة.pop(0)
    # apl-source:28
    ناتج.append(مجموع / len(نافذة))
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(متوسطات_متحركة([1, 10, 3, 5], 3), [1.0, 5.5, 4.666666666666667, 6.0], "نافذة ثلاثة")
# apl-source:32
تأكد_يساوي(متوسطات_متحركة([4, 4], 1), [4.0, 4.0], "نافذة واحدة")
# apl-source:33
