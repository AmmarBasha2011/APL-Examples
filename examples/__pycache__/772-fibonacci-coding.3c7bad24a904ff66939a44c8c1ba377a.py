
# apl-source:1
# مثال 772 — ترميز فيبوناتشي
# apl-source:2
# Fibonacci coding
# apl-source:3
# Demonstrates: زكندورف، بت إنهاء، فصل ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/772-fibonacci-coding.apl
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
# ترميز فيبوناتشي للأعداد: تمثيل زكندورف + بت إنهاء
# apl-source:25
# Demonstrates: تمثيل زكندورف الجشع, شفرة ذاتية الفصل ببتين متتاليين
# apl-source:26

# apl-source:27
def فيبوناتشي_ترميز(ن):
  # apl-source:28
  فيب = [1, 2]
  # apl-source:29
  while فيب[len(فيب) - 1] + فيب[len(فيب) - 2] <= ن:
    # apl-source:30
    فيب.append(فيب[len(فيب) - 1] + فيب[len(فيب) - 2])
  # apl-source:31
  بتات = []
  # apl-source:32
  for ي in range(len(فيب)):
    # apl-source:33
    بتات.append(0)
  # apl-source:34
  باقي = ن
  # apl-source:35
  ي = len(فيب) - 1
  # apl-source:36
  while ي >= 0:
    # apl-source:37
    if فيب[ي] <= باقي:
      # apl-source:38
      بتات[ي] = 1
      # apl-source:39
      باقي = باقي - فيب[ي]
    # apl-source:40
    ي = ي - 1
  # apl-source:41
  اعلى = len(بتات) - 1
  # apl-source:42
  while بتات[اعلى] == 0:
    # apl-source:43
    اعلى = اعلى - 1
  # apl-source:44
  ناتج = ""
  # apl-source:45
  ي = 0
  # apl-source:46
  while ي <= اعلى:
    # apl-source:47
    if بتات[ي] == 1:
      # apl-source:48
      ناتج = ناتج + "1"
    # apl-source:49
    else:
      # apl-source:50
      ناتج = ناتج + "0"
    # apl-source:51
    ي = ي + 1
  # apl-source:52
  return ناتج + "1"
# apl-source:53

# apl-source:54
def فيبوناتشي_فك(شفرة):
  # apl-source:55
  فيب = [1, 2]
  # apl-source:56
  while len(فيب) < len(شفرة):
    # apl-source:57
    فيب.append(فيب[len(فيب) - 1] + فيب[len(فيب) - 2])
  # apl-source:58
  حصيلة = 0
  # apl-source:59
  for ي in range(len(شفرة)):
    # apl-source:60
    if شفرة[ي] == "1":
      # apl-source:61
      if ي > 0 and شفرة[ي - 1] == "1":
        # apl-source:62
        return حصيلة
      # apl-source:63
      حصيلة = حصيلة + فيب[ي]
  # apl-source:64
  return حصيلة
# apl-source:65

# apl-source:66
تأكد_يساوي(فيبوناتشي_ترميز(1), "11", "ترميز 1")
# apl-source:67
تأكد_يساوي(فيبوناتشي_ترميز(11), "001011", "ترميز 11")
# apl-source:68
تأكد_يساوي(فيبوناتشي_ترميز(65), "0100100011", "ترميز 65")
# apl-source:69
تأكد_يساوي(فيبوناتشي_ترميز(100), "00101000011", "ترميز 100")
# apl-source:70
تأكد_يساوي(فيبوناتشي_فك("11"), 1, "فك 1")
# apl-source:71
تأكد_يساوي(فيبوناتشي_فك("001011"), 11, "فك 11")
# apl-source:72
تأكد_يساوي(فيبوناتشي_فك("0100100011"), 65, "فك 65")
# apl-source:73
تأكد_يساوي(فيبوناتشي_فك("00101000011"), 100, "فك 100")
# apl-source:74
تأكد_يساوي(فيبوناتشي_فك(فيبوناتشي_ترميز(999)), 999, "ذهاب وإياب 999")
# apl-source:75
