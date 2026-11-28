
# apl-source:1
# مثال 678 — التقويم العبري المصغر
# apl-source:2
# Hebrew calendar lite
# apl-source:3
# Demonstrates: تقويم قمري شمسي، مولاد، تأجيلات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/678-hebrew-calendar-lite.apl
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
# التقويم العبري: سنة شمسية قمرية
# apl-source:25
# Demonstrates: دورة ميطون 19 سنة, تأجيلات رأس السنة, طول السنة
# apl-source:26
# يجمع القمر والشمس بقواعد حسابية دقيقة
# apl-source:27

# apl-source:28
def كبيسة(سنة):
  # apl-source:29
  return (7 * سنة + 1) % 19 < 7
# apl-source:30

# apl-source:31
def رأس_سنة(سنة):
  # apl-source:32
  أشهر = 235 * ((سنة - 1) // 19) + 12 * ((سنة - 1) % 19) + (7 * ((سنة - 1) % 19) + 1) // 19
  # apl-source:33
  أجزاء = 204 + 793 * (أشهر % 1080)
  # apl-source:34
  ساعة = 5 + 12 * أشهر + 793 * (أشهر // 1080) + أجزاء // 1080
  # apl-source:35
  يوم = 1 + 29 * أشهر + ساعة // 24
  # apl-source:36
  باقي_أجزاء = 1080 * (ساعة % 24) + أجزاء % 1080
  # apl-source:37
  if باقي_أجزاء >= 19440 or (يوم % 7 == 2 and باقي_أجزاء >= 9924 and not كبيسة(سنة)) or (يوم % 7 == 1 and باقي_أجزاء >= 16789 and كبيسة(سنة - 1)):
    # apl-source:38
    يوم = يوم + 1
  # apl-source:39
  if يوم % 7 == 0 or يوم % 7 == 3 or يوم % 7 == 5:
    # apl-source:40
    يوم = يوم + 1
  # apl-source:41
  return يوم
# apl-source:42

# apl-source:43
تأكد_يساوي(كبيسة(5784), True, "5784 كبيسة")
# apl-source:44
تأكد_يساوي(كبيسة(5785), False, "5785 بسيطة")
# apl-source:45
تأكد_يساوي(كبيسة(5787), True, "5787 كبيسة")
# apl-source:46
تأكد_يساوي(رأس_سنة(5785) - رأس_سنة(5784), 383, "طول 5784")
# apl-source:47
تأكد_يساوي(رأس_سنة(5786) - رأس_سنة(5785), 355, "طول 5785")
# apl-source:48
تأكد_يساوي(رأس_سنة(5784) % 7, 6, "روش 5784 سبت")
# apl-source:49
تأكد_يساوي(رأس_سنة(5785) % 7, 4, "روش 5785 خميس")
# apl-source:50
تأكد_يساوي(رأس_سنة(5786) % 7, 2, "روش 5786 ثلاثاء")
# apl-source:51
for سنة in range(5780, 5800):
  # apl-source:52
  بقية = رأس_سنة(سنة) % 7
  # apl-source:53
  تأكد_يساوي(بقية != 0 and بقية != 3 and بقية != 5, True, "لا أحد ولا أربعاء ولا جمعة")
# apl-source:54
print("روش 5786 يوم رقم:", رأس_سنة(5786))
# apl-source:55
