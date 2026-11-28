
# apl-source:1
# مثال 1509 — ترميز الفروق
# apl-source:2
# Delta encoding of a list
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1509-delta-encode-list.apl
# apl-source:6

# apl-source:7
# العنصر الأول يبقى كما هو
# apl-source:8
# باقي العناصر تخزن فروقها
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
def رمّز_الفروق(أ):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ناتج = [أ[0]]
  # apl-source:22
  for ع in range(1, len(أ)):
    # apl-source:23
    ناتج.append(أ[ع] - أ[ع - 1])
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
def فك_الفروق(د):
  # apl-source:27
  if len(د) == 0:
    # apl-source:28
    return []
  # apl-source:29
  ناتج = [د[0]]
  # apl-source:30
  for ع in range(1, len(د)):
    # apl-source:31
    ناتج.append(ناتج[ع - 1] + د[ع])
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(رمّز_الفروق([10, 12, 15, 15, 11]), [10, 2, 3, 0, -4], "ترميز")
# apl-source:35
تأكد_يساوي(فك_الفروق([10, 2, 3, 0, -4]), [10, 12, 15, 15, 11], "فك")
# apl-source:36
تأكد_يساوي(رمّز_الفروق([]), [], "فارغة")
# apl-source:37
