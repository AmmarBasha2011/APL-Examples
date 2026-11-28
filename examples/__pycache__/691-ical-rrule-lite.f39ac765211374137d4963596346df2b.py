
# apl-source:1
# مثال 691 — قاعدة تكرار iCalendar
# apl-source:2
# iCalendar RRULE lite
# apl-source:3
# Demonstrates: تكرار، فواصل، كبس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/691-ical-rrule-lite.apl
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
# قاعدة تكرار iCalendar مصغرة: FREQ و INTERVAL و COUNT
# apl-source:25
# Demonstrates: توليد مواعيد يومية وأسبوعية وشهرية, حساب أيام الشهور والكبس
# apl-source:26
# DTSTART=20240131 مع FREQ=MONTHLY يقفز فبراير لأن 31 غير موجود فيه
# apl-source:27

# apl-source:28
def كبيسة(سنة):
  # apl-source:29
  return (سنة % 4 == 0 and سنة % 100 != 0) or سنة % 400 == 0
# apl-source:30

# apl-source:31
def أيام_شهر(سنة, شهر):
  # apl-source:32
  أطوال = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:33
  if شهر == 2 and كبيسة(سنة):
    # apl-source:34
    return 29
  # apl-source:35
  return أطوال[شهر - 1]
# apl-source:36

# apl-source:37
def أضف_أيام(سنة, شهر, يوم, ن):
  # apl-source:38
  ي = يوم + ن
  # apl-source:39
  س = سنة
  # apl-source:40
  ش = شهر
  # apl-source:41
  while ي > أيام_شهر(س, ش):
    # apl-source:42
    ي = ي - أيام_شهر(س, ش)
    # apl-source:43
    ش = ش + 1
    # apl-source:44
    if ش > 12:
      # apl-source:45
      ش = 1
      # apl-source:46
      س = س + 1
  # apl-source:47
  return [س, ش, ي]
# apl-source:48

# apl-source:49
def أضف_شهور(سنة, شهر, يوم, ن):
  # apl-source:50
  ش = شهر + ن
  # apl-source:51
  س = سنة + (ش - 1) // 12
  # apl-source:52
  ش = (ش - 1) % 12 + 1
  # apl-source:53
  return [س, ش, يوم]
# apl-source:54

# apl-source:55
def صيغة(تاريخ):
  # apl-source:56
  س = str(تاريخ[0])
  # apl-source:57
  ش = str(تاريخ[1] + 100)[1:]
  # apl-source:58
  ي = str(تاريخ[2] + 100)[1:]
  # apl-source:59
  return س + "-" + ش + "-" + ي
# apl-source:60

# apl-source:61
def ولد(سنة, شهر, يوم, تردد, فاصل, عدد):
  # apl-source:62
  مواعيد = []
  # apl-source:63
  حالي = [سنة, شهر, يوم]
  # apl-source:64
  for ي in range(عدد * 40):
    # apl-source:65
    if len(مواعيد) >= عدد:
      # apl-source:66
      return مواعيد
    # apl-source:67
    صالح = True
    # apl-source:68
    if تردد == "MONTHLY" and حالي[2] > أيام_شهر(حالي[0], حالي[1]):
      # apl-source:69
      صالح = False
    # apl-source:70
    if صالح:
      # apl-source:71
      مواعيد.append(صيغة(حالي))
    # apl-source:72
    if تردد == "DAILY":
      # apl-source:73
      حالي = أضف_أيام(حالي[0], حالي[1], حالي[2], فاصل)
    # apl-source:74
    elif تردد == "WEEKLY":
      # apl-source:75
      حالي = أضف_أيام(حالي[0], حالي[1], حالي[2], 7 * فاصل)
    # apl-source:76
    else:
      # apl-source:77
      حالي = أضف_شهور(حالي[0], حالي[1], حالي[2], فاصل)
  # apl-source:78
  return مواعيد
# apl-source:79

# apl-source:80
يومي = ولد(2024, 1, 1, "DAILY", 1, 5)
# apl-source:81
تأكد_يساوي(يومي, ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"], "خمسة أيام")
# apl-source:82
أسبوعي = ولد(2024, 1, 1, "WEEKLY", 1, 3)
# apl-source:83
تأكد_يساوي(أسبوعي, ["2024-01-01", "2024-01-08", "2024-01-15"], "ثلاثة أسابيع")
# apl-source:84
كبس = ولد(2024, 2, 28, "DAILY", 1, 3)
# apl-source:85
تأكد_يساوي(كبس, ["2024-02-28", "2024-02-29", "2024-03-01"], "فبراير الكبيس")
# apl-source:86
شهري = ولد(2024, 1, 31, "MONTHLY", 1, 4)
# apl-source:87
تأكد_يساوي(شهري, ["2024-01-31", "2024-03-31", "2024-05-31", "2024-07-31"], "الشهور التي فيها 31 فقط")
# apl-source:88
فاصل2 = ولد(2024, 1, 1, "DAILY", 3, 3)
# apl-source:89
تأكد_يساوي(فاصل2, ["2024-01-01", "2024-01-04", "2024-01-07"], "كل ثلاثة أيام")
# apl-source:90
print("شهري:", شهري)
# apl-source:91
