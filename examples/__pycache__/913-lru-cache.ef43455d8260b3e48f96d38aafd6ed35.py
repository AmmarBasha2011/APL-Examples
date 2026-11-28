
# apl-source:1
# مثال 913 — مخبأ الأقل استخداماً
# apl-source:2
# LRU cache
# apl-source:3
# Demonstrates: قائمة مرتبة بالاستخدام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/913-lru-cache.apl
# apl-source:6

# apl-source:7
# مخبأ الأقل استخداماً مؤخراً: سعة ثابتة وإخلاء الأقدم استخداماً
# apl-source:8
# قائمة مرتبة بالاستخدام + جدول للقيم
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
# نمثل المخبأ بقائمتين متوازيتين: مفاتيح (مرتبة: الأقدم أولاً) وقيم
# apl-source:19
def ابحث(مفاتيح, مفتاح):
  # apl-source:20
  for i in range(len(مفاتيح)):
    # apl-source:21
    if مفاتيح[i] == مفتاح:
      # apl-source:22
      return i
  # apl-source:23
  return -1
# apl-source:24

# apl-source:25
def اجلب(مفاتيح, قيم, مفتاح):
  # apl-source:26
  موضع = ابحث(مفاتيح, مفتاح)
  # apl-source:27
  if موضع < 0:
    # apl-source:28
    return [[], -1]
  # apl-source:29
  # انقله للذيل (الأحدث)
  # apl-source:30
  مفاتيح2 = مفاتيح[:موضع] + مفاتيح[موضع + 1:] + [مفتاح]
  # apl-source:31
  return [مفاتيح2, قيم[موضع]]
# apl-source:32

# apl-source:33
def اضع(مفاتيح, قيم, مفتاح, قيمة, سعة):
  # apl-source:34
  موضع = ابحث(مفاتيح, مفتاح)
  # apl-source:35
  if موضع >= 0:
    # apl-source:36
    مفاتيح2 = مفاتيح[:موضع] + مفاتيح[موضع + 1:] + [مفتاح]
    # apl-source:37
    قيم2 = قيم[:موضع] + قيم[موضع + 1:] + [قيمة]
    # apl-source:38
    return [مفاتيح2, قيم2]
  # apl-source:39
  if len(مفاتيح) >= سعة:
    # apl-source:40
    # أخل الرأس (الأقل استخداماً)
    # apl-source:41
    مفاتيح = مفاتيح[1:]
    # apl-source:42
    قيم = قيم[1:]
  # apl-source:43
  return [مفاتيح + [مفتاح], قيم + [قيمة]]
# apl-source:44

# apl-source:45
مفاتيح = []
# apl-source:46
قيم = []
# apl-source:47
# ضع 1=10، ضع 2=20، اجلب 1 (=10)، ضع 3=30 (يُخلي 2)، اجلب 2 (-1)، ضع 4=40 (يُخلي 1)، اجلب 3 (=30)
# apl-source:48
حالة = اضع(مفاتيح, قيم, 1, 10, 2)
# apl-source:49
حالة = اضع(حالة[0], حالة[1], 2, 20, 2)
# apl-source:50
جلب1 = اجلب(حالة[0], حالة[1], 1)
# apl-source:51
print("اجلب 1:", جلب1[1])
# apl-source:52
حالة = اضع(جلب1[0], حالة[1], 3, 30, 2)
# apl-source:53
جلب2 = اجلب(حالة[0], حالة[1], 2)
# apl-source:54
print("اجلب 2:", جلب2[1])
# apl-source:55
حالة = اضع(حالة[0], حالة[1], 4, 40, 2)
# apl-source:56
جلب3 = اجلب(حالة[0], حالة[1], 3)
# apl-source:57
print("اجلب 3:", جلب3[1])
# apl-source:58

# apl-source:59
تأكد_يساوي(جلب1[1], 10, "الأول موجود")
# apl-source:60
تأكد_يساوي(جلب2[1], -1, "الثاني أُخلي")
# apl-source:61
تأكد_يساوي(جلب3[1], 30, "الثالث بقي")
# apl-source:62
