
# apl-source:1
# مثال 612 — ذاكرة بمدة صلاحية
# apl-source:2
# TTL cache
# apl-source:3
# Demonstrates: TTL، انتهاء، ساعة مزيفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/612-ttl-cache.apl
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
# ذاكرة مؤقتة بمدة صلاحية (TTL)
# apl-source:25
# Demonstrates: انتهاء صلاحية, ساعة مزيفة للاختبار, تخزين حسابات مكلفة
# apl-source:26
# مفيد لتجنب إعادة الحساب مع تحديث دوري
# apl-source:27

# apl-source:28
def أنشئ(مدة):
  # apl-source:29
  return {"مدة": مدة, "عناصر": {}, "ساعة": [0], "ضربات": [0], "حسابات": [0]}
# apl-source:30

# apl-source:31
def خذ(مخ, مفتاح, حاسبة):
  # apl-source:32
  الآن = مخ["ساعة"][0]
  # apl-source:33
  if مفتاح in مخ["عناصر"]:
    # apl-source:34
    عنصر = مخ["عناصر"][مفتاح]
    # apl-source:35
    if الآن < عنصر["ينتهي"]:
      # apl-source:36
      مخ["ضربات"][0] = مخ["ضربات"][0] + 1
      # apl-source:37
      return عنصر["قيمة"]
  # apl-source:38
  مخ["حسابات"][0] = مخ["حسابات"][0] + 1
  # apl-source:39
  قيمة = حاسبة(مفتاح)
  # apl-source:40
  مخ["عناصر"][مفتاح] = {"قيمة": قيمة, "ينتهي": الآن + مخ["مدة"]}
  # apl-source:41
  return قيمة
# apl-source:42

# apl-source:43
def مربع(س):
  # apl-source:44
  return س * س
# apl-source:45

# apl-source:46
مخ = أنشئ(60)
# apl-source:47
تأكد_يساوي(خذ(مخ, 5, مربع), 25, "حساب أول")
# apl-source:48
تأكد_يساوي(خذ(مخ, 5, مربع), 25, "من الذاكرة")
# apl-source:49
تأكد_يساوي(مخ["حسابات"][0], 1, "حساب واحد فقط")
# apl-source:50
مخ["ساعة"][0] = 61
# apl-source:51
تأكد_يساوي(خذ(مخ, 5, مربع), 25, "بعد الانتهاء يعيد الحساب")
# apl-source:52
تأكد_يساوي(مخ["حسابات"][0], 2, "حسابان بعد الانتهاء")
# apl-source:53
print("ضربات الذاكرة:", مخ["ضربات"][0])
# apl-source:54
