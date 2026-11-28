
# apl-source:1
# مثال 744 — صندوق تعويض AES
# apl-source:2
# AES S-box from math
# apl-source:3
# Demonstrates: حقل GF(2^8)، معكوس، تحويل أفيني
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/744-aes-sbox-lite.apl
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
# بناء صندوق التعويض S-Box في AES من الأسس الرياضية
# apl-source:25
# Demonstrates: حقل GF(2^8), ضرب متعددات الحدود, معكوس, تحويل أفيني
# apl-source:26
# S(x) = affine(inverse(x)) — لا جدول ثابت هنا بل حساب كامل
# apl-source:27

# apl-source:28
def ضرب_حقل(أ, ب):
  # apl-source:29
  ناتج = 0
  # apl-source:30
  م = أ
  # apl-source:31
  while ب > 0:
    # apl-source:32
    if ب % 2 == 1:
      # apl-source:33
      ناتج = ناتج ^ م
    # apl-source:34
    if م >= 128:
      # apl-source:35
      م = (م * 2) % 256 ^ 27
    # apl-source:36
    else:
      # apl-source:37
      م = م * 2
    # apl-source:38
    ب = ب // 2
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
def معكوس(أ):
  # apl-source:42
  if أ == 0:
    # apl-source:43
    return 0
  # apl-source:44
  ناتج = 1
  # apl-source:45
  for ي in range(254):
    # apl-source:46
    ناتج = ضرب_حقل(ناتج, أ)
  # apl-source:47
  return ناتج
# apl-source:48

# apl-source:49
def دوّر(ب, ر):
  # apl-source:50
  return ((ب * قوة_2(ر)) + (ب // قوة_2(8 - ر))) % 256
# apl-source:51

# apl-source:52
def قوة_2(ر):
  # apl-source:53
  ناتج = 1
  # apl-source:54
  for ي in range(ر):
    # apl-source:55
    ناتج = ناتج * 2
  # apl-source:56
  return ناتج
# apl-source:57

# apl-source:58
def صندوق_عوض(س):
  # apl-source:59
  م = معكوس(س)
  # apl-source:60
  return (م ^ دوّر(م, 1) ^ دوّر(م, 2) ^ دوّر(م, 3) ^ دوّر(م, 4) ^ 99) % 256
# apl-source:61

# apl-source:62
# قيم AES المعيارية المعروفة
# apl-source:63
تأكد_يساوي(صندوق_عوض(0), 99, "S(0) = 0x63")
# apl-source:64
تأكد_يساوي(صندوق_عوض(1), 124, "S(1) = 0x7c")
# apl-source:65
تأكد_يساوي(صندوق_عوض(83), 237, "S(0x53) = 0xed")
# apl-source:66
تأكد_يساوي(صندوق_عوض(255), 22, "S(255) = 0x16")
# apl-source:67

# apl-source:68
تأكد_يساوي(ضرب_حقل(87, 131), 193, "ضرب AES الشهير 57*83=c1")
# apl-source:69
تأكد_يساوي(معكوس(83), 202, "معكوس 0x53")
# apl-source:70
تأكد_يساوي(ضرب_حقل(83, 202), 1, "الضرب بالمعكوس يعطي 1")
# apl-source:71

# apl-source:72
# الجدول العكسي يعيد كل قيمة
# apl-source:73
جدول = []
# apl-source:74
for ي in range(256):
  # apl-source:75
  جدول.append(صندوق_عوض(ي))
# apl-source:76
عكسي = []
# apl-source:77
for ي in range(256):
  # apl-source:78
  عكسي.append(0)
# apl-source:79
for ي in range(256):
  # apl-source:80
  عكسي[جدول[ي]] = ي
# apl-source:81
تأكد_يساوي(عكسي[99], 0, "عكس S(0)")
# apl-source:82
تأكد_يساوي(عكسي[جدول[200]], 200, "ذهاب وإياب 200")
# apl-source:83
تأكد_يساوي(len(جدول), 256, "جدول كامل")
# apl-source:84

# apl-source:85
print("S(0x53) =", جدول[83])
# apl-source:86
