
# apl-source:1
# مثال 791 — تجزية xxHash32
# apl-source:2
# xxHash32
# apl-source:3
# Demonstrates: أولية كبيرة، دوار، avalanche
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/791-xxhash-lite.apl
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
# تجزية xxHash32 غير التشفيرية: أولية كبيرة وتدوير وانهيار
# apl-source:25
# Demonstrates: دورات بأربعة مجمعات, معالجة الذيل, خطوات avalanche
# apl-source:26

# apl-source:27
م32 = 4294967296
# apl-source:28
أ1 = 2654435761
# apl-source:29
أ2 = 2246822519
# apl-source:30
أ3 = 3266489917
# apl-source:31
أ4 = 668265263
# apl-source:32
أ5 = 374761393
# apl-source:33

# apl-source:34
def دوار32(س, ر):
  # apl-source:35
  قناع = م32 - 1
  # apl-source:36
  return ((س << ر) & قناع) | (س >> (32 - ر))
# apl-source:37

# apl-source:38
def كتلة_صغيرة(ب, ي):
  # apl-source:39
  return ب[ي] | (ب[ي + 1] << 8) | (ب[ي + 2] << 16) | (ب[ي + 3] << 24)
# apl-source:40

# apl-source:41
def اكس_هاش32(رسالة):
  # apl-source:42
  ب = []
  # apl-source:43
  for حرف in رسالة:
    # apl-source:44
    ب.append(ord(حرف))
  # apl-source:45
  ن = len(ب)
  # apl-source:46
  ي = 0
  # apl-source:47
  if ن >= 16:
    # apl-source:48
    ع1 = (أ1 + أ2) % م32
    # apl-source:49
    ع2 = أ2
    # apl-source:50
    ع3 = 0
    # apl-source:51
    ع4 = (م32 - أ1) % م32
    # apl-source:52
    while ي <= ن - 16:
      # apl-source:53
      ع1 = (دوار32((ع1 + كتلة_صغيرة(ب, ي) * أ2) % م32, 13) * أ1) % م32
      # apl-source:54
      ع2 = (دوار32((ع2 + كتلة_صغيرة(ب, ي + 4) * أ2) % م32, 13) * أ1) % م32
      # apl-source:55
      ع3 = (دوار32((ع3 + كتلة_صغيرة(ب, ي + 8) * أ2) % م32, 13) * أ1) % م32
      # apl-source:56
      ع4 = (دوار32((ع4 + كتلة_صغيرة(ب, ي + 12) * أ2) % م32, 13) * أ1) % م32
      # apl-source:57
      ي = ي + 16
    # apl-source:58
    ه = (دوار32(ع1, 1) + دوار32(ع2, 7) + دوار32(ع3, 12) + دوار32(ع4, 18)) % م32
  # apl-source:59
  else:
    # apl-source:60
    ه = أ5
  # apl-source:61
  ه = (ه + ن) % م32
  # apl-source:62
  while ي <= ن - 4:
    # apl-source:63
    ه = (دوار32((ه + كتلة_صغيرة(ب, ي) * أ3) % م32, 17) * أ4) % م32
    # apl-source:64
    ي = ي + 4
  # apl-source:65
  while ي < ن:
    # apl-source:66
    ه = (دوار32((ه + ب[ي] * أ5) % م32, 11) * أ1) % م32
    # apl-source:67
    ي = ي + 1
  # apl-source:68
  ه = ه ^ (ه >> 15)
  # apl-source:69
  ه = (ه * أ2) % م32
  # apl-source:70
  ه = ه ^ (ه >> 13)
  # apl-source:71
  ه = (ه * أ3) % م32
  # apl-source:72
  ه = ه ^ (ه >> 16)
  # apl-source:73
  return ه
# apl-source:74

# apl-source:75
تأكد_يساوي(اكس_هاش32(""), 46947589, "نص فارغ")
# apl-source:76
تأكد_يساوي(اكس_هاش32("abc"), 852579327, "abc")
# apl-source:77
تأكد_يساوي(اكس_هاش32("hello"), 4211111929, "hello")
# apl-source:78
تأكد_يساوي(اكس_هاش32("The quick brown fox jumps over the lazy dog"), 3898516702, "نص طويل")
# apl-source:79
