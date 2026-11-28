
# apl-source:1
# مثال 802 — ساحة المناورة
# apl-source:2
# Shunting-yard
# apl-source:3
# Demonstrates: مكدس أولويات، RPN، أقواس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/802-shunting-yard.apl
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
# خوارزمية ساحة المناورة لدايكسترا: من infix إلى postfix ثم تقييم
# apl-source:25
# Demonstrates: مكدس عوامل بأولوية, أقواس, تقييم RPN بمكدس
# apl-source:26

# apl-source:27
def أولوية(ع):
  # apl-source:28
  if ع == "*" or ع == "/":
    # apl-source:29
    return 2
  # apl-source:30
  if ع == "+" or ع == "-":
    # apl-source:31
    return 1
  # apl-source:32
  return 0
# apl-source:33

# apl-source:34
def إلى_لاحق(رموز):
  # apl-source:35
  ناتج = []
  # apl-source:36
  مكدس = []
  # apl-source:37
  for رمز in رموز:
    # apl-source:38
    if رمز == "(":
      # apl-source:39
      مكدس.append(رمز)
    # apl-source:40
    elif رمز == ")":
      # apl-source:41
      while مكدس[len(مكدس) - 1] != "(":
        # apl-source:42
        ناتج.append(مكدس.pop())
      # apl-source:43
      مكدس.pop()
    # apl-source:44
    elif رمز == "+" or رمز == "-" or رمز == "*" or رمز == "/":
      # apl-source:45
      while len(مكدس) > 0 and أولوية(مكدس[len(مكدس) - 1]) >= أولوية(رمز):
        # apl-source:46
        ناتج.append(مكدس.pop())
      # apl-source:47
      مكدس.append(رمز)
    # apl-source:48
    else:
      # apl-source:49
      ناتج.append(رمز)
  # apl-source:50
  while len(مكدس) > 0:
    # apl-source:51
    ناتج.append(مكدس.pop())
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
def قيّم(لاحق):
  # apl-source:55
  مكدس = []
  # apl-source:56
  for رمز in لاحق:
    # apl-source:57
    if رمز == "+" or رمز == "-" or رمز == "*" or رمز == "/":
      # apl-source:58
      ب = مكدس.pop()
      # apl-source:59
      أ = مكدس.pop()
      # apl-source:60
      if رمز == "+":
        # apl-source:61
        مكدس.append(أ + ب)
      # apl-source:62
      elif رمز == "-":
        # apl-source:63
        مكدس.append(أ - ب)
      # apl-source:64
      elif رمز == "*":
        # apl-source:65
        مكدس.append(أ * ب)
      # apl-source:66
      else:
        # apl-source:67
        مكدس.append(أ // ب)
    # apl-source:68
    else:
      # apl-source:69
      مكدس.append(int(رمز))
  # apl-source:70
  return مكدس[0]
# apl-source:71

# apl-source:72
تأكد_يساوي(إلى_لاحق("3 + 4 * 2 - ( 1 + 2 )".split(" ")), ["3", "4", "2", "*", "+", "1", "2", "+", "-"], "تحويل لاحق")
# apl-source:73
تأكد_يساوي(إلى_لاحق("2 * ( 3 + 4 )".split(" ")), ["2", "3", "4", "+", "*"], "أقواس")
# apl-source:74
تأكد_يساوي(قيّم(إلى_لاحق("3 + 4 * 2 - ( 1 + 2 )".split(" "))), 8, "تقييم الأول")
# apl-source:75
تأكد_يساوي(قيّم(إلى_لاحق("2 * ( 3 + 4 )".split(" "))), 14, "تقييم الثاني")
# apl-source:76
تأكد_يساوي(قيّم(إلى_لاحق("10 / 4 + 6 * 2".split(" "))), 14, "قسمة صحيحة")
# apl-source:77
