
# apl-source:1
# مثال 771 — ترميز bech32
# apl-source:2
# bech32 encoding
# apl-source:3
# Demonstrates: polymod، GF(32)، توسيع hrp
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/771-bech32-lite.apl
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
# ترميز bech32 (BIP 173): مجموع تحقق polymod فوق GF(32)
# apl-source:25
# Demonstrates: متعددة حدود مودولو, توسيع hrp, محارف qpzry9x8
# apl-source:26

# apl-source:27
محارف = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
# apl-source:28

# apl-source:29
def سداسي_عدد(س):
  # apl-source:30
  سداسي = "0123456789abcdef"
  # apl-source:31
  قيمة = 0
  # apl-source:32
  for حرف in س:
    # apl-source:33
    قيمة = قيمة * 16 + سداسي.index(حرف)
  # apl-source:34
  return قيمة
# apl-source:35

# apl-source:36
def قوة_اثنان(ي):
  # apl-source:37
  ق = 1
  # apl-source:38
  for ج in range(ي):
    # apl-source:39
    ق = ق * 2
  # apl-source:40
  return ق
# apl-source:41

# apl-source:42
def بوليمود(قيم):
  # apl-source:43
  معاملات = [سداسي_عدد("3b6a57b2"), سداسي_عدد("26508e6d"), سداسي_عدد("1ea119fa"), سداسي_عدد("3d4233dd"), سداسي_عدد("2a1462b3")]
  # apl-source:44
  تحقق = 1
  # apl-source:45
  for ق in قيم:
    # apl-source:46
    اعلى = تحقق // 33554432
    # apl-source:47
    تحقق = (تحقق % 33554432) * 32 ^ ق
    # apl-source:48
    for ي in range(5):
      # apl-source:49
      if (اعلى // قوة_اثنان(ي)) % 2 == 1:
        # apl-source:50
        تحقق = تحقق ^ معاملات[ي]
  # apl-source:51
  return تحقق
# apl-source:52

# apl-source:53
def توسيع(hrp):
  # apl-source:54
  ناتج = []
  # apl-source:55
  for حرف in hrp:
    # apl-source:56
    ناتج.append(ord(حرف) // 32)
  # apl-source:57
  ناتج.append(0)
  # apl-source:58
  for حرف in hrp:
    # apl-source:59
    ناتج.append(ord(حرف) % 32)
  # apl-source:60
  return ناتج
# apl-source:61

# apl-source:62
def بيك32_ترميز(hrp, بيانات):
  # apl-source:63
  قيم = توسيع(hrp) + بيانات + [0, 0, 0, 0, 0, 0]
  # apl-source:64
  بم = بوليمود(قيم) ^ 1
  # apl-source:65
  ناتج = hrp + "1"
  # apl-source:66
  for د in بيانات:
    # apl-source:67
    ناتج = ناتج + محارف[د]
  # apl-source:68
  for ي in range(6):
    # apl-source:69
    ناتج = ناتج + محارف[(بم // قوة_اثنان(5 * (5 - ي))) % 32]
  # apl-source:70
  return ناتج
# apl-source:71

# apl-source:72
def بيك32_تحقق(شفرة):
  # apl-source:73
  موضع = -1
  # apl-source:74
  for ي in range(len(شفرة)):
    # apl-source:75
    if شفرة[ي] == "1":
      # apl-source:76
      موضع = ي
  # apl-source:77
  if موضع < 1:
    # apl-source:78
    return False
  # apl-source:79
  hrp = شفرة[0:موضع]
  # apl-source:80
  بيانات = []
  # apl-source:81
  for ي in range(موضع + 1, len(شفرة)):
    # apl-source:82
    if (شفرة[ي] in محارف) == False:
      # apl-source:83
      return False
    # apl-source:84
    بيانات.append(محارف.index(شفرة[ي]))
  # apl-source:85
  return بوليمود(توسيع(hrp) + بيانات) == 1
# apl-source:86

# apl-source:87
تأكد_يساوي(بيك32_ترميز("a", []), "a12uel5l", "متجه BIP173: a")
# apl-source:88
تأكد_يساوي(بيك32_ترميز("test", []), "test12hrzfj", "ترميز test")
# apl-source:89
تأكد_يساوي(بيك32_تحقق("a12uel5l"), True, "تحقق صالح")
# apl-source:90
تأكد_يساوي(بيك32_تحقق("a12uel5m"), False, "تحقق فاسد")
# apl-source:91
تأكد_يساوي(بيك32_تحقق(بيك32_ترميز("bc", [0, 31, 7, 15])), True, "ذهاب وإياب ببيانات")
# apl-source:92
