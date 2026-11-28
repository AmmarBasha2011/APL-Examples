
# apl-source:1
# مثال 722 — ترميز Base58
# apl-source:2
# Base58 codec
# apl-source:3
# Demonstrates: أساس 58، أصفار بادئة، فك عكسي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/722-base58-codec.apl
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
# ترميز Base58 بأبجدية بيتكوين
# apl-source:25
# Demonstrates: قسمة مطولة على 58, أصفار بادئة كواحدات, بلا أحرف ملتبسة
# apl-source:26
# لا 0 ولا O ولا I ولا l: يقرأ بلا لبس
# apl-source:27

# apl-source:28
أبجدية = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
# apl-source:29

# apl-source:30
def شفر58(بايتات):
  # apl-source:31
  عدد = 0
  # apl-source:32
  for بايت in بايتات:
    # apl-source:33
    عدد = عدد * 256 + بايت
  # apl-source:34
  ناتج = ""
  # apl-source:35
  while عدد > 0:
    # apl-source:36
    ناتج = أبجدية[عدد % 58] + ناتج
    # apl-source:37
    عدد = عدد // 58
  # apl-source:38
  أصفار = 0
  # apl-source:39
  while أصفار < len(بايتات) and بايتات[أصفار] == 0:
    # apl-source:40
    أصفار = أصفار + 1
  # apl-source:41
  for ي in range(أصفار):
    # apl-source:42
    ناتج = "1" + ناتج
  # apl-source:43
  return ناتج
# apl-source:44

# apl-source:45
def فك58(نص):
  # apl-source:46
  عدد = 0
  # apl-source:47
  for ي in range(len(نص)):
    # apl-source:48
    رقم = أبجدية.index(نص[ي])
    # apl-source:49
    عدد = عدد * 58 + رقم
  # apl-source:50
  بايتات = []
  # apl-source:51
  while عدد > 0:
    # apl-source:52
    بايتات = [عدد % 256] + بايتات
    # apl-source:53
    عدد = عدد // 256
  # apl-source:54
  أصفار = 0
  # apl-source:55
  while أصفار < len(نص) and نص[أصفار] == "1":
    # apl-source:56
    أصفار = أصفار + 1
  # apl-source:57
  for ي in range(أصفار):
    # apl-source:58
    بايتات = [0] + بايتات
  # apl-source:59
  return بايتات
# apl-source:60

# apl-source:61
def من_نص(نص):
  # apl-source:62
  ناتج = []
  # apl-source:63
  for ي in range(len(نص)):
    # apl-source:64
    ناتج.append(ord(نص[ي]) % 256)
  # apl-source:65
  return ناتج
# apl-source:66

# apl-source:67
تأكد_يساوي(شفر58(من_نص("hello world")), "StV1DL6CwTryKyV", "مثال بيتكوين الشهير")
# apl-source:68
تأكد_يساوي(شفر58([0, 0, 1]), "112", "أصفار بادئة واحدات")
# apl-source:69
تأكد_يساوي(شفر58([0]), "1", "صفر واحد")
# apl-source:70
تأكد_يساوي(فك58("StV1DL6CwTryKyV"), من_نص("hello world"), "الفك يرجع الأصل")
# apl-source:71
تأكد_يساوي(شفر58(فك58("1Boat")), "1Boat", "رحلة ذهاب وعودة")
# apl-source:72
تأكد_يساوي(شفر58([255, 255]), "LUv", "أعلى بايتين")
# apl-source:73
print("hello world بالـ58:", شفر58(من_نص("hello world")))
# apl-source:74
