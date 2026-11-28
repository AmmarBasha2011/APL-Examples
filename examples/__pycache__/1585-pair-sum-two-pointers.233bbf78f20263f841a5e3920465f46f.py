
# apl-source:1
# مثال 1585 — مجموع زوج بمؤشرين
# apl-source:2
# Pair sum with two pointers
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1585-pair-sum-two-pointers.apl
# apl-source:6

# apl-source:7
# مؤشر من البداية وآخر من النهاية
# apl-source:8
# نحرك المناسب بحسب المجموع
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
def يوجد_زوج(أ, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ن = len(أ) - 1
  # apl-source:21
  while ي < ن:
    # apl-source:22
    م = أ[ي] + أ[ن]
    # apl-source:23
    if م == هدف:
      # apl-source:24
      return True
    # apl-source:25
    elif م < هدف:
      # apl-source:26
      ي = ي + 1
    # apl-source:27
    else:
      # apl-source:28
      ن = ن - 1
  # apl-source:29
  return False
# apl-source:30

# apl-source:31
تأكد_يساوي(يوجد_زوج([1, 2, 4, 7, 11], 9), True, "زوج")
# apl-source:32
تأكد_يساوي(يوجد_زوج([1, 2, 4, 7, 11], 10), False, "لا يوجد")
# apl-source:33
تأكد_يساوي(يوجد_زوج([5], 10), False, "عنصر واحد")
# apl-source:34
