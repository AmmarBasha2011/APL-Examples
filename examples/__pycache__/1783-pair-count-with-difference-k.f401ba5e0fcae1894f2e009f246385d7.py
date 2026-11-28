
# apl-source:1
# مثال 1783 — أزواج بفرق معين
# apl-source:2
# Count pairs with difference k
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1783-pair-count-with-difference-k.apl
# apl-source:6

# apl-source:7
# نخزن الأعداد في قاموس
# apl-source:8
# كل عدد يبحث عن شريكه
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
def أزواج_الفرق(ق, ك):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in ق:
    # apl-source:21
    عد[str(ع)] = عد.get(str(ع), 0) + 1
  # apl-source:22
  مجموع = 0
  # apl-source:23
  for ع in ق:
    # apl-source:24
    مجموع = مجموع + عد.get(str(ع + ك), 0)
  # apl-source:25
  return مجموع
# apl-source:26

# apl-source:27
تأكد_يساوي(أزواج_الفرق([1, 5, 3, 4, 2], 2), 3, "ثلاثة")
# apl-source:28
تأكد_يساوي(أزواج_الفرق([1, 4], 3), 1, "زوج")
# apl-source:29
تأكد_يساوي(أزواج_الفرق([1, 2, 3], 5), 0, "لا يوجد")
# apl-source:30
