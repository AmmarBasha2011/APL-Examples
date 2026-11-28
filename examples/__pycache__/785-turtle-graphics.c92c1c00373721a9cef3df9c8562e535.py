
# apl-source:1
# مثال 785 — رسوم السلحفاة
# apl-source:2
# Turtle graphics
# apl-source:3
# Demonstrates: اتجاه مدوّر، شبكة نصية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/785-turtle-graphics.apl
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
# رسوم السلحفاة على شبكة نصية: F أمام، R يمين، L يسار
# apl-source:25
# Demonstrates: متجه اتجاه مدوّر, رسم على شبكة, إخراج أسطر
# apl-source:26

# apl-source:27
def سلحفاة(أوامر, عرض, ارتفاع):
  # apl-source:28
  شبكة = []
  # apl-source:29
  for ي in range(ارتفاع):
    # apl-source:30
    صف = []
    # apl-source:31
    for ج in range(عرض):
      # apl-source:32
      صف.append(" ")
    # apl-source:33
    شبكة.append(صف)
  # apl-source:34
  س = 0
  # apl-source:35
  ص = 0
  # apl-source:36
  دس = 1
  # apl-source:37
  دص = 0
  # apl-source:38
  صف0 = شبكة[0]
  # apl-source:39
  صف0[0] = "*"
  # apl-source:40
  for أمر in أوامر:
    # apl-source:41
    if أمر == "F":
      # apl-source:42
      س = س + دس
      # apl-source:43
      ص = ص + دص
      # apl-source:44
      if س >= 0 and س < عرض and ص >= 0 and ص < ارتفاع:
        # apl-source:45
        صف = شبكة[ص]
        # apl-source:46
        صف[س] = "*"
    # apl-source:47
    elif أمر == "R":
      # apl-source:48
      مؤقت = دس
      # apl-source:49
      دس = 0 - دص
      # apl-source:50
      دص = مؤقت
    # apl-source:51
    elif أمر == "L":
      # apl-source:52
      مؤقت = دس
      # apl-source:53
      دس = دص
      # apl-source:54
      دص = 0 - مؤقت
  # apl-source:55
  أسطر = []
  # apl-source:56
  for ي in range(ارتفاع):
    # apl-source:57
    سطر = ""
    # apl-source:58
    for خلية in شبكة[ي]:
      # apl-source:59
      سطر = سطر + خلية
    # apl-source:60
    أسطر.append(سطر)
  # apl-source:61
  return أسطر
# apl-source:62

# apl-source:63
ن = سلحفاة("FFRFFLFF", 5, 3)
# apl-source:64
تأكد_يساوي(ن[0], "***  ", "صف أول")
# apl-source:65
تأكد_يساوي(ن[1], "  *  ", "صف ثان")
# apl-source:66
تأكد_يساوي(ن[2], "  ***", "صف ثالث")
# apl-source:67
ن2 = سلحفاة("FRFRFRF", 2, 2)
# apl-source:68
تأكد_يساوي(ن2[0], "**", "مربع صف أول")
# apl-source:69
تأكد_يساوي(ن2[1], "**", "مربع صف ثان")
# apl-source:70
ن3 = سلحفاة("FFRFF", 3, 2)
# apl-source:71
تأكد_يساوي(ن3[0], "***", "زاوية أعلى")
# apl-source:72
تأكد_يساوي(ن3[1], "  *", "زاوية أسفل")
# apl-source:73
