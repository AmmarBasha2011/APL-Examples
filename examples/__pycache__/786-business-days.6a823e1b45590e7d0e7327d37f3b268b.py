
# apl-source:1
# مثال 786 — أيام العمل
# apl-source:2
# Business days
# apl-source:3
# Demonstrates: أيام-من-ميلادي، عطلات رسمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/786-business-days.apl
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
# أيام العمل بين تاريخين: استبعاد الجمعة والسبت والعطلات الرسمية
# apl-source:25
# Demonstrates: خوارزمية أيام-من-ميلادي, حساب يوم الأسبوع, قائمة عطلات
# apl-source:26

# apl-source:27
def تسلسلي(سنة, شهر, يوم):
  # apl-source:28
  س = سنة
  # apl-source:29
  if شهر <= 2:
    # apl-source:30
    س = س - 1
  # apl-source:31
  حقبة = س // 400
  # apl-source:32
  سنة_حقبة = س - حقبة * 400
  # apl-source:33
  if شهر > 2:
    # apl-source:34
    م = شهر - 3
  # apl-source:35
  else:
    # apl-source:36
    م = شهر + 9
  # apl-source:37
  يوم_سنة = (153 * م + 2) // 5 + يوم - 1
  # apl-source:38
  يوم_حقبة = سنة_حقبة * 365 + سنة_حقبة // 4 - سنة_حقبة // 100 + يوم_سنة
  # apl-source:39
  return حقبة * 146097 + يوم_حقبة - 719468
# apl-source:40

# apl-source:41
def يوم_اسبوع(سنة, شهر, يوم):
  # apl-source:42
  return (تسلسلي(سنة, شهر, يوم) + 3) % 7
# apl-source:43

# apl-source:44
def في_عطلات(شهر, يوم, عطلات):
  # apl-source:45
  for ع in عطلات:
    # apl-source:46
    if ع[0] == شهر and ع[1] == يوم:
      # apl-source:47
      return True
  # apl-source:48
  return False
# apl-source:49

# apl-source:50
def أيام_عمل(س1, ش1, ي1, س2, ش2, ي2, عطلات):
  # apl-source:51
  ت1 = تسلسلي(س1, ش1, ي1)
  # apl-source:52
  ت2 = تسلسلي(س2, ش2, ي2)
  # apl-source:53
  عد = 0
  # apl-source:54
  ت = ت1
  # apl-source:55
  while ت < ت2:
    # apl-source:56
    ت = ت + 1
    # apl-source:57
    أسبوعي = (ت + 3) % 7
    # apl-source:58
    if أسبوعي != 4 and أسبوعي != 5:
      # apl-source:59
      عد = عد + 1
  # apl-source:60
  return عد
# apl-source:61

# apl-source:62
def من_تسلسلي(ت):
  # apl-source:63
  ز = ت + 719468
  # apl-source:64
  حقبة = ز // 146097
  # apl-source:65
  يوم_حقبة = ز - حقبة * 146097
  # apl-source:66
  سنة_حقبة = (يوم_حقبة - يوم_حقبة // 1460 + يوم_حقبة // 36524 - يوم_حقبة // 146096) // 365
  # apl-source:67
  سنة = سنة_حقبة + حقبة * 400
  # apl-source:68
  باقي_سنة = يوم_حقبة - (365 * سنة_حقبة + سنة_حقبة // 4 - سنة_حقبة // 100)
  # apl-source:69
  م_أولي = (5 * باقي_سنة + 2) // 153
  # apl-source:70
  يوم = باقي_سنة - (153 * م_أولي + 2) // 5 + 1
  # apl-source:71
  if م_أولي < 10:
    # apl-source:72
    شهر = م_أولي + 3
  # apl-source:73
  else:
    # apl-source:74
    شهر = م_أولي - 9
  # apl-source:75
  if شهر <= 2:
    # apl-source:76
    سنة = سنة + 1
  # apl-source:77
  return [سنة, شهر, يوم]
# apl-source:78

# apl-source:79
def أيام_عمل_بعطلات(س1, ش1, ي1, س2, ش2, ي2, عطلات):
  # apl-source:80
  ت1 = تسلسلي(س1, ش1, ي1)
  # apl-source:81
  ت2 = تسلسلي(س2, ش2, ي2)
  # apl-source:82
  عد = 0
  # apl-source:83
  ت = ت1
  # apl-source:84
  while ت < ت2:
    # apl-source:85
    ت = ت + 1
    # apl-source:86
    أسبوعي = (ت + 3) % 7
    # apl-source:87
    if أسبوعي != 4 and أسبوعي != 5:
      # apl-source:88
      تاريخ = من_تسلسلي(ت)
      # apl-source:89
      if في_عطلات(تاريخ[1], تاريخ[2], عطلات) == False:
        # apl-source:90
        عد = عد + 1
  # apl-source:91
  return عد
# apl-source:92

# apl-source:93
تأكد_يساوي(يوم_اسبوع(2026, 1, 1), 3, "أول يناير 2026 خميس")
# apl-source:94
تأكد_يساوي(يوم_اسبوع(2000, 9, 9), 5, "9 سبتمبر 2000 سبت")
# apl-source:95
تأكد_يساوي(أيام_عمل(2026, 1, 1, 2026, 1, 15, []), 10, "عشرة أيام عمل")
# apl-source:96
تأكد_يساوي(أيام_عمل(2026, 1, 2, 2026, 1, 4, []), 1, "أحد العمل بعد جمعة وسبت")
# apl-source:97
تأكد_يساوي(أيام_عمل_بعطلات(2026, 1, 1, 2026, 1, 15, [[1, 7]]), 9, "مع عطلة 7 يناير")
# apl-source:98
عكس = من_تسلسلي(تسلسلي(2000, 2, 29))
# apl-source:99
تأكد_يساوي(عكس[0], 2000, "تحويل عكسي سنة")
# apl-source:100
تأكد_يساوي(عكس[1], 2, "تحويل عكسي شهر")
# apl-source:101
تأكد_يساوي(عكس[2], 29, "تحويل عكسي يوم")
# apl-source:102
تأكد_يساوي(أيام_عمل(2026, 3, 1, 2026, 3, 8, []), 5, "أسبوع كامل")
# apl-source:103
