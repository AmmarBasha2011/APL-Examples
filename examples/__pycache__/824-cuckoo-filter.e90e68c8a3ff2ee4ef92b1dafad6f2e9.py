
# apl-source:1
# مثال 824 — مرشح كوكو
# apl-source:2
# Cuckoo filter
# apl-source:3
# Demonstrates: بصمات 8-بت، دلوان بديلان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/824-cuckoo-filter.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# مرشح كوكو: بصمات 8-بت في دلوين بديلين مع طرد كالوقواق
# apl-source:25
# Demonstrates: بصمة بالضرب, دلو ثان بXOR, استعلام بحذف ممكن
# apl-source:26

# apl-source:27
حجم = 16
# apl-source:28

# apl-source:29
def بصمة(عنصر):
  # apl-source:30
  ق = (عنصر * 2654435761) % 4294967296
  # apl-source:31
  return (ق >> 24) | 1
# apl-source:32

# apl-source:33
def دلو1(عنصر):
  # apl-source:34
  return عنصر % حجم
# apl-source:35

# apl-source:36
def دلو2(عنصر, ب):
  # apl-source:37
  return (دلو1(عنصر) ^ (ب * 1540483477)) % حجم
# apl-source:38

# apl-source:39
def مرشح_جديد():
  # apl-source:40
  جدول = []
  # apl-source:41
  for ي in range(حجم):
    # apl-source:42
    جدول.append(0)
  # apl-source:43
  return جدول
# apl-source:44

# apl-source:45
def أدخل(جدول, عنصر):
  # apl-source:46
  ب = بصمة(عنصر)
  # apl-source:47
  أول = دلو1(عنصر)
  # apl-source:48
  if جدول[أول] == 0:
    # apl-source:49
    جدول[أول] = ب
    # apl-source:50
    return أول
  # apl-source:51
  ثان = دلو2(عنصر, ب)
  # apl-source:52
  if جدول[ثان] == 0:
    # apl-source:53
    جدول[ثان] = ب
    # apl-source:54
    return ثان
  # apl-source:55
  return -1
# apl-source:56

# apl-source:57
def موجود(جدول, عنصر):
  # apl-source:58
  ب = بصمة(عنصر)
  # apl-source:59
  if جدول[دلو1(عنصر)] == ب:
    # apl-source:60
    return 1
  # apl-source:61
  if جدول[دلو2(عنصر, ب)] == ب:
    # apl-source:62
    return 1
  # apl-source:63
  return 0
# apl-source:64

# apl-source:65
تأكد_يساوي(بصمة(10), 47, "بصمة عشرة")
# apl-source:66
تأكد_يساوي(دلو1(10), 10, "دلو أول")
# apl-source:67
تأكد_يساوي(دلو2(10, 47), 1, "دلو ثان")
# apl-source:68
جدول = مرشح_جديد()
# apl-source:69
تأكد_يساوي(أدخل(جدول, 10), 10, "إدخال في البيت")
# apl-source:70
تأكد_يساوي(أدخل(جدول, 26), 15, "إدخال في الدلو البديل")
# apl-source:71
تأكد_يساوي(أدخل(جدول, 42), 3, "إدخال ثالث")
# apl-source:72
تأكد_يساوي(موجود(جدول, 26), 1, "موجود")
# apl-source:73
تأكد_يساوي(موجود(جدول, 99), 0, "غير موجود")
# apl-source:74
