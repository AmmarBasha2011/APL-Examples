
# apl-source:1
# مثال 680 — طور القمر التقريبي
# apl-source:2
# Moon phase lite
# apl-source:3
# Demonstrates: شهر اقتراني، يوم جولياني، أطوار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/680-moon-phase-lite.apl
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
# طور القمر التقريبي
# apl-source:25
# Demonstrates: شهر اقتراني, يوم جولياني, أطوار مسماة
# apl-source:26
# يعرف هل الليلة محاق أم بدر من التاريخ وحده
# apl-source:27

# apl-source:28
اقتراني = 29.530588853
# apl-source:29
مرجع = 2451550.1
# apl-source:30

# apl-source:31
def يوم_جولياني(سنة, شهر, يوم):
  # apl-source:32
  أ = (14 - شهر) // 12
  # apl-source:33
  س2 = سنة + 4800 - أ
  # apl-source:34
  ش2 = شهر + 12 * أ - 3
  # apl-source:35
  return يوم + (153 * ش2 + 2) // 5 + 365 * س2 + س2 // 4 - س2 // 100 + س2 // 400 - 32045
# apl-source:36

# apl-source:37
def طور(سنة, شهر, يوم):
  # apl-source:38
  عمر = (يوم_جولياني(سنة, شهر, يوم) - مرجع) % اقتراني
  # apl-source:39
  if عمر < 1.84566:
    # apl-source:40
    return "محاق"
  # apl-source:41
  if عمر < 5.53699:
    # apl-source:42
    return "هلال متزايد"
  # apl-source:43
  if عمر < 9.22831:
    # apl-source:44
    return "تربيع أول"
  # apl-source:45
  if عمر < 12.91963:
    # apl-source:46
    return "أحدب متزايد"
  # apl-source:47
  if عمر < 16.61096:
    # apl-source:48
    return "بدر"
  # apl-source:49
  if عمر < 20.30228:
    # apl-source:50
    return "أحدب متناقص"
  # apl-source:51
  if عمر < 23.99361:
    # apl-source:52
    return "تربيع أخير"
  # apl-source:53
  if عمر < 27.68493:
    # apl-source:54
    return "هلال متناقص"
  # apl-source:55
  return "محاق"
# apl-source:56

# apl-source:57
تأكد_يساوي(طور(2024, 1, 11), "محاق", "محاق يناير 2024")
# apl-source:58
تأكد_يساوي(طور(2024, 1, 18), "تربيع أول", "تربيع أول")
# apl-source:59
تأكد_يساوي(طور(2024, 1, 25), "بدر", "بدر يناير 2024")
# apl-source:60
تأكد_يساوي(طور(2024, 2, 2), "تربيع أخير", "تربيع أخير")
# apl-source:61
تأكد_يساوي(طور(2024, 2, 9), "محاق", "محاق فبراير 2024")
# apl-source:62
print("طور 2024-01-25:", طور(2024, 1, 25))
# apl-source:63
