
# apl-source:1
# مثال 836 — شجرة سبلاي
# apl-source:2
# Splay tree
# apl-source:3
# Demonstrates: زج-زج وزج-زاج، رفع للجذر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/836-splay-tree.apl
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
# شجرة سبلاي: كل وصول يرفع العقدة للجذر بمناورات زج-زج وزج-زاج
# apl-source:25
# Demonstrates: دورانات, رفع عودي, إدخال بعد الرفع, شجرة [مفتاح, يسار, يمين]
# apl-source:26

# apl-source:27
فارغ = 0
# apl-source:28

# apl-source:29
def دوران_يمين(عقدة):
  # apl-source:30
  فرع = عقدة[1]
  # apl-source:31
  عقدة[1] = فرع[2]
  # apl-source:32
  فرع[2] = عقدة
  # apl-source:33
  return فرع
# apl-source:34

# apl-source:35
def دوران_يسار(عقدة):
  # apl-source:36
  فرع = عقدة[2]
  # apl-source:37
  عقدة[2] = فرع[1]
  # apl-source:38
  فرع[1] = عقدة
  # apl-source:39
  return فرع
# apl-source:40

# apl-source:41
def ارفع(جذر, مفتاح):
  # apl-source:42
  if جذر == فارغ or جذر[0] == مفتاح:
    # apl-source:43
    return جذر
  # apl-source:44
  if مفتاح < جذر[0]:
    # apl-source:45
    if جذر[1] == فارغ:
      # apl-source:46
      return جذر
    # apl-source:47
    if مفتاح < جذر[1][0]:
      # apl-source:48
      جذر[1][1] = ارفع(جذر[1][1], مفتاح)
      # apl-source:49
      جذر = دوران_يمين(جذر)
    # apl-source:50
    elif مفتاح > جذر[1][0]:
      # apl-source:51
      جذر[1][2] = ارفع(جذر[1][2], مفتاح)
      # apl-source:52
      if جذر[1][2] != فارغ:
        # apl-source:53
        جذر[1] = دوران_يسار(جذر[1])
    # apl-source:54
    if جذر[1] == فارغ:
      # apl-source:55
      return جذر
    # apl-source:56
    return دوران_يمين(جذر)
  # apl-source:57
  else:
    # apl-source:58
    if جذر[2] == فارغ:
      # apl-source:59
      return جذر
    # apl-source:60
    if مفتاح > جذر[2][0]:
      # apl-source:61
      جذر[2][2] = ارفع(جذر[2][2], مفتاح)
      # apl-source:62
      جذر = دوران_يسار(جذر)
    # apl-source:63
    elif مفتاح < جذر[2][0]:
      # apl-source:64
      جذر[2][1] = ارفع(جذر[2][1], مفتاح)
      # apl-source:65
      if جذر[2][1] != فارغ:
        # apl-source:66
        جذر[2] = دوران_يمين(جذر[2])
    # apl-source:67
    if جذر[2] == فارغ:
      # apl-source:68
      return جذر
    # apl-source:69
    return دوران_يسار(جذر)
# apl-source:70

# apl-source:71
def أدخل(جذر, مفتاح):
  # apl-source:72
  if جذر == فارغ:
    # apl-source:73
    return [مفتاح, فارغ, فارغ]
  # apl-source:74
  جذر = ارفع(جذر, مفتاح)
  # apl-source:75
  if جذر[0] == مفتاح:
    # apl-source:76
    return جذر
  # apl-source:77
  عقدة = [مفتاح, فارغ, فارغ]
  # apl-source:78
  if مفتاح < جذر[0]:
    # apl-source:79
    عقدة[2] = جذر
    # apl-source:80
    عقدة[1] = جذر[1]
    # apl-source:81
    جذر[1] = فارغ
  # apl-source:82
  else:
    # apl-source:83
    عقدة[1] = جذر
    # apl-source:84
    عقدة[2] = جذر[2]
    # apl-source:85
    جذر[2] = فارغ
  # apl-source:86
  return عقدة
# apl-source:87

# apl-source:88
شجرة = فارغ
# apl-source:89
for مفتاح in [10, 20, 30, 40, 50, 25]:
  # apl-source:90
  شجرة = أدخل(شجرة, مفتاح)
# apl-source:91
تأكد_يساوي(شجرة[0], 25, "آخر مدرج في الجذر")
# apl-source:92
تأكد_يساوي(شجرة[1][0], 20, "يسار الجذر")
# apl-source:93
شجرة = ارفع(شجرة, 10)
# apl-source:94
تأكد_يساوي(شجرة[0], 10, "رفع عشرة للجذر")
# apl-source:95
تأكد_يساوي(شجرة[1], فارغ, "لا يسار لعشرة")
# apl-source:96
تأكد_يساوي(شجرة[2][0], 20, "يمين الجذر")
# apl-source:97
