
# apl-source:1
# مثال 702 — تحليل ترويسة WAV
# apl-source:2
# WAV header parsing
# apl-source:3
# Demonstrates: RIFF، صغير-النهاية، كتل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/702-wav-header-parse.apl
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
# تحليل ترويسة ملف WAV (RIFF)
# apl-source:25
# Demonstrates: بايتات صغيرة-النهاية, حقول ثابتة الأطوال, كتل
# apl-source:26
# الترويسة تبنى في الذاكرة: لا ملفات خارجية
# apl-source:27

# apl-source:28
def نص4(ب, من):
  # apl-source:29
  return chr(ب[من]) + chr(ب[من + 1]) + chr(ب[من + 2]) + chr(ب[من + 3])
# apl-source:30

# apl-source:31
def ص16(ب, من):
  # apl-source:32
  return ب[من] + ب[من + 1] * 256
# apl-source:33

# apl-source:34
def ص32(ب, من):
  # apl-source:35
  return ب[من] + ب[من + 1] * 256 + ب[من + 2] * 65536 + ب[من + 3] * 16777216
# apl-source:36

# apl-source:37
def حلل(ب):
  # apl-source:38
  نتيجة = {}
  # apl-source:39
  نتيجة["riff"] = نص4(ب, 0)
  # apl-source:40
  نتيجة["wave"] = نص4(ب, 8)
  # apl-source:41
  نتيجة["fmt"] = نص4(ب, 12)
  # apl-source:42
  نتيجة["format"] = ص16(ب, 20)
  # apl-source:43
  نتيجة["channels"] = ص16(ب, 22)
  # apl-source:44
  نتيجة["rate"] = ص32(ب, 24)
  # apl-source:45
  نتيجة["bits"] = ص16(ب, 34)
  # apl-source:46
  نتيجة["data_tag"] = نص4(ب, 36)
  # apl-source:47
  نتيجة["data_size"] = ص32(ب, 40)
  # apl-source:48
  return نتيجة
# apl-source:49

# apl-source:50
# ترويسة 44 بايت: PCM ستيريو 44100 هرتز 16 بت، بيانات 1000 بايت
# apl-source:51
ترويسة = [82, 73, 70, 70, 232, 3, 0, 0, 87, 65, 86, 69, 102, 109, 116, 32, 16, 0, 0, 0, 1, 0, 2, 0, 68, 172, 0, 0, 16, 177, 2, 0, 4, 0, 16, 0, 100, 97, 116, 97, 232, 3, 0, 0]
# apl-source:52
ح = حلل(ترويسة)
# apl-source:53
تأكد_يساوي(ح["riff"], "RIFF", "وصف RIFF")
# apl-source:54
تأكد_يساوي(ح["wave"], "WAVE", "وصف WAVE")
# apl-source:55
تأكد_يساوي(ح["fmt"], "fmt ", "كتلة fmt")
# apl-source:56
تأكد_يساوي(ح["format"], 1, "PCM")
# apl-source:57
تأكد_يساوي(ح["channels"], 2, "ستيريو")
# apl-source:58
تأكد_يساوي(ح["rate"], 44100, "معدل العينة")
# apl-source:59
تأكد_يساوي(ح["bits"], 16, "16 بت")
# apl-source:60
تأكد_يساوي(ح["data_tag"], "data", "كتلة البيانات")
# apl-source:61
تأكد_يساوي(ح["data_size"], 1000, "حجم البيانات")
# apl-source:62
عينات = ح["data_size"] // (ح["channels"] * ح["bits"] // 8)
# apl-source:63
تأكد_يساوي(عينات, 250, "250 عينة لكل قناة")
# apl-source:64
print("معدل:", ح["rate"])
# apl-source:65
