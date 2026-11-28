
# apl-source:1
# مثال 769 — SHA-1 يدوي
# apl-source:2
# SHA-1 from spec
# apl-source:3
# Demonstrates: حشوة، 80 دورة، دوران 32-بت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/769-sha1-manual.apl
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
# SHA-1 من المواصفة: حشوة، 80 دورة، خمس كلمات حالة
# apl-source:25
# Demonstrates: دوران 32-بت, جدولة مفاتيح موسعة, حشوة ميركل-دامغارد
# apl-source:26

# apl-source:27
قوى2 = [1]
# apl-source:28
for ي in range(65):
  # apl-source:29
  قوى2.append(قوى2[len(قوى2) - 1] * 2)
# apl-source:30

# apl-source:31
def دوّر(س, ر):
  # apl-source:32
  return ((س * قوى2[ر]) + (س // قوى2[32 - ر])) % قوى2[32]
# apl-source:33

# apl-source:34
def شا1(رسالة):
  # apl-source:35
  م32 = قوى2[32]
  # apl-source:36
  بايتات = []
  # apl-source:37
  for حرف in رسالة:
    # apl-source:38
    بايتات.append(ord(حرف))
  # apl-source:39
  طول_بت = len(بايتات) * 8
  # apl-source:40
  بايتات.append(128)
  # apl-source:41
  while len(بايتات) % 64 != 56:
    # apl-source:42
    بايتات.append(0)
  # apl-source:43
  for ي in range(8):
    # apl-source:44
    بايتات.append((طول_بت // قوى2[8 * (7 - ي)]) % 256)
  # apl-source:45
  ه0 = 1732584193
  # apl-source:46
  ه1 = 4023233417
  # apl-source:47
  ه2 = 2562383102
  # apl-source:48
  ه3 = 271733878
  # apl-source:49
  ه4 = 3285377520
  # apl-source:50
  for كتلة in range(len(بايتات) // 64):
    # apl-source:51
    ش = []
    # apl-source:52
    for ت in range(16):
      # apl-source:53
      ع = كتلة * 64 + ت * 4
      # apl-source:54
      ش.append(بايتات[ع] * 16777216 + بايتات[ع + 1] * 65536 + بايتات[ع + 2] * 256 + بايتات[ع + 3])
    # apl-source:55
    for ت in range(16, 80):
      # apl-source:56
      ش.append(دوّر(((ش[ت - 3] ^ ش[ت - 8]) ^ ش[ت - 14]) ^ ش[ت - 16], 1))
    # apl-source:57
    أ = ه0
    # apl-source:58
    ب = ه1
    # apl-source:59
    ج = ه2
    # apl-source:60
    د = ه3
    # apl-source:61
    هـ = ه4
    # apl-source:62
    for ت in range(80):
      # apl-source:63
      if ت < 20:
        # apl-source:64
        ف = (ب & ج) | ((م32 - 1 - ب) & د)
        # apl-source:65
        ك = 1518500249
      # apl-source:66
      elif ت < 40:
        # apl-source:67
        ف = (ب ^ ج) ^ د
        # apl-source:68
        ك = 1859775393
      # apl-source:69
      elif ت < 60:
        # apl-source:70
        ف = ((ب & ج) | (ب & د)) | (ج & د)
        # apl-source:71
        ك = 2400959708
      # apl-source:72
      else:
        # apl-source:73
        ف = (ب ^ ج) ^ د
        # apl-source:74
        ك = 3395469782
      # apl-source:75
      مؤقت = ((((دوّر(أ, 5) + ف) % م32 + هـ) % م32 + ك) % م32 + ش[ت]) % م32
      # apl-source:76
      هـ = د
      # apl-source:77
      د = ج
      # apl-source:78
      ج = دوّر(ب, 30)
      # apl-source:79
      ب = أ
      # apl-source:80
      أ = مؤقت
    # apl-source:81
    ه0 = (ه0 + أ) % م32
    # apl-source:82
    ه1 = (ه1 + ب) % م32
    # apl-source:83
    ه2 = (ه2 + ج) % م32
    # apl-source:84
    ه3 = (ه3 + د) % م32
    # apl-source:85
    ه4 = (ه4 + هـ) % م32
  # apl-source:86
  سداسي = "0123456789abcdef"
  # apl-source:87
  ناتج = ""
  # apl-source:88
  for كلمة in [ه0, ه1, ه2, ه3, ه4]:
    # apl-source:89
    for ي in range(8):
      # apl-source:90
      ناتج = ناتج + سداسي[(كلمة // قوى2[4 * (7 - ي)]) % 16]
  # apl-source:91
  return ناتج
# apl-source:92

# apl-source:93
تأكد_يساوي(شا1(""), "da39a3ee5e6b4b0d3255bfef95601890afd80709", "sha1 فارغ")
# apl-source:94
تأكد_يساوي(شا1("abc"), "a9993e364706816aba3e25717850c26c9cd0d89d", "sha1 abc")
# apl-source:95
تأكد_يساوي(شا1("abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"), "84983e441c3bd26ebaae4aa1f95129e5e54670f1", "sha1 رسالة طويلة")
# apl-source:96
تأكد_يساوي(شا1("The quick brown fox jumps over the lazy dog"), "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12", "sha1 الثعلب")
# apl-source:97
