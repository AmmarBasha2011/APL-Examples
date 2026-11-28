
# apl-source:1
# مثال 661 — التقويم القبطي
# apl-source:2
# Coptic calendar
# apl-source:3
# Demonstrates: تقويم قبطي، سنة كبيسة، شهر صغير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/661-coptic-calendar.apl
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
# التقويم القبطي: سنوات وشهور وقبسي
# apl-source:25
# Demonstrates: سنة 365 يوما مع كبس كل أربع, 12 شهرا وشهر صغير, ذهاب وإياب
# apl-source:26
# تقويم ما زال يحدد الأعياد في مصر
# apl-source:27

# apl-source:28
حقبة = 1825029
# apl-source:29

# apl-source:30
def أول_سنة(سنة):
  # apl-source:31
  return حقبة + 365 * (سنة - 1) + سنة // 4
# apl-source:32

# apl-source:33
def كبيسة(سنة):
  # apl-source:34
  return سنة % 4 == 3
# apl-source:35

# apl-source:36
def إلى_قبطي(يوم_جولياني):
  # apl-source:37
  سنة = (يوم_جولياني - حقبة) * 4 // 1461 + 1
  # apl-source:38
  while أول_سنة(سنة) > يوم_جولياني:
    # apl-source:39
    سنة = سنة - 1
  # apl-source:40
  while أول_سنة(سنة + 1) <= يوم_جولياني:
    # apl-source:41
    سنة = سنة + 1
  # apl-source:42
  من_السنة = يوم_جولياني - أول_سنة(سنة)
  # apl-source:43
  شهر = من_السنة // 30 + 1
  # apl-source:44
  يوم = من_السنة % 30 + 1
  # apl-source:45
  return [سنة, شهر, يوم]
# apl-source:46

# apl-source:47
def من_قبطي(سنة, شهر, يوم):
  # apl-source:48
  return أول_سنة(سنة) + (شهر - 1) * 30 + (يوم - 1)
# apl-source:49

# apl-source:50
تأكد_يساوي(كبيسة(3), True, "السنة الثالثة كبيسة")
# apl-source:51
تأكد_يساوي(كبيسة(1739), True, "1739 كبيسة")
# apl-source:52
تأكد_يساوي(كبيسة(1740), False, "1740 بسيطة")
# apl-source:53
تأكد_يساوي(أول_سنة(4) - أول_سنة(3), 366, "طول سنة كبيسة")
# apl-source:54
تأكد_يساوي(أول_سنة(2) - أول_سنة(1), 365, "طول سنة بسيطة")
# apl-source:55
for ي in [2450000, 2459000, 2460200, 2460300]:
  # apl-source:56
  ق = إلى_قبطي(ي)
  # apl-source:57
  تأكد_يساوي(من_قبطي(ق[0], ق[1], ق[2]), ي, "ذهاب وإياب")
# apl-source:58
ق = إلى_قبطي(2460200)
# apl-source:59
تأكد_يساوي(ق[1] >= 1 and ق[1] <= 13, True, "شهر صالح")
# apl-source:60
تأكد_يساوي(ق[2] >= 1 and ق[2] <= 30, True, "يوم صالح")
# apl-source:61
print("2460200 قبطيا:", ق)
# apl-source:62
