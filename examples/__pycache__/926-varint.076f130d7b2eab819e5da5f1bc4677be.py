
# apl-source:1
# مثال 926 — الترميز المتغير الطول
# apl-source:2
# Varint encoding
# apl-source:3
# Demonstrates: سبع بتات لكل بايت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/926-varint.apl
# apl-source:6

# apl-source:7
# ترميز varint: أعداد صحيحة بطول متغير (7 بتات لكل بايت)
# apl-source:8
# بت الإشارة العليا تعني "يوجد بايت تالٍ" - يستخدم في بروتوكولات الشبكة
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
def رمز_متغير(ن):
  # apl-source:19
  بايتات = []
  # apl-source:20
  م = ن
  # apl-source:21
  while 1 == 1:
    # apl-source:22
    بت = م & 127
    # apl-source:23
    م = م >> 7
    # apl-source:24
    if م > 0:
      # apl-source:25
      بايتات = بايتات + [بت | 128]
    # apl-source:26
    else:
      # apl-source:27
      بايتات = بايتات + [بت]
      # apl-source:28
      return بايتات
# apl-source:29

# apl-source:30
def فك_متغير(بايتات):
  # apl-source:31
  قيمة = 0
  # apl-source:32
  إزاحة = 0
  # apl-source:33
  for بايت in بايتات:
    # apl-source:34
    قيمة = قيمة | ((بايت & 127) << إزاحة)
    # apl-source:35
    if بايت & 128 == 0:
      # apl-source:36
      return قيمة
    # apl-source:37
    إزاحة = إزاحة + 7
  # apl-source:38
  return قيمة
# apl-source:39

# apl-source:40
print("300 ->", رمز_متغير(300))
# apl-source:41
print("1 ->", رمز_متغير(1))
# apl-source:42
print("624485 ->", رمز_متغير(624485))
# apl-source:43

# apl-source:44
# 300 = 0b100101100 -> بايتان: [172, 2]
# apl-source:45
ر300 = رمز_متغير(300)
# apl-source:46
تأكد_يساوي(len(ر300), 2, "300 ببايتين")
# apl-source:47
تأكد_يساوي(ر300[0], 172, "البايت الأول")
# apl-source:48
تأكد_يساوي(ر300[1], 2, "البايت الثاني")
# apl-source:49

# apl-source:50
# الصغار يأخذون بايتاً واحداً
# apl-source:51
تأكد_يساوي(len(رمز_متغير(1)), 1, "واحد ببايت")
# apl-source:52
تأكد_يساوي(len(رمز_متغير(127)), 1, "127 ببايت")
# apl-source:53
تأكد_يساوي(len(رمز_متغير(128)), 2, "128 ببايتين")
# apl-source:54

# apl-source:55
# 624485 بثلاثة بايتات
# apl-source:56
تأكد_يساوي(len(رمز_متغير(624485)), 3, "624485 بثلاثة")
# apl-source:57

# apl-source:58
# الفك يعيد الأصل
# apl-source:59
for ن in [0, 1, 127, 128, 300, 624485, 1000000]:
  # apl-source:60
  تأكد_يساوي(فك_متغير(رمز_متغير(ن)), ن, "طي وفك " + str(ن))
# apl-source:61
