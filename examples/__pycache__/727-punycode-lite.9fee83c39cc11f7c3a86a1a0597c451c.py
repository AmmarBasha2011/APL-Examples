
# apl-source:1
# مثال 727 — بوني كود مصغر
# apl-source:2
# Punycode lite
# apl-source:3
# Demonstrates: أساس 36، فاصل، تكييف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/727-punycode-lite.apl
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
# بيونيكود (RFC 3492) بخوارزمية كاملة مصغرة التعليق
# apl-source:25
# Demonstrates: أساس 36, متحيز متكيف, أعداد بطول متغير
# apl-source:26
# أسماء النطاقات العربية: xn-- ثم بيونيكود
# apl-source:27

# apl-source:28
def رقم_حرف(ر):
  # apl-source:29
  if ر < 26:
    # apl-source:30
    return chr(ord("a") + ر)
  # apl-source:31
  return chr(ord("0") + ر - 26)
# apl-source:32

# apl-source:33
def تكيف(فرق, نقاط, أول):
  # apl-source:34
  قاعدة = 36
  # apl-source:35
  أدنى = 1
  # apl-source:36
  أعلى = 26
  # apl-source:37
  ميل = 38
  # apl-source:38
  ترطيب = 700
  # apl-source:39
  if أول:
    # apl-source:40
    فرق = فرق // ترطيب
  # apl-source:41
  else:
    # apl-source:42
    فرق = فرق // 2
  # apl-source:43
  فرق = فرق + فرق // نقاط
  # apl-source:44
  ك = 0
  # apl-source:45
  while فرق > ((قاعدة - أدنى) * أعلى) // 2:
    # apl-source:46
    فرق = فرق // (قاعدة - أدنى)
    # apl-source:47
    ك = ك + قاعدة
  # apl-source:48
  return ك + (قاعدة - أدنى + 1) * فرق // (فرق + ميل)
# apl-source:49

# apl-source:50
def شفر(نص):
  # apl-source:51
  نقاط = []
  # apl-source:52
  for ي in range(len(نص)):
    # apl-source:53
    نقاط.append(ord(نص[ي]))
  # apl-source:54
  ناتج = ""
  # apl-source:55
  for ن in نقاط:
    # apl-source:56
    if ن < 128:
      # apl-source:57
      ناتج = ناتج + chr(ن)
  # apl-source:58
  أساسي = len(ناتج)
  # apl-source:59
  if أساسي > 0 and أساسي < len(نقاط):
    # apl-source:60
    ناتج = ناتج + "-"
  # apl-source:61
  ن = 128
  # apl-source:62
  فرق = 0
  # apl-source:63
  متحيز = 72
  # apl-source:64
  طول_سابق = أساسي
  # apl-source:65
  while طول_سابق < len(نقاط):
    # apl-source:66
    أدنى_ج = -1
    # apl-source:67
    for ن2 in نقاط:
      # apl-source:68
      if ن2 >= ن and (أدنى_ج < 0 or ن2 < أدنى_ج):
        # apl-source:69
        أدنى_ج = ن2
    # apl-source:70
    فرق = فرق + (أدنى_ج - ن) * (طول_سابق + 1)
    # apl-source:71
    ن = أدنى_ج
    # apl-source:72
    for ن2 in نقاط:
      # apl-source:73
      if ن2 < ن:
        # apl-source:74
        فرق = فرق + 1
      # apl-source:75
      if ن2 == ن:
        # apl-source:76
        ق = فرق
        # apl-source:77
        ك = 36
        # apl-source:78
        مستمر = True
        # apl-source:79
        while مستمر:
          # apl-source:80
          if ك <= متحيز:
            # apl-source:81
            ت = 1
          # apl-source:82
          elif ك >= متحيز + 26:
            # apl-source:83
            ت = 26
          # apl-source:84
          else:
            # apl-source:85
            ت = ك - متحيز
          # apl-source:86
          if ق < ت:
            # apl-source:87
            مستمر = False
          # apl-source:88
          else:
            # apl-source:89
            ناتج = ناتج + رقم_حرف(ت + (ق - ت) % (36 - ت))
            # apl-source:90
            ق = (ق - ت) // (36 - ت)
            # apl-source:91
            ك = ك + 36
        # apl-source:92
        ناتج = ناتج + رقم_حرف(ق)
        # apl-source:93
        متحيز = تكيف(فرق, طول_سابق + 1, طول_سابق == أساسي)
        # apl-source:94
        فرق = 0
        # apl-source:95
        طول_سابق = طول_سابق + 1
    # apl-source:96
    فرق = فرق + 1
    # apl-source:97
    ن = ن + 1
  # apl-source:98
  return ناتج
# apl-source:99

# apl-source:100
تأكد_يساوي(شفر("mañana"), "maana-pta", "مثال RFC")
# apl-source:101
تأكد_يساوي(شفر("bücher"), "bcher-kva", "ألمانية")
# apl-source:102
تأكد_يساوي(شفر("hello"), "hello", "آسكي خالص بلا لاحقة")
# apl-source:103
تأكد_يساوي(شفر("a"), "a", "حرف واحد")
# apl-source:104
تأكد_يساوي(شفر("例え"), "r8jz45g", "يابانية")
# apl-source:105
print("مثال بيونيكود:", شفر("mañana"))
# apl-source:106
