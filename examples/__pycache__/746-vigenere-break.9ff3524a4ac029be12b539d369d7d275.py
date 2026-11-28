
# apl-source:1
# مثال 746 — كسر فيجنير
# apl-source:2
# Vigenère cryptanalysis
# apl-source:3
# Demonstrates: أعمدة، كاي تربيع، استعادة مفتاح
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/746-vigenere-break.apl
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
# كسر تشفير فيجنير بتحليل الأعمدة (طول المفتاح معلوم)
# apl-source:25
# Demonstrates: تقسيم أعمدة, كاي تربيع ضد تكرارات الإنجليزية, استعادة المفتاح
# apl-source:26
# كل عمود هو تشفير قيصر مستقل فيكفي أفضل إزاحة لكل عمود
# apl-source:27

# apl-source:28
تكرارات = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4,
           # apl-source:29
           6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]
# apl-source:30

# apl-source:31
def أفضل_إزاحة(عمود):
  # apl-source:32
  ن = len(عمود)
  # apl-source:33
  أفضل = 0
  # apl-source:34
  أدنى = 1000000.0
  # apl-source:35
  for إزاحة in range(26):
    # apl-source:36
    كاي = 0.0
    # apl-source:37
    for حرف in range(26):
      # apl-source:38
      مرصود = 0
      # apl-source:39
      for ي in range(ن):
        # apl-source:40
        if (ord(عمود[ي]) - 97 - إزاحة) % 26 == حرف:
          # apl-source:41
          مرصود = مرصود + 1
      # apl-source:42
      متوقع = ن * تكرارات[حرف] / 100.0
      # apl-source:43
      فرق = مرصود - متوقع
      # apl-source:44
      كاي = كاي + فرق * فرق / (متوقع + 0.01)
    # apl-source:45
    if كاي < أدنى:
      # apl-source:46
      أدنى = كاي
      # apl-source:47
      أفضل = إزاحة
  # apl-source:48
  return أفضل
# apl-source:49

# apl-source:50
def اكسر(مشفر, طول_مفتاح):
  # apl-source:51
  مفتاح = ""
  # apl-source:52
  for عمود in range(طول_مفتاح):
    # apl-source:53
    حروف = ""
    # apl-source:54
    ي = عمود
    # apl-source:55
    while ي < len(مشفر):
      # apl-source:56
      حروف = حروف + مشفر[ي]
      # apl-source:57
      ي = ي + طول_مفتاح
    # apl-source:58
    مفتاح = مفتاح + chr(أفضل_إزاحة(حروف) + 97)
  # apl-source:59
  return مفتاح
# apl-source:60

# apl-source:61
def فك_فيجنير(مشفر, مفتاح):
  # apl-source:62
  ناتج = ""
  # apl-source:63
  for ي in range(len(مشفر)):
    # apl-source:64
    إزاحة = ord(مفتاح[ي % len(مفتاح)]) - 97
    # apl-source:65
    ناتج = ناتج + chr((ord(مشفر[ي]) - 97 - إزاحة) % 26 + 97)
  # apl-source:66
  return ناتج
# apl-source:67

# apl-source:68
مشفر = "txiofelqprdxatgtqqgveamggsiicedxatgtqqgveamggsimurzjiwfosywgheehupessbqjacytwtbrdwuhjlwfvrptaquzjnsytirwgheehupibcpssrwanvqrhwmfmveamggsiesndszcswmsvgtxiofelqgrlwabbqhmfxyiegveamggsiedetrscsssbsveamggsiiwaeidcsoiedntvisulhqjrccfvvyknsszvqifhitoqysfvvyknsszvqif"
# apl-source:69

# apl-source:70
مفتاح = اكسر(مشفر, 5)
# apl-source:71
تأكد_يساوي(مفتاح, "lemon", "المفتاح المكتشف")
# apl-source:72
مستعاد = فك_فيجنير(مشفر, مفتاح)
# apl-source:73
تأكد_يساوي(مستعاد[0:12], "itwasthebest", "بداية النص المستعاد")
# apl-source:74
تأكد_يساوي(len(مستعاد), len(مشفر), "الطول محفوظ")
# apl-source:75

# apl-source:76
# نص قصير بمفتاح قصير آخر
# apl-source:77
def شفر_فيجنير(نص, مفتاح):
  # apl-source:78
  ناتج = ""
  # apl-source:79
  for ي in range(len(نص)):
    # apl-source:80
    إزاحة = ord(مفتاح[ي % len(مفتاح)]) - 97
    # apl-source:81
    ناتج = ناتج + chr((ord(نص[ي]) - 97 + إزاحة) % 26 + 97)
  # apl-source:82
  return ناتج
# apl-source:83

# apl-source:84
تأكد_يساوي(فك_فيجنير(شفر_فيجنير("hellohellohello", "abc"), "abc"), "hellohellohello", "ذهاب وإياب")
# apl-source:85

# apl-source:86
print("المفتاح:", مفتاح)
# apl-source:87
