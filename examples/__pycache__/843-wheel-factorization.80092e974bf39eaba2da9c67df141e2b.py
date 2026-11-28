
# apl-source:1
# مثال 843 — التحليل بالعجلة
# apl-source:2
# Wheel factorization
# apl-source:3
# Demonstrates: عجلة 30، تخطي المضاعفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/843-wheel-factorization.apl
# apl-source:6

# apl-source:7
# التحليل بعجلة 30: قسمة تجريبية تتخطى مضاعفات 2 و3 و5
# apl-source:8
# المرشحون فقط من البواقي الأولية مع 30: 1,7,11,13,17,19,23,29
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
def حلل_بالعجلة(عدد):
  # apl-source:19
  عوامل = []
  # apl-source:20
  ن = عدد
  # apl-source:21
  for أولي in [2, 3, 5]:
    # apl-source:22
    while ن % أولي == 0:
      # apl-source:23
      عوامل = عوامل + [أولي]
      # apl-source:24
      ن = ن // أولي
  # apl-source:25
  # زيادات العجلة: الفروق بين الأعداد الأولية مع 30
  # apl-source:26
  زيادات = [4, 2, 4, 2, 4, 6, 2, 6]
  # apl-source:27
  مرشح = 7
  # apl-source:28
  موضع = 0
  # apl-source:29
  while مرشح * مرشح <= ن:
    # apl-source:30
    while ن % مرشح == 0:
      # apl-source:31
      عوامل = عوامل + [مرشح]
      # apl-source:32
      ن = ن // مرشح
    # apl-source:33
    مرشح = مرشح + زيادات[موضع]
    # apl-source:34
    موضع = (موضع + 1) % 8
  # apl-source:35
  if ن > 1:
    # apl-source:36
    عوامل = عوامل + [ن]
  # apl-source:37
  return عوامل
# apl-source:38

# apl-source:39
عوامل = حلل_بالعجلة(360360)
# apl-source:40
print("عوامل 360360:", عوامل)
# apl-source:41

# apl-source:42
تأكد_يساوي(len(عوامل), 9, "عدد العوامل")
# apl-source:43
تأكد_يساوي(عوامل[0], 2, "أول عامل")
# apl-source:44
تأكد_يساوي(عوامل[2], 2, "ثلاثة اثنينات")
# apl-source:45
تأكد_يساوي(عوامل[4], 3, "ثم ثلاثتان")
# apl-source:46
تأكد_يساوي(عوامل[5], 5, "ثم خمسة")
# apl-source:47
تأكد_يساوي(عوامل[8], 13, "آخر عامل")
# apl-source:48

# apl-source:49
# تحقق من الجداء
# apl-source:50
جداء = 1
# apl-source:51
for ع in عوامل:
  # apl-source:52
  جداء = جداء * ع
# apl-source:53
تأكد_يساوي(جداء, 360360, "الجداء يعيد العدد")
# apl-source:54

# apl-source:55
عوامل_أولي = حلل_بالعجلة(99991)
# apl-source:56
print("عوامل 99991:", عوامل_أولي)
# apl-source:57
تأكد_يساوي(len(عوامل_أولي), 1, "عدد أولي يعيد نفسه")
# apl-source:58
تأكد_يساوي(عوامل_أولي[0], 99991, "العدد الأولي نفسه")
# apl-source:59
