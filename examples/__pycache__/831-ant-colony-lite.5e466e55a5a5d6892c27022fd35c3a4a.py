
# apl-source:1
# مثال 831 — مستعمرة النمل
# apl-source:2
# Ant colony
# apl-source:3
# Demonstrates: فرمون وتبخير، اختيار احتمالي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/831-ant-colony-lite.apl
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
# مستعمرة نمل لأقصر جولة: فرمون يتبخر ويتراكم على الجولات الجيدة
# apl-source:25
# Demonstrates: اختيار احتمالي بفرمون ومرشد, تبخير وترسيب, LCG حتمي
# apl-source:26

# apl-source:27
مسافات = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
# apl-source:28

# apl-source:29
def مستعمرة(دورات):
  # apl-source:30
  فرمون = []
  # apl-source:31
  for ي in range(4):
    # apl-source:32
    صف = []
    # apl-source:33
    for ج in range(4):
      # apl-source:34
      صف.append(1.0)
    # apl-source:35
    فرمون.append(صف)
  # apl-source:36
  بذرة = 12345
  # apl-source:37
  أفضل = []
  # apl-source:38
  أقصر = 1000000.0
  # apl-source:39
  for دورة in range(دورات):
    # apl-source:40
    for نملة in range(4):
      # apl-source:41
      مزار = [نملة % 4]
      # apl-source:42
      while len(مزار) < 4:
        # apl-source:43
        حالي = مزار[len(مزار) - 1]
        # apl-source:44
        احتمالات = []
        # apl-source:45
        for ج in range(4):
          # apl-source:46
          if ج in مزار:
            # apl-source:47
            احتمالات.append(0.0)
          # apl-source:48
          else:
            # apl-source:49
            احتمالات.append(فرمون[حالي][ج] / مسافات[حالي][ج])
        # apl-source:50
        مجموع = 0.0
        # apl-source:51
        for ح in احتمالات:
          # apl-source:52
          مجموع = مجموع + ح
        # apl-source:53
        بذرة = (بذرة * 1103515245 + 12345) % 2147483648
        # apl-source:54
        قرعة = بذرة / 2147483648.0 * مجموع
        # apl-source:55
        تراكم = 0.0
        # apl-source:56
        اختير = -1
        # apl-source:57
        for ج in range(4):
          # apl-source:58
          if اختير == -1:
            # apl-source:59
            تراكم = تراكم + احتمالات[ج]
            # apl-source:60
            if قرعة <= تراكم:
              # apl-source:61
              اختير = ج
        # apl-source:62
        if اختير == -1:
          # apl-source:63
          اختير = 0
          # apl-source:64
          for ج in range(1, 4):
            # apl-source:65
            if احتمالات[ج] > احتمالات[اختير]:
              # apl-source:66
              اختير = ج
        # apl-source:67
        مزار.append(اختير)
      # apl-source:68
      طول_جولة = 0
      # apl-source:69
      for ي in range(4):
        # apl-source:70
        طول_جولة = طول_جولة + مسافات[مزار[ي]][مزار[(ي + 1) % 4]]
      # apl-source:71
      if طول_جولة < أقصر:
        # apl-source:72
        أقصر = طول_جولة * 1.0
        # apl-source:73
        أفضل = []
        # apl-source:74
        for عقدة in مزار:
          # apl-source:75
          أفضل.append(عقدة)
    # apl-source:76
    for ي in range(4):
      # apl-source:77
      for ج in range(4):
        # apl-source:78
        فرمون[ي][ج] = فرمون[ي][ج] * 0.5
    # apl-source:79
    for ي in range(4):
      # apl-source:80
      فرمون[أفضل[ي]][أفضل[(ي + 1) % 4]] = فرمون[أفضل[ي]][أفضل[(ي + 1) % 4]] + 1.0 / أقصر
  # apl-source:81
  return [أفضل, أقصر]
# apl-source:82

# apl-source:83
نتيجة = مستعمرة(20)
# apl-source:84
تأكد_يساوي(نتيجة[0], [1, 0, 2, 3], "أفضل جولة")
# apl-source:85
تأكد_يساوي(نتيجة[1], 21.0, "أقصر طول")
# apl-source:86
نتيجة2 = مستعمرة(5)
# apl-source:87
تأكد_يساوي(نتيجة2[1] <= 27.0 == False, False, "خمس دورات تتعلم أيضاً")
# apl-source:88
