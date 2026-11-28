
# apl-source:1
# مثال 793 — الشيفرة النيهيلستية
# apl-source:2
# Nihilist cipher
# apl-source:3
# Demonstrates: بوليبيوس، مفتاح جاري بالجمع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/793-nihilist-cipher.apl
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
# الشيفرة النيهيلستية: مربع بوليبيوس مع مفتاح جاري بالجمع
# apl-source:25
# Demonstrates: تحويل حرف لرقم ثنائي الخانة, مفتاح دوري, جمع مركب
# apl-source:26

# apl-source:27
مربع = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
# apl-source:28

# apl-source:29
def رقم_حرف(ح):
  # apl-source:30
  م = -1
  # apl-source:31
  for ي in range(25):
    # apl-source:32
    if مربع[ي] == ح:
      # apl-source:33
      م = ي
  # apl-source:34
  return (م // 5 + 1) * 10 + (م % 5 + 1)
# apl-source:35

# apl-source:36
def تشفير_نيهيلست(مدخل, مفتاح):
  # apl-source:37
  ناتج = []
  # apl-source:38
  for ي in range(len(مدخل)):
    # apl-source:39
    ح = مدخل[ي]
    # apl-source:40
    if ح != " ":
      # apl-source:41
      ك = مفتاح[ي % len(مفتاح)]
      # apl-source:42
      ناتج.append(رقم_حرف(ح) + رقم_حرف(ك))
  # apl-source:43
  return ناتج
# apl-source:44

# apl-source:45
def فك_نيهيلست(أرقام, مفتاح):
  # apl-source:46
  ناتج = ""
  # apl-source:47
  for ي in range(len(أرقام)):
    # apl-source:48
    ك = مفتاح[ي % len(مفتاح)]
    # apl-source:49
    ن = أرقام[ي] - رقم_حرف(ك)
    # apl-source:50
    ص = (ن // 10 - 1) * 5 + (ن % 10 - 1)
    # apl-source:51
    ناتج = ناتج + مربع[ص]
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
تأكد_يساوي(رقم_حرف("A"), 11, "رقم A")
# apl-source:55
تأكد_يساوي(رقم_حرف("Z"), 55, "رقم Z")
# apl-source:56
تأكد_يساوي(تشفير_نيهيلست("HELLO", "KEY"), [48, 30, 85, 56, 49], "تشفير HELLO بالمفتاح KEY")
# apl-source:57
تأكد_يساوي(فك_نيهيلست([48, 30, 85, 56, 49], "KEY"), "HELLO", "فك التشفير")
# apl-source:58
تأكد_يساوي(فك_نيهيلست(تشفير_نيهيلست("ATTACK", "ZEBRA"), "ZEBRA"), "ATTACK", "دورة كاملة")
# apl-source:59
