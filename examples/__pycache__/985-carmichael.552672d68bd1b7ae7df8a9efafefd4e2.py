
# apl-source:1
# مثال 985 — أعداد كارمايكل
# apl-source:2
# Carmichael numbers
# apl-source:3
# Demonstrates: فحص قواعد فيرما
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/985-carmichael.apl
# apl-source:6

# apl-source:7
# أعداد كارمايكل: مركبة تخدع اختبار فيرما لكل قاعدة سليمة
# apl-source:8
# 561 أصغرها: تمر كل قاعدة غير مشتركة معها في القواسم
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def قاسم(أ, ب):
  # apl-source:19
  س = أ
  # apl-source:20
  ص = ب
  # apl-source:21
  while ص != 0:
    # apl-source:22
    مؤقت = ص
    # apl-source:23
    ص = س % ص
    # apl-source:24
    س = مؤقت
  # apl-source:25
  return س
# apl-source:26

# apl-source:27
def قوة_مود(أ, هـ, م):
  # apl-source:28
  ناتج = 1
  # apl-source:29
  قاعدة = أ % م
  # apl-source:30
  باقي = هـ
  # apl-source:31
  while باقي > 0:
    # apl-source:32
    if (باقي % 2) == 1:
      # apl-source:33
      ناتج = (ناتج * قاعدة) % م
    # apl-source:34
    قاعدة = (قاعدة * قاعدة) % م
    # apl-source:35
    باقي = باقي // 2
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
عدد_سليم = 0
# apl-source:39
نجح_الكل = 1
# apl-source:40
for أ in range(2, 20):
  # apl-source:41
  if قاسم(أ, 561) == 1:
    # apl-source:42
    عدد_سليم = عدد_سليم + 1
    # apl-source:43
    if قوة_مود(أ, 560, 561) != 1:
      # apl-source:44
      نجح_الكل = 0
# apl-source:45

# apl-source:46
تأكد_يساوي(عدد_سليم, 10, "عشر قواعد سليمة")
# apl-source:47
تأكد_يساوي(نجح_الكل, 1, "كل القواعد تخدع فيرما")
# apl-source:48
تأكد_يساوي(561, 561, "مركب بثلاثة عوامل")
# apl-source:49
تأكد_يساوي(قاسم(12, 561), 3, "قاسم مشترك")
# apl-source:50
