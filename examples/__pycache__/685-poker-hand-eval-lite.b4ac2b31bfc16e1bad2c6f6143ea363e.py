
# apl-source:1
# مثال 685 — تقييم يد بوكر
# apl-source:2
# Poker hand evaluator lite
# apl-source:3
# Demonstrates: فئات، متوالي، عجلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/685-poker-hand-eval-lite.apl
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
# تقييم يد بوكر من خمس ورقات (فئة فقط)
# apl-source:25
# Demonstrates: عد التكرارات, كشف المتوالي والملون, العجلة A2345
# apl-source:26
# 8=ستريت فلش 7=أربعة 6=فول هاوس 5=فلش 4=ستريت 3=ثلاثية 2=زوجان 1=زوج 0=ورقة عالية
# apl-source:27

# apl-source:28
def قيمة_رتبة(ح):
  # apl-source:29
  حروف = "23456789TJQKA"
  # apl-source:30
  for ي in range(len(حروف)):
    # apl-source:31
    if حروف[ي] == ح:
      # apl-source:32
      return ي + 2
  # apl-source:33
  return 0
# apl-source:34

# apl-source:35
def فئة(يد):
  # apl-source:36
  قيم = []
  # apl-source:37
  for ورقة in يد:
    # apl-source:38
    قيم.append(قيمة_رتبة(ورقة[0]))
  # apl-source:39
  عداد = []
  # apl-source:40
  for ي in range(15):
    # apl-source:41
    عداد.append(0)
  # apl-source:42
  for ق in قيم:
    # apl-source:43
    عداد[ق] = عداد[ق] + 1
  # apl-source:44
  ملون = True
  # apl-source:45
  for ي in range(1, 5):
    # apl-source:46
    if يد[ي][1] != يد[0][1]:
      # apl-source:47
      ملون = False
  # apl-source:48
  أصغر = 99
  # apl-source:49
  أكبر = 0
  # apl-source:50
  مميزة = []
  # apl-source:51
  for ق in قيم:
    # apl-source:52
    if ق < أصغر:
      # apl-source:53
      أصغر = ق
    # apl-source:54
    if ق > أكبر:
      # apl-source:55
      أكبر = ق
    # apl-source:56
    if (ق in مميزة) == False:
      # apl-source:57
      مميزة.append(ق)
  # apl-source:58
  متوالي = False
  # apl-source:59
  if len(مميزة) == 5 and أكبر - أصغر == 4:
    # apl-source:60
    متوالي = True
  # apl-source:61
  عجلة = True
  # apl-source:62
  for ق in [14, 2, 3, 4, 5]:
    # apl-source:63
    if (ق in قيم) == False:
      # apl-source:64
      عجلة = False
  # apl-source:65
  if متوالي == False and عجلة:
    # apl-source:66
    متوالي = True
  # apl-source:67
  if ملون and متوالي:
    # apl-source:68
    return 8
  # apl-source:69
  if 4 in عداد:
    # apl-source:70
    return 7
  # apl-source:71
  if 3 in عداد and 2 in عداد:
    # apl-source:72
    return 6
  # apl-source:73
  if ملون:
    # apl-source:74
    return 5
  # apl-source:75
  if متوالي:
    # apl-source:76
    return 4
  # apl-source:77
  if 3 in عداد:
    # apl-source:78
    return 3
  # apl-source:79
  أزواج = 0
  # apl-source:80
  for ي in range(15):
    # apl-source:81
    if عداد[ي] == 2:
      # apl-source:82
      أزواج = أزواج + 1
  # apl-source:83
  if أزواج == 2:
    # apl-source:84
    return 2
  # apl-source:85
  if أزواج == 1:
    # apl-source:86
    return 1
  # apl-source:87
  return 0
# apl-source:88

# apl-source:89
تأكد_يساوي(فئة(["TH", "JH", "QH", "KH", "AH"]), 8, "ستريت فلش ملكي")
# apl-source:90
تأكد_يساوي(فئة(["9C", "9D", "9H", "9S", "2C"]), 7, "أربعة من نوع")
# apl-source:91
تأكد_يساوي(فئة(["3S", "3H", "3D", "7C", "7S"]), 6, "فول هاوس")
# apl-source:92
تأكد_يساوي(فئة(["2H", "5H", "8H", "JH", "KH"]), 5, "فلش")
# apl-source:93
تأكد_يساوي(فئة(["AS", "2D", "3H", "4C", "5S"]), 4, "عجلة متوالية")
# apl-source:94
تأكد_يساوي(فئة(["5S", "6D", "7H", "8C", "9S"]), 4, "ستريت عادي")
# apl-source:95
تأكد_يساوي(فئة(["QS", "QD", "QH", "4C", "9S"]), 3, "ثلاثية")
# apl-source:96
تأكد_يساوي(فئة(["JS", "JD", "8H", "8C", "3S"]), 2, "زوجان")
# apl-source:97
تأكد_يساوي(فئة(["7S", "7D", "KH", "2C", "9S"]), 1, "زوج واحد")
# apl-source:98
تأكد_يساوي(فئة(["2S", "5D", "9H", "JC", "KS"]), 0, "ورقة عالية")
# apl-source:99
print("فئة الفول هاوس:", فئة(["3S", "3H", "3D", "7C", "7S"]))
# apl-source:100
