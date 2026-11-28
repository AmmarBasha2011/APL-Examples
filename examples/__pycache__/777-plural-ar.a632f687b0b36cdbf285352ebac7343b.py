
# apl-source:1
# مثال 777 — فئات الجمع العربية
# apl-source:2
# Arabic plural categories
# apl-source:3
# Demonstrates: CLDR، ست فئات، الباقي من 100
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/777-plural-ar.apl
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
# قواعد الجمع العربية حسب CLDR: ست فئات
# apl-source:25
# Demonstrates: zero/one/two/few/many/other, الباقي من 100
# apl-source:26

# apl-source:27
def فئة_عدد(ن):
  # apl-source:28
  if ن == 0:
    # apl-source:29
    return "صفر"
  # apl-source:30
  if ن == 1:
    # apl-source:31
    return "مفرد"
  # apl-source:32
  if ن == 2:
    # apl-source:33
    return "مثنى"
  # apl-source:34
  باقي = ن % 100
  # apl-source:35
  if باقي >= 3 and باقي <= 10:
    # apl-source:36
    return "قلة"
  # apl-source:37
  if باقي >= 11 and باقي <= 99:
    # apl-source:38
    return "كثرة"
  # apl-source:39
  return "أخرى"
# apl-source:40

# apl-source:41
def صيغة_كتاب(ن):
  # apl-source:42
  فئة = فئة_عدد(ن)
  # apl-source:43
  if فئة == "صفر":
    # apl-source:44
    return "لا كتب"
  # apl-source:45
  if فئة == "مفرد":
    # apl-source:46
    return "كتاب واحد"
  # apl-source:47
  if فئة == "مثنى":
    # apl-source:48
    return "كتابان"
  # apl-source:49
  if فئة == "قلة":
    # apl-source:50
    return str(ن) + " كتب"
  # apl-source:51
  if فئة == "كثرة":
    # apl-source:52
    return str(ن) + " كتاباً"
  # apl-source:53
  return str(ن) + " كتاب"
# apl-source:54

# apl-source:55
تأكد_يساوي(فئة_عدد(0), "صفر", "صفر")
# apl-source:56
تأكد_يساوي(فئة_عدد(1), "مفرد", "واحد")
# apl-source:57
تأكد_يساوي(فئة_عدد(2), "مثنى", "اثنان")
# apl-source:58
تأكد_يساوي(فئة_عدد(3), "قلة", "ثلاثة")
# apl-source:59
تأكد_يساوي(فئة_عدد(10), "قلة", "عشرة")
# apl-source:60
تأكد_يساوي(فئة_عدد(11), "كثرة", "أحد عشر")
# apl-source:61
تأكد_يساوي(فئة_عدد(99), "كثرة", "تسعة وتسعون")
# apl-source:62
تأكد_يساوي(فئة_عدد(100), "أخرى", "مئة")
# apl-source:63
تأكد_يساوي(فئة_عدد(102), "أخرى", "مئة واثنان")
# apl-source:64
تأكد_يساوي(فئة_عدد(111), "كثرة", "مئة وأحد عشر")
# apl-source:65
تأكد_يساوي(فئة_عدد(1000), "أخرى", "ألف")
# apl-source:66
تأكد_يساوي(صيغة_كتاب(2), "كتابان", "صيغة المثنى")
# apl-source:67
تأكد_يساوي(صيغة_كتاب(5), "5 كتب", "صيغة القلة")
# apl-source:68
تأكد_يساوي(صيغة_كتاب(25), "25 كتاباً", "صيغة الكثرة")
# apl-source:69
