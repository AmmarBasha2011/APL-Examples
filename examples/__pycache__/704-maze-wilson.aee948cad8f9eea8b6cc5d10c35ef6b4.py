
# apl-source:1
# مثال 704 — متاهة ويلسون
# apl-source:2
# Wilson's maze
# apl-source:3
# Demonstrates: مشي ممحى الحلقات، شجرة ممتدة، LCG
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/704-maze-wilson.apl
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
# متاهة مثالية بخوارزمية ويلسون (شجرة ممتدة منتظمة)
# apl-source:25
# Demonstrates: مشي عشوائي ممحى الحلقات, مولد LCG حتمي, شجرة
# apl-source:26
# البذرة ثابتة فتتولد نفس المتاهة دائما
# apl-source:27

# apl-source:28
def جيران(خلية, صفوف, أعمدة):
  # apl-source:29
  ص = خلية // أعمدة
  # apl-source:30
  ع2 = خلية % أعمدة
  # apl-source:31
  ناتج = []
  # apl-source:32
  if ص > 0:
    # apl-source:33
    ناتج.append(خلية - أعمدة)
  # apl-source:34
  if ص < صفوف - 1:
    # apl-source:35
    ناتج.append(خلية + أعمدة)
  # apl-source:36
  if ع2 > 0:
    # apl-source:37
    ناتج.append(خلية - 1)
  # apl-source:38
  if ع2 < أعمدة - 1:
    # apl-source:39
    ناتج.append(خلية + 1)
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
def ويلسون(صفوف, أعمدة, بذرة):
  # apl-source:43
  ن = صفوف * أعمدة
  # apl-source:44
  في_الشجرة = [False] * ن
  # apl-source:45
  حواف = []
  # apl-source:46
  ع = بذرة
  # apl-source:47
  في_الشجرة[0] = True
  # apl-source:48
  باقي = ن - 1
  # apl-source:49
  for بداية in range(1, ن):
    # apl-source:50
    if في_الشجرة[بداية]:
      # apl-source:51
      باقي = باقي
    # apl-source:52
    else:
      # apl-source:53
      مسار = [بداية]
      # apl-source:54
      حالية = بداية
      # apl-source:55
      while في_الشجرة[حالية] == False:
        # apl-source:56
        ج = جيران(حالية, صفوف, أعمدة)
        # apl-source:57
        ع = (ع * 1103515245 + 12345) % 2147483648
        # apl-source:58
        تالية = ج[ع % len(ج)]
        # apl-source:59
        if تالية in مسار:
          # apl-source:60
          موضع = مسار.index(تالية)
          # apl-source:61
          مسار = مسار[:موضع + 1]
        # apl-source:62
        else:
          # apl-source:63
          مسار.append(تالية)
        # apl-source:64
        حالية = تالية
      # apl-source:65
      for ي in range(len(مسار) - 1):
        # apl-source:66
        حواف.append([مسار[ي], مسار[ي + 1]])
        # apl-source:67
        في_الشجرة[مسار[ي]] = True
      # apl-source:68
      في_الشجرة[مسار[len(مسار) - 1]] = True
  # apl-source:69
  return حواف
# apl-source:70

# apl-source:71
def متصلة_كليا(حواف, ن):
  # apl-source:72
  جوار = {}
  # apl-source:73
  for ي in range(ن):
    # apl-source:74
    جوار[ي] = []
  # apl-source:75
  for ح in حواف:
    # apl-source:76
    جوار[ح[0]].append(ح[1])
    # apl-source:77
    جوار[ح[1]].append(ح[0])
  # apl-source:78
  مرئي = [False] * ن
  # apl-source:79
  طابور = [0]
  # apl-source:80
  مرئي[0] = True
  # apl-source:81
  رأس = 0
  # apl-source:82
  while رأس < len(طابور):
    # apl-source:83
    حالية = طابور[رأس]
    # apl-source:84
    رأس = رأس + 1
    # apl-source:85
    for ج in جوار[حالية]:
      # apl-source:86
      if مرئي[ج] == False:
        # apl-source:87
        مرئي[ج] = True
        # apl-source:88
        طابور.append(ج)
  # apl-source:89
  عدد = 0
  # apl-source:90
  for ي in range(ن):
    # apl-source:91
    if مرئي[ي]:
      # apl-source:92
      عدد = عدد + 1
  # apl-source:93
  return عدد
# apl-source:94

# apl-source:95
حواف = ويلسون(4, 4, 7)
# apl-source:96
تأكد_يساوي(len(حواف), 15, "شجرة 16 خلية لها 15 حافة")
# apl-source:97
تأكد_يساوي(متصلة_كليا(حواف, 16), 16, "كل الخلايا متصلة")
# apl-source:98
حواف2 = ويلسون(4, 4, 7)
# apl-source:99
تأكد_يساوي(len(حواف2), 15, "حتمية بنفس البذرة")
# apl-source:100
حواف3 = ويلسون(3, 3, 7)
# apl-source:101
تأكد_يساوي(len(حواف3), 8, "شجرة 9 خلايا لها 8 حواف")
# apl-source:102
تأكد_يساوي(متصلة_كليا(حواف3, 9), 9, "متاهة 3×3 متصلة")
# apl-source:103
print("حواف 4×4:", len(حواف))
# apl-source:104
