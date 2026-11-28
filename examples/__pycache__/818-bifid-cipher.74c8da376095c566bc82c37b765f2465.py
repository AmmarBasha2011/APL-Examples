
# apl-source:1
# مثال 818 — شفرة بيفيد
# apl-source:2
# Bifid cipher
# apl-source:3
# Demonstrates: فصل إحداثيات، كتل بدورة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/818-bifid-cipher.apl
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
# شفرة بيفيد التجزيئية: فصل الصفوف عن الأعمدة ثم إعادة الاقتران
# apl-source:25
# Demonstrates: مربع بوليبيوس, كتل بدورة ثابتة, خلط إحداثيات
# apl-source:26

# apl-source:27
مربع = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
# apl-source:28

# apl-source:29
def موقع(ح):
  # apl-source:30
  for ي in range(25):
    # apl-source:31
    if مربع[ي] == ح:
      # apl-source:32
      return ي
  # apl-source:33
  return -1
# apl-source:34

# apl-source:35
def شفر_بيفيد(نص, دورة):
  # apl-source:36
  ناتج = ""
  # apl-source:37
  بداية = 0
  # apl-source:38
  while بداية < len(نص):
    # apl-source:39
    صفوف = []
    # apl-source:40
    أعمدة = []
    # apl-source:41
    نهاية = بداية + دورة
    # apl-source:42
    if نهاية > len(نص):
      # apl-source:43
      نهاية = len(نص)
    # apl-source:44
    for ي in range(بداية, نهاية):
      # apl-source:45
      م = موقع(نص[ي])
      # apl-source:46
      صفوف.append(م // 5 + 1)
      # apl-source:47
      أعمدة.append(م % 5 + 1)
    # apl-source:48
    أرقام = []
    # apl-source:49
    for ر in صفوف:
      # apl-source:50
      أرقام.append(ر)
    # apl-source:51
    for ع in أعمدة:
      # apl-source:52
      أرقام.append(ع)
    # apl-source:53
    ي = 0
    # apl-source:54
    while ي < len(أرقام):
      # apl-source:55
      ناتج = ناتج + مربع[(أرقام[ي] - 1) * 5 + أرقام[ي + 1] - 1]
      # apl-source:56
      ي = ي + 2
    # apl-source:57
    بداية = نهاية
  # apl-source:58
  return ناتج
# apl-source:59

# apl-source:60
تأكد_يساوي(شفر_بيفيد("HELLO", 5), "FNNVD", "كلمة واحدة")
# apl-source:61
تأكد_يساوي(شفر_بيفيد("HELLOWORLD", 5), "FNNVDXSBRD", "كلمتان بدورتين")
# apl-source:62
تأكد_يساوي(شفر_بيفيد("ABC", 3), "AAH", "كتلة قصيرة")
# apl-source:63
تأكد_يساوي(شفر_بيفيد("ABC", 10), "AAH", "دورة أكبر من النص")
# apl-source:64
