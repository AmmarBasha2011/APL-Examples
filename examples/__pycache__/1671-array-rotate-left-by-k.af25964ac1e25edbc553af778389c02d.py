
# apl-source:1
# مثال 1671 — تدوير المصفوفة لليسار
# apl-source:2
# Rotate array left by k
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1671-array-rotate-left-by-k.apl
# apl-source:6

# apl-source:7
# نأخذ ك مقياس الطول
# apl-source:8
# نبني القائمة الجديدة بالترتيب
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
def دوّر(ق, ك):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return []
  # apl-source:22
  ك = ك % ن
  # apl-source:23
  ناتج = []
  # apl-source:24
  for ع in range(ن):
    # apl-source:25
    ناتج.append(ق[(ع + ك) % ن])
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(دوّر([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2], "اثنان")
# apl-source:29
تأكد_يساوي(دوّر([1, 2, 3], 3), [1, 2, 3], "دورة كاملة")
# apl-source:30
تأكد_يساوي(دوّر([1, 2, 3], 4), [2, 3, 1], "أكبر من الطول")
# apl-source:31
