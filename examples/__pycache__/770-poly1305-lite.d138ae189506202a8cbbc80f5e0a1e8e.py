
# apl-source:1
# مثال 770 — مصادقة Poly1305
# apl-source:2
# Poly1305 MAC
# apl-source:3
# Demonstrates: أعداد ضخمة، 2^130-5، كتل 16 بايت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/770-poly1305-lite.apl
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
# Poly1305: مصادقة رسائل بكثيرة حدود مودولو 2^130-5 (RFC 8439)
# apl-source:25
# Demonstrates: أعداد صحيحة ضخمة, تثبيط r, كتل 16 بايت
# apl-source:26

# apl-source:27
def سداسي_عدد(س):
  # apl-source:28
  سداسي = "0123456789abcdef"
  # apl-source:29
  قيمة = 0
  # apl-source:30
  for حرف in س:
    # apl-source:31
    قيمة = قيمة * 16 + سداسي.index(حرف)
  # apl-source:32
  return قيمة
# apl-source:33

# apl-source:34
def صغير_الطرف_عدد(بايتات):
  # apl-source:35
  قيمة = 0
  # apl-source:36
  معامل = 1
  # apl-source:37
  for ب in بايتات:
    # apl-source:38
    قيمة = قيمة + ب * معامل
    # apl-source:39
    معامل = معامل * 256
  # apl-source:40
  return قيمة
# apl-source:41

# apl-source:42
def بايتات_نص(نص):
  # apl-source:43
  ناتج = []
  # apl-source:44
  for حرف in نص:
    # apl-source:45
    ناتج.append(ord(حرف))
  # apl-source:46
  return ناتج
# apl-source:47

# apl-source:48
def بولي1305(مفتاح_سداسي, رسالة):
  # apl-source:49
  مفتاح = []
  # apl-source:50
  ي = 0
  # apl-source:51
  while ي < 64:
    # apl-source:52
    مفتاح.append(سداسي_عدد(مفتاح_سداسي[ي:ي + 2]))
    # apl-source:53
    ي = ي + 2
  # apl-source:54
  ر = صغير_الطرف_عدد(مفتاح[0:16]) & سداسي_عدد("0ffffffc0ffffffc0ffffffc0fffffff")
  # apl-source:55
  س = صغير_الطرف_عدد(مفتاح[16:32])
  # apl-source:56
  قوة130 = 1
  # apl-source:57
  for ي in range(130):
    # apl-source:58
    قوة130 = قوة130 * 2
  # apl-source:59
  أولي = قوة130 - 5
  # apl-source:60
  بايتات = بايتات_نص(رسالة)
  # apl-source:61
  تراكم = 0
  # apl-source:62
  ع = 0
  # apl-source:63
  while ع < len(بايتات):
    # apl-source:64
    نهاية = ع + 16
    # apl-source:65
    if نهاية > len(بايتات):
      # apl-source:66
      نهاية = len(بايتات)
    # apl-source:67
    كتلة = بايتات[ع:نهاية]
    # apl-source:68
    قوة_بت = 1
    # apl-source:69
    for ي in range(8 * len(كتلة)):
      # apl-source:70
      قوة_بت = قوة_بت * 2
    # apl-source:71
    ن = صغير_الطرف_عدد(كتلة) + قوة_بت
    # apl-source:72
    تراكم = ((تراكم + ن) * ر) % أولي
    # apl-source:73
    ع = ع + 16
  # apl-source:74
  قوة128 = 1
  # apl-source:75
  for ي in range(128):
    # apl-source:76
    قوة128 = قوة128 * 2
  # apl-source:77
  وسم = (تراكم + س) % قوة128
  # apl-source:78
  سداسي = "0123456789abcdef"
  # apl-source:79
  ناتج = ""
  # apl-source:80
  for ي in range(16):
    # apl-source:81
    بايت = وسم % 256
    # apl-source:82
    وسم = وسم // 256
    # apl-source:83
    ناتج = ناتج + سداسي[بايت // 16] + سداسي[بايت % 16]
  # apl-source:84
  return ناتج
# apl-source:85

# apl-source:86
تأكد_يساوي(بولي1305("85d6be7857556d337f4452fe42d506a80103808afb0db2fd4abff6af4149f51b", "Cryptographic Forum Research Group"), "a8061dc1305136c6c22b8baf0c0127a9", "متجه RFC 8439")
# apl-source:87
تأكد_يساوي(بولي1305("0000000000000000000000000000000000000000000000000000000000000000", ""), "00000000000000000000000000000000", "مفتاح صفري")
# apl-source:88
