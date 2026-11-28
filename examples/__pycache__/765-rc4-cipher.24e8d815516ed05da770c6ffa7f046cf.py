
# apl-source:1
# مثال 765 — تشفير RC4
# apl-source:2
# RC4 stream cipher
# apl-source:3
# Demonstrates: KSA وPRGA، تيار مفتاح، XOR
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/765-rc4-cipher.apl
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
# تشفير RC4 التدفقي: KSA ثم PRGA
# apl-source:25
# Demonstrates: جدول تبديل 256 بايت, مؤشران متجولان, XOR مع تيار المفتاح
# apl-source:26

# apl-source:27
def ار_سي_فور(مفتاح, بيانات):
  # apl-source:28
  س = []
  # apl-source:29
  for ي in range(256):
    # apl-source:30
    س.append(ي)
  # apl-source:31
  ج = 0
  # apl-source:32
  for ي in range(256):
    # apl-source:33
    ج = (ج + س[ي] + مفتاح[ي % len(مفتاح)]) % 256
    # apl-source:34
    مؤقت = س[ي]
    # apl-source:35
    س[ي] = س[ج]
    # apl-source:36
    س[ج] = مؤقت
  # apl-source:37
  ي = 0
  # apl-source:38
  ج = 0
  # apl-source:39
  ناتج = []
  # apl-source:40
  for ب in بيانات:
    # apl-source:41
    ي = (ي + 1) % 256
    # apl-source:42
    ج = (ج + س[ي]) % 256
    # apl-source:43
    مؤقت = س[ي]
    # apl-source:44
    س[ي] = س[ج]
    # apl-source:45
    س[ج] = مؤقت
    # apl-source:46
    ناتج.append(ب ^ س[(س[ي] + س[ج]) % 256])
  # apl-source:47
  return bytearray(ناتج)
# apl-source:48

# apl-source:49
تأكد_يساوي(ار_سي_فور(b"Key", b"Plaintext").hex(), "bbf316e8d940af0ad3", "متجه ويكيبيديا Key")
# apl-source:50
تأكد_يساوي(ار_سي_فور(b"Wiki", b"pedia").hex(), "1021bf0420", "متجه ويكيبيديا Wiki")
# apl-source:51
تأكد_يساوي(ار_سي_فور(b"Secret", b"Attack at dawn").hex(), "45a01f645fc35b383552544b9bf5", "متجه ويكيبيديا Secret")
# apl-source:52
مشفر = ار_سي_فور(b"Key", b"Hello, RC4!")
# apl-source:53
تأكد_يساوي(ار_سي_فور(b"Key", مشفر).hex(), "48656c6c6f2c2052433421", "فك التشفير بإعادة التطبيق")
# apl-source:54
