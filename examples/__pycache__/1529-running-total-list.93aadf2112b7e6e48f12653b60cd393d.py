
# apl-source:1
# مثال 1529 — المجموع التراكمي
# apl-source:2
# Running total list
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1529-running-total-list.apl
# apl-source:6

# apl-source:7
# نحتفظ بمجموع جار
# apl-source:8
# نضيفه للقائمة بعد كل عنصر
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
def تراكمي(أ):
  # apl-source:19
  ناتج = []
  # apl-source:20
  جار = 0
  # apl-source:21
  for ع in أ:
    # apl-source:22
    جار = جار + ع
    # apl-source:23
    ناتج.append(جار)
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
تأكد_يساوي(تراكمي([1, 2, 3, 4]), [1, 3, 6, 10], "أربعة")
# apl-source:27
تأكد_يساوي(تراكمي([5, -5, 5]), [5, 0, 5], "سالب")
# apl-source:28
تأكد_يساوي(تراكمي([]), [], "فارغة")
# apl-source:29
