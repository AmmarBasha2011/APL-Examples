
# apl-source:1
# مثال 604 — جولة الحصان
# apl-source:2
# Knight tour
# apl-source:3
# Demonstrates: حصان الشطرنج، وارنسدورف، جولة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/604-knight-tour.apl
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
# جولة الحصان: زيارة كل مربع مرة واحدة
# apl-source:25
# Demonstrates: قاعدة وارنسدورف, أقل الخيارات أولا, تحقق من الجولة
# apl-source:26
# حصان الشطرنج يتحرك بحرف L
# apl-source:27

# apl-source:28
ن = 8
# apl-source:29
حركات = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
# apl-source:30

# apl-source:31
def داخل(س, ص):
  # apl-source:32
  return س >= 0 and س < ن and ص >= 0 and ص < ن
# apl-source:33

# apl-source:34
def عدد_الخيارات(س, ص, لوحة):
  # apl-source:35
  عدد = 0
  # apl-source:36
  for ح in حركات:
    # apl-source:37
    if داخل(س + ح[0], ص + ح[1]) and لوحة[س + ح[0]][ص + ح[1]] == -1:
      # apl-source:38
      عدد = عدد + 1
  # apl-source:39
  return عدد
# apl-source:40

# apl-source:41
لوحة = []
# apl-source:42
for ي in range(ن):
  # apl-source:43
  لوحة.append([-1] * ن)
# apl-source:44
لوحة[0][0] = 0
# apl-source:45
س = 0
# apl-source:46
ص = 0
# apl-source:47
for خطوة in range(1, ن * ن):
  # apl-source:48
  أفضل = -1
  # apl-source:49
  أقل = ن + 1
  # apl-source:50
  for ح in حركات:
    # apl-source:51
    س2 = س + ح[0]
    # apl-source:52
    ص2 = ص + ح[1]
    # apl-source:53
    if داخل(س2, ص2) and لوحة[س2][ص2] == -1:
      # apl-source:54
      خيارات = عدد_الخيارات(س2, ص2, لوحة)
      # apl-source:55
      if خيارات < أقل:
        # apl-source:56
        أقل = خيارات
        # apl-source:57
        أفضل = ح
  # apl-source:58
  س = س + أفضل[0]
  # apl-source:59
  ص = ص + أفضل[1]
  # apl-source:60
  لوحة[س][ص] = خطوة
# apl-source:61

# apl-source:62
print("آخر خطوة:", لوحة[س][ص])
# apl-source:63
تأكد_يساوي(لوحة[س][ص], ن * ن - 1, "زيارة كل المربعات")
# apl-source:64
مجموع = 0
# apl-source:65
for صف in لوحة:
  # apl-source:66
  for خانة in صف:
    # apl-source:67
    مجموع = مجموع + خانة
# apl-source:68
تأكد_يساوي(مجموع, (ن * ن - 1) * ن * ن // 2, "مجموع أرقام الخطوات")
# apl-source:69
