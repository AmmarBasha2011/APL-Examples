
# apl-source:1
# مثال 747 — تشفير بلايفير
# apl-source:2
# Playfair cipher
# apl-source:3
# Demonstrates: مربع 5x5، أزواج، ثلاث قواعد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/747-playfair-lite.apl
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
# تشفير بلايفير: مربع 5x5 وقواعد الصف والعمود والمستطيل
# apl-source:25
# Demonstrates: بناء مربع مفتاح, أزواج حروف مع حشو X, ثلاث قواعد
# apl-source:26
# J تدمج في I، والأزواج المتساوية يفصلها X
# apl-source:27

# apl-source:28
def مربع_مفتاح(مفتاح):
  # apl-source:29
  مربع = ""
  # apl-source:30
  for ي in range(len(مفتاح)):
    # apl-source:31
    حرف = مفتاح[ي]
    # apl-source:32
    if حرف == "J":
      # apl-source:33
      حرف = "I"
    # apl-source:34
    if حرف >= "A" and حرف <= "Z":
      # apl-source:35
      if حرف in مربع:
        # apl-source:36
        حرف = ""
      # apl-source:37
      مربع = مربع + حرف
  # apl-source:38
  أبجدية = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  # apl-source:39
  for ي in range(25):
    # apl-source:40
    if أبجدية[ي] in مربع:
      # apl-source:41
      مربع = مربع + ""
    # apl-source:42
    else:
      # apl-source:43
      مربع = مربع + أبجدية[ي]
  # apl-source:44
  return مربع
# apl-source:45

# apl-source:46
def جهز(نص):
  # apl-source:47
  مهيأ = ""
  # apl-source:48
  for ي in range(len(نص)):
    # apl-source:49
    حرف = نص[ي]
    # apl-source:50
    if حرف >= "a" and حرف <= "z":
      # apl-source:51
      حرف = نص.upper()[ي]
    # apl-source:52
    if حرف == "J":
      # apl-source:53
      حرف = "I"
    # apl-source:54
    if حرف >= "A" and حرف <= "Z":
      # apl-source:55
      مهيأ = مهيأ + حرف
  # apl-source:56
  return مهيأ
# apl-source:57

# apl-source:58
def شفر_بلايفير(نص, مفتاح):
  # apl-source:59
  مربع = مربع_مفتاح(مفتاح)
  # apl-source:60
  مهيأ = جهز(نص)
  # apl-source:61
  ناتج = ""
  # apl-source:62
  ي = 0
  # apl-source:63
  while ي < len(مهيأ):
    # apl-source:64
    أ = مهيأ[ي]
    # apl-source:65
    if ي + 1 < len(مهيأ):
      # apl-source:66
      ب = مهيأ[ي + 1]
    # apl-source:67
    else:
      # apl-source:68
      ب = "X"
    # apl-source:69
    if أ == ب:
      # apl-source:70
      ب = "X"
      # apl-source:71
      ي = ي - 1
    # apl-source:72
    موضع_أ = مربع.index(أ)
    # apl-source:73
    موضع_ب = مربع.index(ب)
    # apl-source:74
    صف_أ = موضع_أ // 5
    # apl-source:75
    عمود_أ = موضع_أ % 5
    # apl-source:76
    صف_ب = موضع_ب // 5
    # apl-source:77
    عمود_ب = موضع_ب % 5
    # apl-source:78
    if صف_أ == صف_ب:
      # apl-source:79
      ناتج = ناتج + مربع[صف_أ * 5 + (عمود_أ + 1) % 5] + مربع[صف_ب * 5 + (عمود_ب + 1) % 5]
    # apl-source:80
    elif عمود_أ == عمود_ب:
      # apl-source:81
      ناتج = ناتج + مربع[((صف_أ + 1) % 5) * 5 + عمود_أ] + مربع[((صف_ب + 1) % 5) * 5 + عمود_ب]
    # apl-source:82
    else:
      # apl-source:83
      ناتج = ناتج + مربع[صف_أ * 5 + عمود_ب] + مربع[صف_ب * 5 + عمود_أ]
    # apl-source:84
    ي = ي + 2
  # apl-source:85
  return ناتج
# apl-source:86

# apl-source:87
تأكد_يساوي(مربع_مفتاح("PLAYFAIREXAMPLE"), "PLAYFIREXMBCDGHKNOQSTUVWZ", "مربع المفتاح الكلاسيكي")
# apl-source:88
تأكد_يساوي(شفر_بلايفير("Hide the gold in the tree stump", "PLAYFAIREXAMPLE"), "BMODZBXDNABEKUDMUIXMMOUVIF", "المتجه الكلاسيكي")
# apl-source:89
تأكد_يساوي(شفر_بلايفير("BALLOON", "MONARCHY"), "IBSUPMNA", "بالون بمفتاح موناركي")
# apl-source:90
تأكد_يساوي(جهز("Hello, World!"), "HELLOWORLD", "تنقية الإدخال")
# apl-source:91

# apl-source:92
print("التشفير:", شفر_بلايفير("INSTRUMENTS", "MONARCHY"))
# apl-source:93
