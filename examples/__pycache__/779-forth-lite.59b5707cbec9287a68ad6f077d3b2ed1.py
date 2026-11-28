
# apl-source:1
# مثال 779 — مفسر فورث
# apl-source:2
# Forth interpreter
# apl-source:3
# Demonstrates: مكدس RPN، تعريف كلمات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/779-forth-lite.apl
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
# مفسر فورث مصغر: مكدس، كلمات مدمجة، تعريفات جديدة
# apl-source:25
# Demonstrates: مكدس RPN, تعريف : اسم ... ;, إعادة استخدام الكلمات
# apl-source:26

# apl-source:27
def كلها_ارقام(س):
  # apl-source:28
  نتيجة = True
  # apl-source:29
  for حرف in س:
    # apl-source:30
    if حرف < "0" or حرف > "9":
      # apl-source:31
      نتيجة = False
  # apl-source:32
  return نتيجة
# apl-source:33

# apl-source:34
def نفذ(وحدات, مكدس, أسماء, أجسام, مخرجات):
  # apl-source:35
  ي = 0
  # apl-source:36
  while ي < len(وحدات):
    # apl-source:37
    وح = وحدات[ي]
    # apl-source:38
    if وح == ":":
      # apl-source:39
      أسماء.append(وحدات[ي + 1])
      # apl-source:40
      جسم = []
      # apl-source:41
      ي = ي + 2
      # apl-source:42
      while وحدات[ي] != ";":
        # apl-source:43
        جسم.append(وحدات[ي])
        # apl-source:44
        ي = ي + 1
      # apl-source:45
      أجسام.append(جسم)
    # apl-source:46
    elif وح == ".":
      # apl-source:47
      مخرجات.append(مكدس.pop())
    # apl-source:48
    elif وح == "dup":
      # apl-source:49
      مكدس.append(مكدس[len(مكدس) - 1])
    # apl-source:50
    elif وح == "drop":
      # apl-source:51
      مكدس.pop()
    # apl-source:52
    elif وح == "swap":
      # apl-source:53
      أ = مكدس.pop()
      # apl-source:54
      ب = مكدس.pop()
      # apl-source:55
      مكدس.append(أ)
      # apl-source:56
      مكدس.append(ب)
    # apl-source:57
    elif وح == "over":
      # apl-source:58
      مكدس.append(مكدس[len(مكدس) - 2])
    # apl-source:59
    elif وح == "+":
      # apl-source:60
      ب = مكدس.pop()
      # apl-source:61
      أ = مكدس.pop()
      # apl-source:62
      مكدس.append(أ + ب)
    # apl-source:63
    elif وح == "-":
      # apl-source:64
      ب = مكدس.pop()
      # apl-source:65
      أ = مكدس.pop()
      # apl-source:66
      مكدس.append(أ - ب)
    # apl-source:67
    elif وح == "*":
      # apl-source:68
      ب = مكدس.pop()
      # apl-source:69
      أ = مكدس.pop()
      # apl-source:70
      مكدس.append(أ * ب)
    # apl-source:71
    elif وح == "/":
      # apl-source:72
      ب = مكدس.pop()
      # apl-source:73
      أ = مكدس.pop()
      # apl-source:74
      مكدس.append(أ // ب)
    # apl-source:75
    elif كلها_ارقام(وح):
      # apl-source:76
      مكدس.append(int(وح))
    # apl-source:77
    elif وح in أسماء:
      # apl-source:78
      نفذ(أجسام[أسماء.index(وح)], مكدس, أسماء, أجسام, مخرجات)
    # apl-source:79
    ي = ي + 1
# apl-source:80

# apl-source:81
def فورث(برنامج):
  # apl-source:82
  مخرجات = []
  # apl-source:83
  نفذ(برنامج.split(" "), [], [], [], مخرجات)
  # apl-source:84
  return مخرجات
# apl-source:85

# apl-source:86
ن1 = فورث("3 4 + .")
# apl-source:87
تأكد_يساوي(ن1[0], 7, "جمع")
# apl-source:88
ن2 = فورث(": sq dup * ; 5 sq .")
# apl-source:89
تأكد_يساوي(ن2[0], 25, "كلمة معرفة")
# apl-source:90
ن3 = فورث("10 3 - 2 * .")
# apl-source:91
تأكد_يساوي(ن3[0], 14, "أولوية المكدس")
# apl-source:92
ن4 = فورث("1 2 swap - .")
# apl-source:93
تأكد_يساوي(ن4[0], 1, "swap")
# apl-source:94
ن5 = فورث("1 2 over + + .")
# apl-source:95
تأكد_يساوي(ن5[0], 4, "over")
# apl-source:96
ن6 = فورث(": avg + 2 / ; 3 9 avg .")
# apl-source:97
تأكد_يساوي(ن6[0], 6, "متوسط بكلمة")
# apl-source:98
ن7 = فورث("5 dup dup * * .")
# apl-source:99
تأكد_يساوي(ن7[0], 125, "تكعيب")
# apl-source:100
