
# apl-source:1
# مثال 754 — مسارات JSON
# apl-source:2
# JSONPath lite
# apl-source:3
# Demonstrates: تحليل مسار، حقول، فهارس معقوفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/754-json-path-lite.apl
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
# مقيّم مسارات JSON مبسط: $.a.b[0].c
# apl-source:25
# Demonstrates: تحليل مسار نصي, نزول في قواميس وقوائم, فهارس معقوفة
# apl-source:26
# يدعم النقطة للحقول والأقواس المعقوفة للفهارس
# apl-source:27

# apl-source:28
def حلل_مسار(مسار):
  # apl-source:29
  خطوات = []
  # apl-source:30
  حالي = ""
  # apl-source:31
  ي = 0
  # apl-source:32
  while ي < len(مسار):
    # apl-source:33
    حرف = مسار[ي]
    # apl-source:34
    if حرف == ".":
      # apl-source:35
      if حالي != "":
        # apl-source:36
        خطوات.append(["حقل", حالي])
        # apl-source:37
        حالي = ""
    # apl-source:38
    elif حرف == "[":
      # apl-source:39
      if حالي != "":
        # apl-source:40
        خطوات.append(["حقل", حالي])
        # apl-source:41
        حالي = ""
      # apl-source:42
      نهاية = مسار.index("]", ي)
      # apl-source:43
      خطوات.append(["فهرس", int(مسار[ي + 1:نهاية])])
      # apl-source:44
      ي = نهاية
    # apl-source:45
    elif حرف != "$":
      # apl-source:46
      حالي = حالي + حرف
    # apl-source:47
    ي = ي + 1
  # apl-source:48
  if حالي != "":
    # apl-source:49
    خطوات.append(["حقل", حالي])
  # apl-source:50
  return خطوات
# apl-source:51

# apl-source:52
def طبق(بيانات, مسار):
  # apl-source:53
  حالي = بيانات
  # apl-source:54
  for خطوة in حلل_مسار(مسار):
    # apl-source:55
    if خطوة[0] == "حقل":
      # apl-source:56
      حالي = حالي.get(خطوة[1], None)
    # apl-source:57
    else:
      # apl-source:58
      if حالي == None:
        # apl-source:59
        return None
      # apl-source:60
      if خطوة[1] < 0 or خطوة[1] >= len(حالي):
        # apl-source:61
        return None
      # apl-source:62
      حالي = حالي[خطوة[1]]
  # apl-source:63
  return حالي
# apl-source:64

# apl-source:65
بيانات = {
  # apl-source:66
  "متجر": {
    # apl-source:67
    "كتب": [
      # apl-source:68
      {"عنوان": "الأول", "سعر": 8},
      # apl-source:69
      {"عنوان": "الثاني", "سعر": 12}
    # apl-source:70
    ],
    # apl-source:71
    "دراجة": {"لون": "أحمر"}
  # apl-source:72
  },
  # apl-source:73
  "غالي": True
# apl-source:74
}
# apl-source:75

# apl-source:76
تأكد_يساوي(طبق(بيانات, "$.متجر.دراجة.لون"), "أحمر", "حقل متداخل")
# apl-source:77
تأكد_يساوي(طبق(بيانات, "$.متجر.كتب[0].عنوان"), "الأول", "فهرس ثم حقل")
# apl-source:78
تأكد_يساوي(طبق(بيانات, "$.متجر.كتب[1].سعر"), 12, "سعر الكتاب الثاني")
# apl-source:79
تأكد_يساوي(طبق(بيانات, "$.غالي"), True, "قيمة منطقية")
# apl-source:80
تأكد_يساوي(طبق(بيانات, "$.متجر.غيرموجود"), None, "حقل مفقود")
# apl-source:81
تأكد_يساوي(طبق(بيانات, "$.متجر.كتب[5]"), None, "فهرس خارج النطاق")
# apl-source:82
تأكد_يساوي(طبق(بيانات, "$.متجر.غيرموجود[0].عميق"), None, "سلسلة مفقودة")
# apl-source:83

# apl-source:84
تأكد_يساوي(حلل_مسار("$.a.b[2]"), [["حقل", "a"], ["حقل", "b"], ["فهرس", 2]], "خطوات المسار")
# apl-source:85

# apl-source:86
print("اللون:", طبق(بيانات, "$.متجر.دراجة.لون"))
# apl-source:87
