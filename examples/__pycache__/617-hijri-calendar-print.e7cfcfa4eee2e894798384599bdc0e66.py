
# apl-source:1
# مثال 617 — طباعة شهر هجري
# apl-source:2
# Hijri month print
# apl-source:3
# Demonstrates: هجري، شبكة أسابيع، أطوال شهور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/617-hijri-calendar-print.apl
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
# طباعة شهر هجري كشبكة أسابيع
# apl-source:25
# Demonstrates: التقويم الهجري الاصطلاحي, أطوال الشهور, شبكة طباعة
# apl-source:26
# السنة الهجرية 354 أو 355 يوما في دورة ثلاثينية
# apl-source:27

# apl-source:28
أشهر = ["محرم", "صفر", "ربيع الأول", "ربيع الآخر", "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"]
# apl-source:29

# apl-source:30
def كبيسة(سنة):
  # apl-source:31
  return سنة % 30 in [2, 5, 7, 10, 13, 16, 18, 21, 24, 26, 29]
# apl-source:32

# apl-source:33
def طول_شهر(سنة, شهر):
  # apl-source:34
  if شهر % 2 == 1:
    # apl-source:35
    return 30
  # apl-source:36
  if شهر == 12 and كبيسة(سنة):
    # apl-source:37
    return 30
  # apl-source:38
  return 29
# apl-source:39

# apl-source:40
def طول_سنة(سنة):
  # apl-source:41
  if كبيسة(سنة):
    # apl-source:42
    return 355
  # apl-source:43
  return 354
# apl-source:44

# apl-source:45
print("شبكة رمضان 1447 (بداية افتراضية: سبت):")
# apl-source:46
إزاحة = 0
# apl-source:47
سطر = ""
# apl-source:48
for فراغ in range(إزاحة):
  # apl-source:49
  سطر = سطر + "    "
# apl-source:50
for يوم in range(1, طول_شهر(1447, 9) + 1):
  # apl-source:51
  نص_يوم = str(يوم)
  # apl-source:52
  while len(نص_يوم) < 3:
    # apl-source:53
    نص_يوم = " " + نص_يوم
  # apl-source:54
  سطر = سطر + نص_يوم + " "
  # apl-source:55
  if (يوم + إزاحة) % 7 == 0:
    # apl-source:56
    print(سطر)
    # apl-source:57
    سطر = ""
# apl-source:58
if سطر != "":
  # apl-source:59
  print(سطر)
# apl-source:60

# apl-source:61
تأكد_يساوي(طول_شهر(1447, 9), 30, "رمضان 30 في الاصطلاحي")
# apl-source:62
تأكد_يساوي(طول_سنة(1446), 354, "1446 سنة بسيطة")
# apl-source:63
تأكد_يساوي(كبيسة(1447), True, "1447 سنة كبيسة")
# apl-source:64
تأكد_يساوي(طول_سنة(1447), 355, "1447 فيها 355 يوما")
# apl-source:65
تأكد_يساوي(len(أشهر), 12, "اثنا عشر شهرا")
# apl-source:66
