
# apl-source:1
# مثال 748 — آلة إنجما
# apl-source:2
# Enigma machine lite
# apl-source:3
# Demonstrates: دوارات، عاكس، تنقل مزدوج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/748-enigma-lite.apl
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
# آلة إنجما I مبسطة: ثلاثة دوارات وعاكس
# apl-source:25
# Demonstrates: توصيلات دوارة, تنقّل مزدوج الخطوة, ذهاب وإياب عبر العاكس
# apl-source:26
# الدوارات I وII وIII والعاكس B بالتوصيلات التاريخية
# apl-source:27

# apl-source:28
دوار1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
# apl-source:29
دوار2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
# apl-source:30
دوار3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
# apl-source:31
عاكس = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
# apl-source:32
# نقاط تنقل كل دوار (موضع النافذة الذي يدفع التالي)
# apl-source:33
تنقل1 = 16
# apl-source:34
تنقل2 = 4
# apl-source:35
تنقل3 = 21
# apl-source:36

# apl-source:37
def عبر(دوار, حرف, إزاحة):
  # apl-source:38
  return (ord(دوار[(حرف + إزاحة) % 26]) - 65 - إزاحة) % 26
# apl-source:39

# apl-source:40
def عكس(دوار, حرف, إزاحة):
  # apl-source:41
  هدف = chr((حرف + إزاحة) % 26 + 65)
  # apl-source:42
  return (دوار.index(هدف) - إزاحة) % 26
# apl-source:43

# apl-source:44
def إنجما(نص, م1, م2, م3):
  # apl-source:45
  موضع1 = م1
  # apl-source:46
  موضع2 = م2
  # apl-source:47
  موضع3 = م3
  # apl-source:48
  ناتج = ""
  # apl-source:49
  for ي in range(len(نص)):
    # apl-source:50
    # التنقل: مزدوج الخطوة كالآلة الحقيقية
    # apl-source:51
    if موضع2 == تنقل2:
      # apl-source:52
      موضع1 = (موضع1 + 1) % 26
      # apl-source:53
      موضع2 = (موضع2 + 1) % 26
    # apl-source:54
    if موضع3 == تنقل3:
      # apl-source:55
      موضع2 = (موضع2 + 1) % 26
    # apl-source:56
    موضع3 = (موضع3 + 1) % 26
    # apl-source:57
    حرف = ord(نص[ي]) - 65
    # apl-source:58
    حرف = عبر(دوار3, حرف, موضع3)
    # apl-source:59
    حرف = عبر(دوار2, حرف, موضع2)
    # apl-source:60
    حرف = عبر(دوار1, حرف, موضع1)
    # apl-source:61
    حرف = ord(عاكس[حرف]) - 65
    # apl-source:62
    حرف = عكس(دوار1, حرف, موضع1)
    # apl-source:63
    حرف = عكس(دوار2, حرف, موضع2)
    # apl-source:64
    حرف = عكس(دوار3, حرف, موضع3)
    # apl-source:65
    ناتج = ناتج + chr(حرف + 65)
  # apl-source:66
  return ناتج
# apl-source:67

# apl-source:68
تأكد_يساوي(إنجما("AAAAA", 0, 0, 0), "BDZGO", "خمسة A تاريخية")
# apl-source:69
تأكد_يساوي(إنجما("HELLOWORLD", 0, 0, 0), "ILBDAAMTAZ", "تحية العالم")
# apl-source:70
تأكد_يساوي(إنجما(إنجما("HELLOWORLD", 0, 0, 0), 0, 0, 0), "HELLOWORLD", "التشفير عكس نفسه")
# apl-source:71
تأكد_يساوي(إنجما("AAA", 0, 0, 25), "UBD", "بدء من موضع مختلف")
# apl-source:72
تأكد_يساوي(len(إنجما("TESTING", 5, 7, 11)), 7, "الطول محفوظ")
# apl-source:73

# apl-source:74
print("AAAAA:", إنجما("AAAAA", 0, 0, 0))
# apl-source:75
