
# apl-source:1
# مثال 798 — ترميز Ascii85
# apl-source:2
# Ascii85 codec
# apl-source:3
# Demonstrates: أربعة بايتات لخمسة أحرف، حشو
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/798-base85-codec.apl
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
# ترميز Ascii85: أربعة بايتات تصبح خمسة أحرف قابلة للطباعة
# apl-source:25
# Demonstrates: قسمة متكررة على 85, حشو المجموعة الأخيرة, فك عكسي
# apl-source:26

# apl-source:27
def ترميز_85(بيانات):
  # apl-source:28
  ب = []
  # apl-source:29
  for حرف in بيانات:
    # apl-source:30
    ب.append(ord(حرف))
  # apl-source:31
  ناتج = ""
  # apl-source:32
  ي = 0
  # apl-source:33
  while ي < len(ب):
    # apl-source:34
    مجموعة = []
    # apl-source:35
    for ك in range(4):
      # apl-source:36
      if ي + ك < len(ب):
        # apl-source:37
        مجموعة.append(ب[ي + ك])
      # apl-source:38
      else:
        # apl-source:39
        مجموعة.append(0)
    # apl-source:40
    قيمة = مجموعة[0] * 16777216 + مجموعة[1] * 65536 + مجموعة[2] * 256 + مجموعة[3]
    # apl-source:41
    أحرف = ["!", "!", "!", "!", "!"]
    # apl-source:42
    for ك in range(5):
      # apl-source:43
      أحرف[4 - ك] = chr(33 + قيمة % 85)
      # apl-source:44
      قيمة = قيمة // 85
    # apl-source:45
    متبقي = len(ب) - ي
    # apl-source:46
    if متبقي >= 4:
      # apl-source:47
      for ح in أحرف:
        # apl-source:48
        ناتج = ناتج + ح
    # apl-source:49
    else:
      # apl-source:50
      for ك in range(متبقي + 1):
        # apl-source:51
        ناتج = ناتج + أحرف[ك]
    # apl-source:52
    ي = ي + 4
  # apl-source:53
  return ناتج
# apl-source:54

# apl-source:55
def فك_85(مشفر):
  # apl-source:56
  ناتج = ""
  # apl-source:57
  ي = 0
  # apl-source:58
  while ي < len(مشفر):
    # apl-source:59
    متبقي = len(مشفر) - ي
    # apl-source:60
    عدد = 5
    # apl-source:61
    if متبقي < 5:
      # apl-source:62
      عدد = متبقي
    # apl-source:63
    قيمة = 0
    # apl-source:64
    for ك in range(عدد):
      # apl-source:65
      قيمة = قيمة * 85 + ord(مشفر[ي + ك]) - 33
    # apl-source:66
    for ك in range(5 - عدد):
      # apl-source:67
      قيمة = قيمة * 85 + 84
    # apl-source:68
    for ك in range(عدد - 1):
      # apl-source:69
      إزاحة = (3 - ك) * 8
      # apl-source:70
      ناتج = ناتج + chr((قيمة // (2 ** إزاحة)) % 256)
    # apl-source:71
    ي = ي + عدد
  # apl-source:72
  return ناتج
# apl-source:73

# apl-source:74
تأكد_يساوي(ترميز_85("APL!"), "5u:5u", "أربعة أحرف")
# apl-source:75
تأكد_يساوي(ترميز_85("hello world"), "BOu!rD]j7BEbo7", "hello world")
# apl-source:76
تأكد_يساوي(فك_85("5u:5u"), "APL!", "فك أربعة")
# apl-source:77
تأكد_يساوي(فك_85("BOu!rD]j7BEbo7"), "hello world", "فك hello world")
# apl-source:78
تأكد_يساوي(فك_85(ترميز_85("12345678")), "12345678", "دورة ثمانية")
# apl-source:79
