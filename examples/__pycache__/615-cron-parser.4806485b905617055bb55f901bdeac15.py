
# apl-source:1
# مثال 615 — محلل كرون
# apl-source:2
# Cron parser
# apl-source:3
# Demonstrates: كرون، جدولة، حقول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/615-cron-parser.apl
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
# محلل كرون: متى يرن الجدول التالي؟
# apl-source:25
# Demonstrates: حقول كرون الخمسة, نجمة وخطوة وقائمة, بحث تصاعدي
# apl-source:26
# يحسب الدقائق المطابقة خلال يوم كامل
# apl-source:27

# apl-source:28
def يطابق_دقيقة(حقل, قيمة):
  # apl-source:29
  if حقل == "*":
    # apl-source:30
    return True
  # apl-source:31
  if حقل.startswith("*/"):
    # apl-source:32
    خطوة = int(حقل[2:])
    # apl-source:33
    return قيمة % خطوة == 0
  # apl-source:34
  for جزء in حقل.split(","):
    # apl-source:35
    if int(جزء) == قيمة:
      # apl-source:36
      return True
  # apl-source:37
  return False
# apl-source:38

# apl-source:39
def يطابق(مواصفة, ساعة, دقيقة):
  # apl-source:40
  حقول = مواصفة.split(" ")
  # apl-source:41
  return يطابق_دقيقة(حقول[0], دقيقة) and يطابق_دقيقة(حقول[1], ساعة)
# apl-source:42

# apl-source:43
def التالي(مواصفة, ساعة, دقيقة):
  # apl-source:44
  for إزاحة in range(1, 1441):
    # apl-source:45
    كلي = ساعة * 60 + دقيقة + إزاحة
    # apl-source:46
    س = (كلي // 60) % 24
    # apl-source:47
    د = كلي % 60
    # apl-source:48
    if يطابق(مواصفة, س, د):
      # apl-source:49
      return [س, د]
  # apl-source:50
  return [-1, -1]
# apl-source:51

# apl-source:52
تأكد_يساوي(التالي("*/15 * * * *", 10, 7), [10, 15], "ربع ساعة")
# apl-source:53
تأكد_يساوي(التالي("0 9 * * *", 10, 30), [9, 0], "التاسعة صباحا غدا")
# apl-source:54
تأكد_يساوي(التالي("30 14 * * *", 10, 0), [14, 30], "اليوم نفسه")
# apl-source:55
تأكد_يساوي(يطابق("5,10 3 * * *", 3, 10), True, "قائمة دقائق")
# apl-source:56
print("التالي بعد 10:07 لجدول */15:", التالي("*/15 * * * *", 10, 7))
# apl-source:57
