
# apl-source:1
# مثال 618 — العد التنازلي لرمضان
# apl-source:2
# Ramadan countdown
# apl-source:3
# Demonstrates: رمضان، دورة ثلاثينية، فرق تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/618-ramadan-countdown.apl
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
# العد التنازلي لرمضان بالتقويم الاصطلاحي
# apl-source:25
# Demonstrates: تحويل هجري إلى أيام مطلقة, فرق تواريخ, دورة 30 سنة
# apl-source:26
# يحسب الأيام المتبقية حتى أول رمضان من أي تاريخ هجري
# apl-source:27

# apl-source:28
def كبيسة(سنة):
  # apl-source:29
  return سنة % 30 in [2, 5, 7, 10, 13, 16, 18, 21, 24, 26, 29]
# apl-source:30

# apl-source:31
def أيام_حتى_سنة(سنة):
  # apl-source:32
  دورات = (سنة - 1) // 30
  # apl-source:33
  باقي = (سنة - 1) % 30
  # apl-source:34
  مجموع = دورات * 10631
  # apl-source:35
  for س in range(1, باقي + 1):
    # apl-source:36
    if كبيسة(س):
      # apl-source:37
      مجموع = مجموع + 355
    # apl-source:38
    else:
      # apl-source:39
      مجموع = مجموع + 354
  # apl-source:40
  return مجموع
# apl-source:41

# apl-source:42
def طول_شهر(سنة, شهر):
  # apl-source:43
  if شهر % 2 == 1:
    # apl-source:44
    return 30
  # apl-source:45
  if شهر == 12 and كبيسة(سنة):
    # apl-source:46
    return 30
  # apl-source:47
  return 29
# apl-source:48

# apl-source:49
def رقم_مطلق(سنة, شهر, يوم):
  # apl-source:50
  مجموع = أيام_حتى_سنة(سنة) + يوم - 1
  # apl-source:51
  for م in range(1, شهر):
    # apl-source:52
    مجموع = مجموع + طول_شهر(سنة, م)
  # apl-source:53
  return مجموع
# apl-source:54

# apl-source:55
def متبقي_لرمضان(سنة, شهر, يوم):
  # apl-source:56
  if شهر <= 9:
    # apl-source:57
    هدف = رقم_مطلق(سنة, 9, 1)
  # apl-source:58
  else:
    # apl-source:59
    هدف = رقم_مطلق(سنة + 1, 9, 1)
  # apl-source:60
  return هدف - رقم_مطلق(سنة, شهر, يوم)
# apl-source:61

# apl-source:62
تأكد_يساوي(متبقي_لرمضان(1447, 9, 1), 0, "أول رمضان نفسه")
# apl-source:63
تأكد_يساوي(متبقي_لرمضان(1447, 8, 1), 29, "شعبان 29 قبل رمضان")
# apl-source:64
تأكد_يساوي(متبقي_لرمضان(1447, 1, 1), 236, "من أول محرم")
# apl-source:65
بعد_رمضان = متبقي_لرمضان(1447, 10, 1)
# apl-source:66
print("من أول شوال إلى رمضان التالي:", بعد_رمضان)
# apl-source:67
تأكد_يساوي(بعد_رمضان, 325, "من شوال إلى رمضان 1448")
# apl-source:68
