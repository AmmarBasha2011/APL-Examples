
# apl-source:1
# مثال 788 — خوارزمية جينية
# apl-source:2
# Genetic algorithm
# apl-source:3
# Demonstrates: انتقاء، عبور، طفرة، LCG حتمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/788-genetic-algorithm.apl
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
# خوارزمية جينية لمشكلة Ones-Max: انتقاء، عبور، طفرة
# apl-source:25
# Demonstrates: مولد عشوائي LCG حتمي, لياقة, نخبة, عبور نقطة واحدة
# apl-source:26

# apl-source:27
def اهتزاز(حالة):
  # apl-source:28
  return (حالة * 1103515245 + 12345) % 2147483648
# apl-source:29

# apl-source:30
def لياقة(فرد):
  # apl-source:31
  واحدات = 0
  # apl-source:32
  for جين in فرد:
    # apl-source:33
    واحدات = واحدات + جين
  # apl-source:34
  return واحدات
# apl-source:35

# apl-source:36
def خوارزمية_جينية(بذرة, حجم, طول_كروموسوم, أجيال):
  # apl-source:37
  حالة = بذرة
  # apl-source:38
  سكان = []
  # apl-source:39
  for ي in range(حجم):
    # apl-source:40
    فرد = []
    # apl-source:41
    for ج in range(طول_كروموسوم):
      # apl-source:42
      حالة = اهتزاز(حالة)
      # apl-source:43
      فرد.append(حالة % 2)
    # apl-source:44
    سكان.append(فرد)
  # apl-source:45
  for جيل in range(أجيال):
    # apl-source:46
    for ي in range(حجم):
      # apl-source:47
      افضل = ي
      # apl-source:48
      for ج in range(ي + 1, حجم):
        # apl-source:49
        if لياقة(سكان[ج]) > لياقة(سكان[افضل]):
          # apl-source:50
          افضل = ج
      # apl-source:51
      مؤقت = سكان[ي]
      # apl-source:52
      سكان[ي] = سكان[افضل]
      # apl-source:53
      سكان[افضل] = مؤقت
    # apl-source:54
    if لياقة(سكان[0]) == طول_كروموسوم:
      # apl-source:55
      return [جيل, لياقة(سكان[0])]
    # apl-source:56
    جدد = [سكان[0], سكان[1]]
    # apl-source:57
    while len(جدد) < حجم:
      # apl-source:58
      حالة = اهتزاز(حالة)
      # apl-source:59
      أ = سكان[حالة % 10]
      # apl-source:60
      حالة = اهتزاز(حالة)
      # apl-source:61
      ب = سكان[حالة % 10]
      # apl-source:62
      حالة = اهتزاز(حالة)
      # apl-source:63
      قطع = 1 + حالة % (طول_كروموسوم - 1)
      # apl-source:64
      طفل = []
      # apl-source:65
      for ج in range(قطع):
        # apl-source:66
        طفل.append(أ[ج])
      # apl-source:67
      for ج in range(قطع, طول_كروموسوم):
        # apl-source:68
        طفل.append(ب[ج])
      # apl-source:69
      طفل_مطفر = []
      # apl-source:70
      for جين in طفل:
        # apl-source:71
        حالة = اهتزاز(حالة)
        # apl-source:72
        if حالة % 100 < 5:
          # apl-source:73
          طفل_مطفر.append(1 - جين)
        # apl-source:74
        else:
          # apl-source:75
          طفل_مطفر.append(جين)
      # apl-source:76
      جدد.append(طفل_مطفر)
    # apl-source:77
    سكان = جدد
  # apl-source:78
  return [أجيال, لياقة(سكان[0])]
# apl-source:79

# apl-source:80
ن = خوارزمية_جينية(7, 20, 16, 50)
# apl-source:81
تأكد_يساوي(ن[1], 16, "لياقة كاملة")
# apl-source:82
تأكد_يساوي(ن[0], 14, "التقارب في الجيل 14")
# apl-source:83
ن2 = خوارزمية_جينية(7, 20, 16, 50)
# apl-source:84
تأكد_يساوي(ن2[0], ن[0], "حتمية التكرار")
# apl-source:85
تأكد_يساوي(لياقة([1, 0, 1, 1]), 3, "لياقة بسيطة")
# apl-source:86
