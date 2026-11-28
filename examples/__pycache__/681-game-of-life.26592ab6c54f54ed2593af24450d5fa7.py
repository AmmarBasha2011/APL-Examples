
# apl-source:1
# مثال 681 — لعبة الحياة
# apl-source:2
# Game of Life
# apl-source:3
# Demonstrates: أتمتة خلوية، قواعد B3/S23، مذبذبات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/681-game-of-life.apl
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
# لعبة الحياة لكونواي على شبكة محدودة
# apl-source:25
# Demonstrates: قواعد الولادة والبقاء B3/S23, عد الجيران, مذبذب ونمط ساكن
# apl-source:26
# الخلايا خارج الشبكة ميتة دائما
# apl-source:27

# apl-source:28
def شبكة_فارغة(صفوف, أعمدة):
  # apl-source:29
  شبكة = []
  # apl-source:30
  for ي in range(صفوف):
    # apl-source:31
    صف = []
    # apl-source:32
    for ج in range(أعمدة):
      # apl-source:33
      صف.append(0)
    # apl-source:34
    شبكة.append(صف)
  # apl-source:35
  return شبكة
# apl-source:36

# apl-source:37
def جيران_أحياء(شبكة, ص, ع, صفوف, أعمدة):
  # apl-source:38
  عدد = 0
  # apl-source:39
  for دص in range(-1, 2):
    # apl-source:40
    for دع in range(-1, 2):
      # apl-source:41
      if دص == 0 and دع == 0:
        # apl-source:42
        عدد = عدد + 0
      # apl-source:43
      else:
        # apl-source:44
        ص2 = ص + دص
        # apl-source:45
        ع2 = ع + دع
        # apl-source:46
        if ص2 >= 0 and ص2 < صفوف and ع2 >= 0 and ع2 < أعمدة:
          # apl-source:47
          عدد = عدد + شبكة[ص2][ع2]
  # apl-source:48
  return عدد
# apl-source:49

# apl-source:50
def خطوة(شبكة, صفوف, أعمدة):
  # apl-source:51
  جديدة = شبكة_فارغة(صفوف, أعمدة)
  # apl-source:52
  for ص in range(صفوف):
    # apl-source:53
    for ع in range(أعمدة):
      # apl-source:54
      ج = جيران_أحياء(شبكة, ص, ع, صفوف, أعمدة)
      # apl-source:55
      if شبكة[ص][ع] == 1:
        # apl-source:56
        if ج == 2 or ج == 3:
          # apl-source:57
          جديدة[ص][ع] = 1
      # apl-source:58
      else:
        # apl-source:59
        if ج == 3:
          # apl-source:60
          جديدة[ص][ع] = 1
  # apl-source:61
  return جديدة
# apl-source:62

# apl-source:63
def عدد_أحياء(شبكة, صفوف, أعمدة):
  # apl-source:64
  عدد = 0
  # apl-source:65
  for ص in range(صفوف):
    # apl-source:66
    for ع in range(أعمدة):
      # apl-source:67
      عدد = عدد + شبكة[ص][ع]
  # apl-source:68
  return عدد
# apl-source:69

# apl-source:70
# المومياء (مذبذب بدورية 2)
# apl-source:71
وميض = شبكة_فارغة(5, 5)
# apl-source:72
وميض[2][1] = 1
# apl-source:73
وميض[2][2] = 1
# apl-source:74
وميض[2][3] = 1
# apl-source:75
بعد1 = خطوة(وميض, 5, 5)
# apl-source:76
تأكد_يساوي(بعد1[1][2], 1, "الموميض يدور عموديا 1")
# apl-source:77
تأكد_يساوي(بعد1[2][2], 1, "الموميض يدور عموديا 2")
# apl-source:78
تأكد_يساوي(بعد1[3][2], 1, "الموميض يدور عموديا 3")
# apl-source:79
تأكد_يساوي(بعد1[2][1], 0, "الأفقي اختفى 1")
# apl-source:80
تأكد_يساوي(بعد1[2][3], 0, "الأفقي اختفى 2")
# apl-source:81
بعد2 = خطوة(بعد1, 5, 5)
# apl-source:82
تأكد_يساوي(بعد2[2][1] + بعد2[2][2] + بعد2[2][3], 3, "الموميض يعود أفقيا بعد خطوتين")
# apl-source:83

# apl-source:84
# الكتلة نمط ساكن
# apl-source:85
كتلة = شبكة_فارغة(4, 4)
# apl-source:86
كتلة[1][1] = 1
# apl-source:87
كتلة[1][2] = 1
# apl-source:88
كتلة[2][1] = 1
# apl-source:89
كتلة[2][2] = 1
# apl-source:90
كتلة2 = خطوة(كتلة, 4, 4)
# apl-source:91
تأكد_يساوي(عدد_أحياء(كتلة2, 4, 4), 4, "الكتلة ساكنة")
# apl-source:92
print("أحياء الموميض:", عدد_أحياء(بعد1, 5, 5))
# apl-source:93
