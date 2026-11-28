
# apl-source:1
# مثال 664 — مشاركة سر شامير
# apl-source:2
# Shamir secret sharing
# apl-source:3
# Demonstrates: شامير، حقل منته، لاغرانج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/664-shamir-secret.apl
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
# مشاركة سر شامير (3 من 5)
# apl-source:25
# Demonstrates: كثيرة حدود على حقل منته, معكوس معياري, إدخال لاغرانج
# apl-source:26
# أي 3 حصص تكفي وأي 2 لا تكشف شيئا
# apl-source:27

# apl-source:28
أولي = 257
# apl-source:29
سر = 42
# apl-source:30

# apl-source:31
def باقي(س):
  # apl-source:32
  ن = س % أولي
  # apl-source:33
  if ن < 0:
    # apl-source:34
    ن = ن + أولي
  # apl-source:35
  return ن
# apl-source:36

# apl-source:37
def عكس(س):
  # apl-source:38
  ق = 1
  # apl-source:39
  أس = أولي - 2
  # apl-source:40
  قاعدة = س
  # apl-source:41
  while أس > 0:
    # apl-source:42
    if أس % 2 == 1:
      # apl-source:43
      ق = باقي(ق * قاعدة)
    # apl-source:44
    قاعدة = باقي(قاعدة * قاعدة)
    # apl-source:45
    أس = أس // 2
  # apl-source:46
  return ق
# apl-source:47

# apl-source:48
def قيمة_كثيرة(س):
  # apl-source:49
  return باقي(سر + 17 * س + 91 * س * س)
# apl-source:50

# apl-source:51
حصص = []
# apl-source:52
for س in range(1, 6):
  # apl-source:53
  حصص.append([س, قيمة_كثيرة(س)])
# apl-source:54

# apl-source:55
def استعد(ثلاث):
  # apl-source:56
  حاصل = 0
  # apl-source:57
  for ي in range(3):
    # apl-source:58
    بسط = 1
    # apl-source:59
    مقام = 1
    # apl-source:60
    for ج in range(3):
      # apl-source:61
      if ي != ج:
        # apl-source:62
        بسط = باقي(بسط * (0 - ثلاث[ج][0]))
        # apl-source:63
        مقام = باقي(مقام * (ثلاث[ي][0] - ثلاث[ج][0]))
    # apl-source:64
    حد = باقي(ثلاث[ي][1] * بسط * عكس(مقام))
    # apl-source:65
    حاصل = باقي(حاصل + حد)
  # apl-source:66
  return حاصل
# apl-source:67

# apl-source:68
تأكد_يساوي(استعد([حصص[0], حصص[2], حصص[4]]), سر, "حصص 1 و3 و5")
# apl-source:69
تأكد_يساوي(استعد([حصص[1], حصص[2], حصص[3]]), سر, "حصص 2 و3 و4")
# apl-source:70
تأكد_يساوي(استعد([حصص[0], حصص[1], حصص[2]]), سر, "حصص 1 و2 و3")
# apl-source:71
تأكد_يساوي(قيمة_كثيرة(1), باقي(150), "حصة أولى يدويا")
# apl-source:72
print("حصة 1:", حصص[0][1])
# apl-source:73
