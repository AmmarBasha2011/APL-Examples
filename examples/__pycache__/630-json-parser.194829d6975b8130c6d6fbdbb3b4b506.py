
# apl-source:1
# مثال 630 — محلل JSON من الصفر
# apl-source:2
# JSON parser
# apl-source:3
# Demonstrates: تحليل عودي، محلل رمزي، JSON
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/630-json-parser.apl
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
# محلل JSON مصغر من الصفر
# apl-source:25
# Demonstrates: تحليل عودي تنازلي, محلل رمزي, بناء قيم APL
# apl-source:26
# يحول نص JSON إلى قواميس وقوائم دون مكتبة
# apl-source:27

# apl-source:28
def محلل(نص):
  # apl-source:29
  return {"نص": نص, "موضع": 0}
# apl-source:30

# apl-source:31
def جسون_فراغ(م):
  # apl-source:32
  while م["موضع"] < len(م["نص"]) and م["نص"][م["موضع"]] == " ":
    # apl-source:33
    م["موضع"] = م["موضع"] + 1
# apl-source:34

# apl-source:35
def جسون_حرف(م):
  # apl-source:36
  ح = م["نص"][م["موضع"]]
  # apl-source:37
  م["موضع"] = م["موضع"] + 1
  # apl-source:38
  return ح
# apl-source:39

# apl-source:40
def جسون_قيمة(م):
  # apl-source:41
  جسون_فراغ(م)
  # apl-source:42
  ح = م["نص"][م["موضع"]]
  # apl-source:43
  if ح == "{":
    # apl-source:44
    return جسون_كائن(م)
  # apl-source:45
  if ح == "[":
    # apl-source:46
    return جسون_قائمة(م)
  # apl-source:47
  if ord(ح) == 34:
    # apl-source:48
    return جسون_نص(م)
  # apl-source:49
  return جسون_عدد(م)
# apl-source:50

# apl-source:51
def جسون_نص(م):
  # apl-source:52
  جسون_حرف(م)
  # apl-source:53
  ناتج = ""
  # apl-source:54
  while ord(م["نص"][م["موضع"]]) != 34:
    # apl-source:55
    ناتج = ناتج + جسون_حرف(م)
  # apl-source:56
  جسون_حرف(م)
  # apl-source:57
  return ناتج
# apl-source:58

# apl-source:59
def جسون_عدد(م):
  # apl-source:60
  بداية = م["موضع"]
  # apl-source:61
  while م["موضع"] < len(م["نص"]) and م["نص"][م["موضع"]] in "0123456789.-":
    # apl-source:62
    م["موضع"] = م["موضع"] + 1
  # apl-source:63
  return int(م["نص"][بداية:م["موضع"]])
# apl-source:64

# apl-source:65
def جسون_كائن(م):
  # apl-source:66
  جسون_حرف(م)
  # apl-source:67
  قاموس = {}
  # apl-source:68
  جسون_فراغ(م)
  # apl-source:69
  if م["نص"][م["موضع"]] == "}":
    # apl-source:70
    جسون_حرف(م)
    # apl-source:71
    return قاموس
  # apl-source:72
  while True:
    # apl-source:73
    جسون_فراغ(م)
    # apl-source:74
    مفتاح = جسون_نص(م)
    # apl-source:75
    جسون_فراغ(م)
    # apl-source:76
    جسون_حرف(م)
    # apl-source:77
    قاموس[مفتاح] = جسون_قيمة(م)
    # apl-source:78
    جسون_فراغ(م)
    # apl-source:79
    ح = جسون_حرف(م)
    # apl-source:80
    if ح == "}":
      # apl-source:81
      return قاموس
# apl-source:82

# apl-source:83
def جسون_قائمة(م):
  # apl-source:84
  جسون_حرف(م)
  # apl-source:85
  عناصر = []
  # apl-source:86
  جسون_فراغ(م)
  # apl-source:87
  if م["نص"][م["موضع"]] == "]":
    # apl-source:88
    جسون_حرف(م)
    # apl-source:89
    return عناصر
  # apl-source:90
  while True:
    # apl-source:91
    عناصر.append(جسون_قيمة(م))
    # apl-source:92
    جسون_فراغ(م)
    # apl-source:93
    ح = جسون_حرف(م)
    # apl-source:94
    if ح == "]":
      # apl-source:95
      return عناصر
# apl-source:96

# apl-source:97
نص = "{ \"اسم\": \"أحمد\", \"عمر\": 30, \"هوايات\": [\"قراءة\", \"سباحة\"], \"رصيد\": -5 }"
# apl-source:98
م = محلل(نص)
# apl-source:99
قيمة = جسون_قيمة(م)
# apl-source:100
print("الاسم:", قيمة["اسم"], " والعمر:", قيمة["عمر"])
# apl-source:101
تأكد_يساوي(قيمة["اسم"], "أحمد", "حقل نصي")
# apl-source:102
تأكد_يساوي(قيمة["عمر"], 30, "حقل عددي")
# apl-source:103
تأكد_يساوي(قيمة["هوايات"], ["قراءة", "سباحة"], "قائمة متداخلة")
# apl-source:104
تأكد_يساوي(قيمة["رصيد"], -5, "عدد سالب")
# apl-source:105
