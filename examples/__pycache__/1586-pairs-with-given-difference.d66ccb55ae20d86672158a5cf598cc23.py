
# apl-source:1
# مثال 1586 — أزواج بفرق معين
# apl-source:2
# Pairs with a given difference
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1586-pairs-with-given-difference.apl
# apl-source:6

# apl-source:7
# نخزن القيم في قاموس
# apl-source:8
# لكل قيمة نبحث عن قيمة زائد الفرق
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
def أزواج_بفرق(أ, فرق):
  # apl-source:19
  موجود = {}
  # apl-source:20
  for ع in أ:
    # apl-source:21
    موجود[ع] = True
  # apl-source:22
  عد = 0
  # apl-source:23
  for ع in موجود:
    # apl-source:24
    if (ع + فرق) in موجود:
      # apl-source:25
      عد = عد + 1
  # apl-source:26
  return عد
# apl-source:27

# apl-source:28
تأكد_يساوي(أزواج_بفرق([1, 5, 3, 4, 2], 2), 3, "ثلاثة")
# apl-source:29
تأكد_يساوي(أزواج_بفرق([1, 2, 3], 5), 0, "لا يوجد")
# apl-source:30
تأكد_يساوي(أزواج_بفرق([1, 3, 1, 5], 2), 2, "مكرر")
# apl-source:31
