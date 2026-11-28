
# apl-source:1
# مثال 774 — الفرز الطبيعي
# apl-source:2
# Natural sort
# apl-source:3
# Demonstrates: مقاطع رقمية، مقارنة كأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/774-natural-sort.apl
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
# الفرز الطبيعي: img2 قبل img10
# apl-source:25
# Demonstrates: تقسيم النص إلى مقاطع رقمية ونصية, مقارنة المقاطع الرقمية كأعداد
# apl-source:26

# apl-source:27
def كلها_ارقام(س):
  # apl-source:28
  نتيجة = True
  # apl-source:29
  for حرف in س:
    # apl-source:30
    if حرف < "0" or حرف > "9":
      # apl-source:31
      نتيجة = False
  # apl-source:32
  return نتيجة
# apl-source:33

# apl-source:34
def مفاتيح_طبيعية(نص):
  # apl-source:35
  أجزاء = []
  # apl-source:36
  حالي = ""
  # apl-source:37
  رقمي = False
  # apl-source:38
  for حرف in نص:
    # apl-source:39
    if حرف >= "0" and حرف <= "9":
      # apl-source:40
      هو_رقم = True
    # apl-source:41
    else:
      # apl-source:42
      هو_رقم = False
    # apl-source:43
    if len(حالي) > 0 and هو_رقم != رقمي:
      # apl-source:44
      أجزاء.append(حالي)
      # apl-source:45
      حالي = ""
    # apl-source:46
    حالي = حالي + حرف
    # apl-source:47
    رقمي = هو_رقم
  # apl-source:48
  if len(حالي) > 0:
    # apl-source:49
    أجزاء.append(حالي)
  # apl-source:50
  return أجزاء
# apl-source:51

# apl-source:52
def اصغر_طبيعي(أ, ب):
  # apl-source:53
  كأ = مفاتيح_طبيعية(أ)
  # apl-source:54
  كب = مفاتيح_طبيعية(ب)
  # apl-source:55
  ن = len(كأ)
  # apl-source:56
  if len(كب) < ن:
    # apl-source:57
    ن = len(كب)
  # apl-source:58
  for ي in range(ن):
    # apl-source:59
    جزءأ = كأ[ي]
    # apl-source:60
    جزءب = كب[ي]
    # apl-source:61
    if كلها_ارقام(جزءأ) and كلها_ارقام(جزءب):
      # apl-source:62
      if int(جزءأ) < int(جزءب):
        # apl-source:63
        return True
      # apl-source:64
      if int(جزءأ) > int(جزءب):
        # apl-source:65
        return False
    # apl-source:66
    else:
      # apl-source:67
      if جزءأ < جزءب:
        # apl-source:68
        return True
      # apl-source:69
      if جزءأ > جزءب:
        # apl-source:70
        return False
  # apl-source:71
  return len(كأ) < len(كب)
# apl-source:72

# apl-source:73
def فرز_طبيعي(عناصر):
  # apl-source:74
  ن = len(عناصر)
  # apl-source:75
  for ي in range(ن):
    # apl-source:76
    ادنى = ي
    # apl-source:77
    for ج in range(ي + 1, ن):
      # apl-source:78
      if اصغر_طبيعي(عناصر[ج], عناصر[ادنى]):
        # apl-source:79
        ادنى = ج
    # apl-source:80
    مؤقت = عناصر[ي]
    # apl-source:81
    عناصر[ي] = عناصر[ادنى]
    # apl-source:82
    عناصر[ادنى] = مؤقت
  # apl-source:83
  return عناصر
# apl-source:84

# apl-source:85
م = فرز_طبيعي(["img12", "img2", "img1", "a10", "a2"])
# apl-source:86
تأكد_يساوي(م[0], "a2", "الأول")
# apl-source:87
تأكد_يساوي(م[1], "a10", "الثاني")
# apl-source:88
تأكد_يساوي(م[2], "img1", "الثالث")
# apl-source:89
تأكد_يساوي(م[3], "img2", "الرابع")
# apl-source:90
تأكد_يساوي(م[4], "img12", "الخامس")
# apl-source:91
ن = فرز_طبيعي(["x10y2", "x10y10", "x9"])
# apl-source:92
تأكد_يساوي(ن[0], "x9", "مقاطع متعددة 1")
# apl-source:93
تأكد_يساوي(ن[1], "x10y2", "مقاطع متعددة 2")
# apl-source:94
تأكد_يساوي(ن[2], "x10y10", "مقاطع متعددة 3")
# apl-source:95
