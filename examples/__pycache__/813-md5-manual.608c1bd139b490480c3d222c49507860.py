
# apl-source:1
# مثال 813 — MD5 يدوي
# apl-source:2
# MD5 from spec
# apl-source:3
# Demonstrates: حشوة، 4 جولات، كلمات صغيرة الطرفية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/813-md5-manual.apl
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
# بناء MD5 من المواصفة: أربع جولات بدوال منطقية مختلفة وكلمات صغيرة الطرفية
# apl-source:25
# Demonstrates: حشوة ببايت 128, جداول K من الجيب, دوران متغير, إخراج سداسي
# apl-source:26

# apl-source:27
ك = [3614090360, 3905402710, 606105819, 3250441966, 4118548399, 1200080426, 2821735955, 4249261313, 1770035416, 2336552879, 4294925233, 2304563134, 1804603682, 4254626195, 2792965006, 1236535329, 4129170786, 3225465664, 643717713, 3921069994, 3593408605, 38016083, 3634488961, 3889429448, 568446438, 3275163606, 4107603335, 1163531501, 2850285829, 4243563512, 1735328473, 2368359562, 4294588738, 2272392833, 1839030562, 4259657740, 2763975236, 1272893353, 4139469664, 3200236656, 681279174, 3936430074, 3572445317, 76029189, 3654602809, 3873151461, 530742520, 3299628645, 4096336452, 1126891415, 2878612391, 4237533241, 1700485571, 2399980690, 4293915773, 2240044497, 1873313359, 4264355552, 2734768916, 1309151649, 4149444226, 3174756917, 718787259, 3951481745]
# apl-source:28
سرعة = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
# apl-source:29
م32 = 4294967296
# apl-source:30
سداسي = "0123456789abcdef"
# apl-source:31

# apl-source:32
def دوّر(س, ر):
  # apl-source:33
  return ((س << ر) % م32) | (س >> (32 - ر))
# apl-source:34

# apl-source:35
def سداسي_كلمة(و):
  # apl-source:36
  ناتج = ""
  # apl-source:37
  for ي in range(4):
    # apl-source:38
    ب = (و >> (8 * ي)) % 256
    # apl-source:39
    ناتج = ناتج + سداسي[ب // 16] + سداسي[ب % 16]
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
def إم_دي_5(رسالة):
  # apl-source:43
  بايتات = []
  # apl-source:44
  for حرف in رسالة:
    # apl-source:45
    بايتات.append(ord(حرف))
  # apl-source:46
  طول_بت = len(بايتات) * 8
  # apl-source:47
  بايتات.append(128)
  # apl-source:48
  while len(بايتات) % 64 != 56:
    # apl-source:49
    بايتات.append(0)
  # apl-source:50
  for ي in range(8):
    # apl-source:51
    بايتات.append((طول_بت // (2 ** (8 * ي))) % 256)
  # apl-source:52
  أ0 = 1732584193
  # apl-source:53
  ب0 = 4023233417
  # apl-source:54
  ج0 = 2562383102
  # apl-source:55
  د0 = 271733878
  # apl-source:56
  for كتلة in range(len(بايتات) // 64):
    # apl-source:57
    ش = []
    # apl-source:58
    for ي in range(16):
      # apl-source:59
      قاعدة = كتلة * 64 + ي * 4
      # apl-source:60
      ش.append(بايتات[قاعدة] | (بايتات[قاعدة + 1] << 8) | (بايتات[قاعدة + 2] << 16) | (بايتات[قاعدة + 3] << 24))
    # apl-source:61
    أ = أ0
    # apl-source:62
    ب = ب0
    # apl-source:63
    ج = ج0
    # apl-source:64
    د = د0
    # apl-source:65
    for ي in range(64):
      # apl-source:66
      if ي < 16:
        # apl-source:67
        ق = (ب & ج) | ((ب ^ 4294967295) & د)
        # apl-source:68
        غ = ي
      # apl-source:69
      elif ي < 32:
        # apl-source:70
        ق = (د & ب) | ((د ^ 4294967295) & ج)
        # apl-source:71
        غ = (5 * ي + 1) % 16
      # apl-source:72
      elif ي < 48:
        # apl-source:73
        ق = ب ^ ج ^ د
        # apl-source:74
        غ = (3 * ي + 5) % 16
      # apl-source:75
      else:
        # apl-source:76
        ق = ج ^ (ب | (د ^ 4294967295))
        # apl-source:77
        غ = (7 * ي) % 16
      # apl-source:78
      ق = (ق + أ + ك[ي] + ش[غ]) % م32
      # apl-source:79
      أ = د
      # apl-source:80
      د = ج
      # apl-source:81
      ج = ب
      # apl-source:82
      ب = (ب + دوّر(ق, سرعة[ي])) % م32
    # apl-source:83
    أ0 = (أ0 + أ) % م32
    # apl-source:84
    ب0 = (ب0 + ب) % م32
    # apl-source:85
    ج0 = (ج0 + ج) % م32
    # apl-source:86
    د0 = (د0 + د) % م32
  # apl-source:87
  return سداسي_كلمة(أ0) + سداسي_كلمة(ب0) + سداسي_كلمة(ج0) + سداسي_كلمة(د0)
# apl-source:88

# apl-source:89
تأكد_يساوي(إم_دي_5(""), "d41d8cd98f00b204e9800998ecf8427e", "نص فارغ")
# apl-source:90
تأكد_يساوي(إم_دي_5("abc"), "900150983cd24fb0d6963f7d28e17f72", "abc")
# apl-source:91
تأكد_يساوي(إم_دي_5("The quick brown fox"), "a2004f37730b9445670a738fa0fc9ee5", "جملة قصيرة")
# apl-source:92
تأكد_يساوي(إم_دي_5("The quick brown fox jumps over the lazy dog"), "9e107d9d372bb6826bd81d3542a419d6", "الجملة الكاملة")
# apl-source:93
