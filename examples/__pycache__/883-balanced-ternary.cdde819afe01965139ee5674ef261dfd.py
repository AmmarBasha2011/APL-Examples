
# apl-source:1
# مثال 883 — الثلاثي المتوازن
# apl-source:2
# Balanced ternary
# apl-source:3
# Demonstrates: أرقام -1,0,+1
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/883-balanced-ternary.apl
# apl-source:6

# apl-source:7
# الثلاثي المتوازن: أرقام -1 و0 و+1 بدل 0 و1 و2
# apl-source:8
# 14 = 27-9-3-1 وكل عدد صحيح له تمثيل فريد
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
def إلى_متوازن(ن):
  # apl-source:19
  أرقام = []
  # apl-source:20
  م = ن
  # apl-source:21
  if م == 0:
    # apl-source:22
    أرقام = أرقام + [0]
  # apl-source:23
  while م != 0:
    # apl-source:24
    باقي = م % 3
    # apl-source:25
    م = م // 3
    # apl-source:26
    if باقي == 2:
      # apl-source:27
      باقي = -1
      # apl-source:28
      م = م + 1
    # apl-source:29
    أرقام = أرقام + [باقي]
  # apl-source:30
  ناتج = []
  # apl-source:31
  for i in range(len(أرقام)):
    # apl-source:32
    ناتج = ناتج + [أرقام[len(أرقام) - 1 - i]]
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
def من_متوازن(أرقام):
  # apl-source:36
  قيمة = 0
  # apl-source:37
  for رقم in أرقام:
    # apl-source:38
    قيمة = قيمة * 3 + رقم
  # apl-source:39
  return قيمة
# apl-source:40

# apl-source:41
ت14 = إلى_متوازن(14)
# apl-source:42
ت25 = إلى_متوازن(25)
# apl-source:43
print("14 =", ت14)
# apl-source:44
print("25 =", ت25)
# apl-source:45

# apl-source:46
تأكد_يساوي(len(ت14), 4, "14 بأربعة أرقام")
# apl-source:47
تأكد_يساوي(ت14[0], 1, "14 تبدأ بـ +1 (27)")
# apl-source:48
تأكد_يساوي(ت14[1], -1, "ثم -1 (9)")
# apl-source:49
تأكد_يساوي(ت14[3], -1, "وتنتهي بـ -1")
# apl-source:50
تأكد_يساوي(من_متوازن(ت14), 14, "الفك يعيد 14")
# apl-source:51
تأكد_يساوي(من_متوازن(ت25), 25, "الفك يعيد 25")
# apl-source:52
تأكد_يساوي(ت25[0], 1, "25: 27-3+1")
# apl-source:53
تأكد_يساوي(ت25[2], -1, "الرقم الثالث -1")
# apl-source:54

# apl-source:55
# السالب بقلب الإشارات فقط
# apl-source:56
تس14 = إلى_متوازن(-14)
# apl-source:57
تأكد_يساوي(تس14[0], -1, "-14 تبدأ بـ -1")
# apl-source:58
تأكد_يساوي(من_متوازن(تس14), -14, "الفك يعيد -14")
# apl-source:59

# apl-source:60
# طي وفك لكل الأعداد حتى 100
# apl-source:61
for ن in range(0, 101):
  # apl-source:62
  تأكد_يساوي(من_متوازن(إلى_متوازن(ن)), ن, "طي وفك " + str(ن))
# apl-source:63
