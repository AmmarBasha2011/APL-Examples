
# apl-source:1
# مثال 1724 — الفرز بالعد لنطاق صغير
# apl-source:2
# Counting sort for small range
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1724-counting-sort-small-range.apl
# apl-source:6

# apl-source:7
# نحجز جدول عد بحجم أكبر قيمة
# apl-source:8
# نقرأ الجدول بالترتيب
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
def فرز_بالعد(ق, أعلى):
  # apl-source:19
  عد = []
  # apl-source:20
  for ك in range(أعلى + 1):
    # apl-source:21
    عد.append(0)
  # apl-source:22
  for ع in ق:
    # apl-source:23
    عد[ع] = عد[ع] + 1
  # apl-source:24
  ناتج = []
  # apl-source:25
  for ك in range(أعلى + 1):
    # apl-source:26
    for ي in range(عد[ك]):
      # apl-source:27
      ناتج.append(ك)
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(فرز_بالعد([3, 1, 2, 3, 0], 3), [0, 1, 2, 3, 3], "خمسة")
# apl-source:31
تأكد_يساوي(فرز_بالعد([], 5), [], "فارغة")
# apl-source:32
تأكد_يساوي(فرز_بالعد([2, 2], 2), [2, 2], "متكررة")
# apl-source:33
