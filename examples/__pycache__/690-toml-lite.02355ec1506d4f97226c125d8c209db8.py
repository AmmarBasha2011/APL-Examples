
# apl-source:1
# مثال 690 — قارئ TOML مصغر
# apl-source:2
# TOML lite parser
# apl-source:3
# Demonstrates: أقسام، مفاتيح، أنواع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/690-toml-lite.apl
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
# قارئ TOML مصغر: أقسام ومفاتيح وقيم
# apl-source:25
# Demonstrates: تتبع القسم الحالي, قيم نصية ورقمية ومنطقية, تعليقات
# apl-source:26
# يدعم: [قسم]، مفتاح = "نص"، مفتاح = 42، مفتاح = true/false
# apl-source:27

# apl-source:28
def قيمة_من(خام):
  # apl-source:29
  if خام.startswith("\"") and خام.endswith("\""):
    # apl-source:30
    return خام[1:len(خام) - 1]
  # apl-source:31
  if خام == "true":
    # apl-source:32
    return True
  # apl-source:33
  if خام == "false":
    # apl-source:34
    return False
  # apl-source:35
  return int(خام)
# apl-source:36

# apl-source:37
def اقرأ_تومل(سطور):
  # apl-source:38
  جذر = {}
  # apl-source:39
  حالي = جذر
  # apl-source:40
  for سطر in سطور:
    # apl-source:41
    م = سطر.strip()
    # apl-source:42
    if len(م) == 0 or م.startswith("#"):
      # apl-source:43
      م = ""
    # apl-source:44
    elif م.startswith("["):
      # apl-source:45
      اسم = م[1:len(م) - 1]
      # apl-source:46
      جذر[اسم] = {}
      # apl-source:47
      حالي = جذر[اسم]
    # apl-source:48
    else:
      # apl-source:49
      طرفان = م.split("=")
      # apl-source:50
      مفتاح = طرفان[0].strip()
      # apl-source:51
      خام = طرفان[1].strip()
      # apl-source:52
      حالي[مفتاح] = قيمة_من(خام)
  # apl-source:53
  return جذر
# apl-source:54

# apl-source:55
سطور = [
  # apl-source:56
  "# إعداد الخادم",
  # apl-source:57
  "عنوان = \"موقعي\"",
  # apl-source:58
  "",
  # apl-source:59
  "[server]",
  # apl-source:60
  "host = \"127.0.0.1\"",
  # apl-source:61
  "port = 8080",
  # apl-source:62
  "tls = true",
  # apl-source:63
  "",
  # apl-source:64
  "[limits]",
  # apl-source:65
  "max_conn = 256",
  # apl-source:66
  "debug = false"
# apl-source:67
]
# apl-source:68
ق = اقرأ_تومل(سطور)
# apl-source:69
تأكد_يساوي(ق["عنوان"], "موقعي", "مفتاح الجذر")
# apl-source:70
تأكد_يساوي(ق["server"]["host"], "127.0.0.1", "مضيف")
# apl-source:71
تأكد_يساوي(ق["server"]["port"], 8080, "منفذ رقمي")
# apl-source:72
تأكد_يساوي(ق["server"]["tls"], True, "قيمة منطقية صحيحة")
# apl-source:73
تأكد_يساوي(ق["limits"]["max_conn"], 256, "حد الاتصالات")
# apl-source:74
تأكد_يساوي(ق["limits"]["debug"], False, "قيمة منطقية خاطئة")
# apl-source:75
print("المنفذ:", ق["server"]["port"])
# apl-source:76
