
# apl-source:1
# مثال 1087 — ترتيب العملات
# apl-source:2
# Arranging coins
# apl-source:3
# Demonstrates: مجموع حسابي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1087-arranging-coins.apl
# apl-source:6

# apl-source:7
# الصف ك يحتاج ك عملة والمجموع ك(ك+1)/2
# apl-source:8
# نبحث بالبحث الثنائي عن أكبر ك لا يتجاوز مجموعه عدد العملات
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
def صفوف_كاملة(ن):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = ن
  # apl-source:21
  افضل = 0
  # apl-source:22
  while ي <= ل:
    # apl-source:23
    ك = (ي + ل) // 2
    # apl-source:24
    if ((ك * (ك + 1)) // 2) <= ن:
      # apl-source:25
      افضل = ك
      # apl-source:26
      ي = ك + 1
    # apl-source:27
    else:
      # apl-source:28
      ل = ك - 1
  # apl-source:29
  return افضل
# apl-source:30

# apl-source:31
تأكد_يساوي(صفوف_كاملة(5), 2, "خمس عملات")
# apl-source:32
تأكد_يساوي(صفوف_كاملة(8), 3, "ثمان عملات")
# apl-source:33
تأكد_يساوي(صفوف_كاملة(0), 0, "بلا عملات")
# apl-source:34
تأكد_يساوي(صفوف_كاملة(10), 4, "عشر عملات")
# apl-source:35
