
# apl-source:1
# مثال 1638 — ترتيب العملات في درج
# apl-source:2
# Arranging coins in a staircase
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1638-arranging-coins-staircase.apl
# apl-source:6

# apl-source:7
# الصف ك يحتاج ك عملة
# apl-source:8
# نبحث عن أكبر ك مجموعه لا يتجاوز العدد
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
  ج = ن
  # apl-source:21
  نتيجة = 0
  # apl-source:22
  while ي <= ج:
    # apl-source:23
    م = (ي + ج) // 2
    # apl-source:24
    if م * (م + 1) // 2 <= ن:
      # apl-source:25
      نتيجة = م
      # apl-source:26
      ي = م + 1
    # apl-source:27
    else:
      # apl-source:28
      ج = م - 1
  # apl-source:29
  return نتيجة
# apl-source:30

# apl-source:31
تأكد_يساوي(صفوف_كاملة(5), 2, "خمس")
# apl-source:32
تأكد_يساوي(صفوف_كاملة(8), 3, "ثمان")
# apl-source:33
تأكد_يساوي(صفوف_كاملة(1), 1, "واحدة")
# apl-source:34
تأكد_يساوي(صفوف_كاملة(0), 0, "لا شيء")
# apl-source:35
