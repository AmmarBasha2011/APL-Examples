
# apl-source:1
# مثال 907 — النظام السالب الثنائي
# apl-source:2
# Negabinary
# apl-source:3
# Demonstrates: أساس ناقص اثنين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/907-negabinary.apl
# apl-source:6

# apl-source:7
# النظام السالب الثنائي: تمثيل الأعداد بالأساس -2
# apl-source:8
# كل عدد صحيح (موجباً أو سالباً) له تمثيل بلا إشارة
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
def إلى_سالب_ثنائي(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return [0]
  # apl-source:21
  أرقام = []
  # apl-source:22
  م = ن
  # apl-source:23
  while م != 0:
    # apl-source:24
    باقي = م % -2
    # apl-source:25
    م = م // -2
    # apl-source:26
    if باقي < 0:
      # apl-source:27
      باقي = باقي + 2
      # apl-source:28
      م = م + 1
    # apl-source:29
    أرقام = أرقام + [باقي]
  # apl-source:30
  # الأرقام بالترتيب العكسي (الأقل أهمية أولاً) ثم نعكسها
  # apl-source:31
  مقلوبة = []
  # apl-source:32
  for i in range(len(أرقام)):
    # apl-source:33
    مقلوبة = مقلوبة + [أرقام[len(أرقام) - 1 - i]]
  # apl-source:34
  return مقلوبة
# apl-source:35

# apl-source:36
def من_سالب_ثنائي(أرقام):
  # apl-source:37
  قيمة = 0
  # apl-source:38
  أساس = 1
  # apl-source:39
  for i in range(len(أرقام)):
    # apl-source:40
    قيمة = قيمة + أرقام[len(أرقام) - 1 - i] * أساس
    # apl-source:41
    أساس = أساس * -2
  # apl-source:42
  return قيمة
# apl-source:43

# apl-source:44
س7 = إلى_سالب_ثنائي(7)
# apl-source:45
س9 = إلى_سالب_ثنائي(-9)
# apl-source:46
print("7 بالسالب الثنائي:", س7)
# apl-source:47
print("-9 بالسالب الثنائي:", س9)
# apl-source:48

# apl-source:49
# 7 = 16 - 8 + 0 + 2 - 1 = 11011 بالأساس -2
# apl-source:50
تأكد_يساوي(len(س7), 5, "طول تمثيل 7")
# apl-source:51
تأكد_يساوي(س7[0], 1, "خانة أولى")
# apl-source:52

# apl-source:53
# سالب 9 = 1011: -8 + 0 + 2 - 1... تحقق بالفك
# apl-source:54
تأكد_يساوي(من_سالب_ثنائي(س7), 7, "فك 7")
# apl-source:55
تأكد_يساوي(من_سالب_ثنائي(س9), -9, "فك -9")
# apl-source:56

# apl-source:57
# طي وفك لمجال واسع
# apl-source:58
for ن in range(-50, 51):
  # apl-source:59
  تأكد_يساوي(من_سالب_ثنائي(إلى_سالب_ثنائي(ن)), ن, "طي وفك " + str(ن))
# apl-source:60
