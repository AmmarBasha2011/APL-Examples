
# apl-source:1
# مثال 1792 — أعداد أرمسترونغ تحت حد
# apl-source:2
# Armstrong numbers below limit
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1792-armstrong-numbers-below.apl
# apl-source:6

# apl-source:7
# نحسب عدد الأرقام
# apl-source:8
# نقارن المجموع بالعدد
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
def أرمسترونغ(ن):
  # apl-source:19
  أرقام = []
  # apl-source:20
  ك = ن
  # apl-source:21
  while ك > 0:
    # apl-source:22
    أرقام.append(ك % 10)
    # apl-source:23
    ك = ك // 10
  # apl-source:24
  عدد = len(أرقام)
  # apl-source:25
  مجموع = 0
  # apl-source:26
  for ر in أرقام:
    # apl-source:27
    مجموع = مجموع + ر ** عدد
  # apl-source:28
  return مجموع == ن
# apl-source:29

# apl-source:30
def قائمة_أرمسترونغ(حد):
  # apl-source:31
  ناتج = []
  # apl-source:32
  for ن in range(1, حد):
    # apl-source:33
    if أرمسترونغ(ن):
      # apl-source:34
      ناتج.append(ن)
  # apl-source:35
  return ناتج
# apl-source:36

# apl-source:37
تأكد_يساوي(قائمة_أرمسترونغ(10), [1, 2, 3, 4, 5, 6, 7, 8, 9], "رقم واحد")
# apl-source:38
تأكد_يساوي(قائمة_أرمسترونغ(500), [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407], "حتى 500")
# apl-source:39
