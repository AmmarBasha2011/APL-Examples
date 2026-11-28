
# apl-source:1
# مثال 588 — ذاكرة LFU
# apl-source:2
# LFU cache
# apl-source:3
# Demonstrates: LFU، ترددات، طرد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/588-lfu-cache.apl
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
# ذاكرة مؤقتة LFU: طرد الأقل استخداما
# apl-source:25
# Demonstrates: عد الترددات, سياسة طرد, مقارنة مع LRU
# apl-source:26
# الأقل استخداما يطرد أولا، والأقدم بين المتساوين
# apl-source:27

# apl-source:28
def أنشئ(سعة):
  # apl-source:29
  return {"سعة": سعة, "قيم": {}, "تردد": {}, "ترتيب": []}
# apl-source:30

# apl-source:31
def المس(مخ, مفتاح):
  # apl-source:32
  مخ["تردد"][مفتاح] = مخ["تردد"][مفتاح] + 1
  # apl-source:33
  مخ["ترتيب"].remove(مفتاح)
  # apl-source:34
  مخ["ترتيب"].append(مفتاح)
# apl-source:35

# apl-source:36
def ضع(مخ, مفتاح, قيمة):
  # apl-source:37
  if مفتاح in مخ["قيم"]:
    # apl-source:38
    مخ["قيم"][مفتاح] = قيمة
    # apl-source:39
    المس(مخ, مفتاح)
  # apl-source:40
  else:
    # apl-source:41
    if len(مخ["قيم"]) >= مخ["سعة"]:
      # apl-source:42
      أدنى_تردد = min(مخ["تردد"].values())
      # apl-source:43
      مطروح = -1
      # apl-source:44
      for م in مخ["ترتيب"]:
        # apl-source:45
        if مطروح == -1 and مخ["تردد"][م] == أدنى_تردد:
          # apl-source:46
          مطروح = م
      # apl-source:47
      محو_عنصر = مخ["قيم"].pop(مطروح)
      # apl-source:48
      محو_تردد = مخ["تردد"].pop(مطروح)
      # apl-source:49
      مخ["ترتيب"].remove(مطروح)
    # apl-source:50
    مخ["قيم"][مفتاح] = قيمة
    # apl-source:51
    مخ["تردد"][مفتاح] = 1
    # apl-source:52
    مخ["ترتيب"].append(مفتاح)
# apl-source:53

# apl-source:54
def خذ(مخ, مفتاح):
  # apl-source:55
  if مفتاح in مخ["قيم"]:
    # apl-source:56
    المس(مخ, مفتاح)
    # apl-source:57
    return مخ["قيم"][مفتاح]
  # apl-source:58
  return -1
# apl-source:59

# apl-source:60
مخ = أنشئ(2)
# apl-source:61
ضع(مخ, "أ", 1)
# apl-source:62
ضع(مخ, "ب", 2)
# apl-source:63
تأكد_يساوي(خذ(مخ, "أ"), 1, "قراءة ترفع التردد")
# apl-source:64
ضع(مخ, "ج", 3)
# apl-source:65
تأكد_يساوي(خذ(مخ, "ب"), -1, "ب مطروح (الأقل استخداما)")
# apl-source:66
تأكد_يساوي(خذ(مخ, "أ"), 1, "أ بقي لتردده الأعلى")
# apl-source:67
ضع(مخ, "د", 4)
# apl-source:68
تأكد_يساوي(خذ(مخ, "ج"), -1, "ج طرد عند إضافة د (تردد 1)")
# apl-source:69
تأكد_يساوي(خذ(مخ, "أ"), 1, "أ بقي لتردده الأعلى")
# apl-source:70
تأكد_يساوي(خذ(مخ, "د"), 4, "د موجود")
# apl-source:71
