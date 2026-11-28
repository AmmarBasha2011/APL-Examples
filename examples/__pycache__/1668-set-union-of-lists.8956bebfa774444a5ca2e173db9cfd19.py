
# apl-source:1
# مثال 1668 — اتحاد قائمتين
# apl-source:2
# Union of two lists without repeats
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1668-set-union-of-lists.apl
# apl-source:6

# apl-source:7
# نضيف عناصر الأولى
# apl-source:8
# ثم عناصر الثانية غير الموجودة
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
def اتحاد(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in أ:
    # apl-source:21
    if (ع in ناتج) == False:
      # apl-source:22
      ناتج.append(ع)
  # apl-source:23
  for ع in ب:
    # apl-source:24
    if (ع in ناتج) == False:
      # apl-source:25
      ناتج.append(ع)
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(اتحاد([1, 2, 2], [2, 3]), [1, 2, 3], "اتحاد")
# apl-source:29
تأكد_يساوي(اتحاد([], [4, 4]), [4], "فارغة")
# apl-source:30
تأكد_يساوي(اتحاد([1], [1]), [1], "متطابقتان")
# apl-source:31
