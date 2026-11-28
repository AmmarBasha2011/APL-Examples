
# apl-source:1
# مثال 1995 — عدد أزواج القيم بفارق معين
# apl-source:2
# Count pairs with given difference
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1995-count-pairs-with-given-difference.apl
# apl-source:6

# apl-source:7
# # نحول القائمة إلى مجموعة قيم فريدة
# apl-source:8
# # ونعد القيم التي لها شريك
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
def ازواج(قائمة, ك):
  # apl-source:19
  قيم = {}
  # apl-source:20
  for ع in قائمة:
    # apl-source:21
    قيم[ع] = 1
  # apl-source:22
  عدد = 0
  # apl-source:23
  for ع in قيم:
    # apl-source:24
    if (ع + ك) in قيم:
      # apl-source:25
      عدد = عدد + 1
  # apl-source:26
  return عدد
# apl-source:27

# apl-source:28
تأكد_يساوي(ازواج([1, 5, 3, 4, 2], 2), 3, "ثلاثة أزواج")
# apl-source:29
تأكد_يساوي(ازواج([1, 3], 5), 0, "لا يوجد")
# apl-source:30
تأكد_يساوي(ازواج([1, 2, 2, 3], 1), 2, "قيم مكررة")
# apl-source:31
