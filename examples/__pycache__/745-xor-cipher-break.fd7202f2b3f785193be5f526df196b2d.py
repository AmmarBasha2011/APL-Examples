
# apl-source:1
# مثال 745 — كسر XOR أحادي
# apl-source:2
# Single-byte XOR break
# apl-source:3
# Demonstrates: تجربة كل المفاتيح، حروف شائعة، كلفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/745-xor-cipher-break.apl
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
# كسر تشفير XOR أحادي البايت بتحليل التكرارات
# apl-source:25
# Demonstrates: تجربة 256 مفتاحاً, تسجيل بحرف شائع, اختيار الأدنى كلفة
# apl-source:26
# النص الإنجليزي تكثر فيه الحروف etaoinshrdlu والمسافة
# apl-source:27

# apl-source:28
def شفر_xor(بايتات, مفتاح):
  # apl-source:29
  ناتج = []
  # apl-source:30
  for ي in range(len(بايتات)):
    # apl-source:31
    ناتج.append(بايتات[ي] ^ مفتاح)
  # apl-source:32
  return bytearray(ناتج)
# apl-source:33

# apl-source:34
def كلفة(نص):
  # apl-source:35
  شائعة = "etaoinshrdlu ETAOIN"
  # apl-source:36
  مجموع = 0
  # apl-source:37
  for ي in range(len(نص)):
    # apl-source:38
    if نص[ي] in شائعة:
      # apl-source:39
      مجموع = مجموع + 1
  # apl-source:40
  return len(نص) - مجموع
# apl-source:41

# apl-source:42
def اكسر(مشفر):
  # apl-source:43
  أفضل_مفتاح = 0
  # apl-source:44
  أفضل_كلفة = 999999
  # apl-source:45
  أفضل_نص = ""
  # apl-source:46
  for مفتاح in range(256):
    # apl-source:47
    مرشح = شفر_xor(مشفر, مفتاح).decode("latin1")
    # apl-source:48
    تكلفة = كلفة(مرشح)
    # apl-source:49
    if تكلفة < أفضل_كلفة:
      # apl-source:50
      أفضل_كلفة = تكلفة
      # apl-source:51
      أفضل_مفتاح = مفتاح
      # apl-source:52
      أفضل_نص = مرشح
  # apl-source:53
  return [أفضل_مفتاح, أفضل_نص]
# apl-source:54

# apl-source:55
نص = "the quick brown fox jumps over the lazy dog and runs away from the fox"
# apl-source:56
مشفر = شفر_xor(نص.encode("latin1"), 66)
# apl-source:57

# apl-source:58
تأكد_يساوي(مشفر[0], 0x74 ^ 66, "أول بايت مشفر")
# apl-source:59
تأكد_يساوي(شفر_xor(مشفر, 66).decode("latin1"), نص, "فك بنفس المفتاح")
# apl-source:60

# apl-source:61
نتيجة = اكسر(مشفر)
# apl-source:62
تأكد_يساوي(نتيجة[0], 66, "المفتاح المكتشف")
# apl-source:63
تأكد_يساوي(نتيجة[1], نص, "النص المستعاد")
# apl-source:64

# apl-source:65
مشفر2 = شفر_xor("attack at dawn with full force".encode("latin1"), 7)
# apl-source:66
تأكد_يساوي(اكسر(مشفر2), [7, "attack at dawn with full force"], "مفتاح صغير")
# apl-source:67

# apl-source:68
print("المفتاح:", نتيجة[0])
# apl-source:69
