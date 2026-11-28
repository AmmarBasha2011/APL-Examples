
# apl-source:1
# مثال 1503 — هجوم الوزير في الشطرنج
# apl-source:2
# Queen attack check
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1503-queen-attack-check.apl
# apl-source:6

# apl-source:7
# الهجوم على نفس الصف أو العمود
# apl-source:8
# أو على القطر حيث فرقا الصف والعمود متساويان
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
def يهاجم(وزير, هدف):
  # apl-source:19
  فرق_ص = وزير[0] - هدف[0]
  # apl-source:20
  فرق_ع = وزير[1] - هدف[1]
  # apl-source:21
  if فرق_ص < 0:
    # apl-source:22
    فرق_ص = -فرق_ص
  # apl-source:23
  if فرق_ع < 0:
    # apl-source:24
    فرق_ع = -فرق_ع
  # apl-source:25
  if فرق_ص == 0 and فرق_ع == 0:
    # apl-source:26
    return False
  # apl-source:27
  return فرق_ص == 0 or فرق_ع == 0 or فرق_ص == فرق_ع
# apl-source:28

# apl-source:29
تأكد_يساوي(يهاجم([0, 0], [0, 5]), True, "صف")
# apl-source:30
تأكد_يساوي(يهاجم([2, 2], [5, 5]), True, "قطر")
# apl-source:31
تأكد_يساوي(يهاجم([0, 0], [1, 2]), False, "حركة حصان")
# apl-source:32
تأكد_يساوي(يهاجم([3, 3], [3, 3]), False, "نفس الخانة")
# apl-source:33
