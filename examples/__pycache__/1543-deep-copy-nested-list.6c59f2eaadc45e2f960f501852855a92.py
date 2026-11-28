
# apl-source:1
# مثال 1543 — نسخ عميق لقائمة متداخلة
# apl-source:2
# Deep copy of nested lists
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1543-deep-copy-nested-list.apl
# apl-source:6

# apl-source:7
# النسخ السطحي يشارك القوائم الداخلية
# apl-source:8
# ننسخ تراجعياً كل قائمة داخلية
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
def انسخ(ق):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    if type(ع) == type([]):
      # apl-source:22
      ناتج.append(انسخ(ع))
    # apl-source:23
    else:
      # apl-source:24
      ناتج.append(ع)
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
أصل = [1, [2, 3], [4, [5]]]
# apl-source:28
نسخة = انسخ(أصل)
# apl-source:29
أصل[1][0] = 99
# apl-source:30
أصل[2][1][0] = 77
# apl-source:31
تأكد_يساوي(نسخة, [1, [2, 3], [4, [5]]], "النسخة سليمة")
# apl-source:32
تأكد_يساوي(أصل, [1, [99, 3], [4, [77]]], "الأصل تغير")
# apl-source:33
