
# apl-source:1
# مثال 822 — مولد PCG32
# apl-source:2
# PCG32
# apl-source:3
# Demonstrates: LCG 64-بت، تبديل إخراج دوار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/822-pcg-lite.apl
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
# مولد PCG32: مولد خطي 64-بت مع تبديل إخراج دوار
# apl-source:25
# Demonstrates: LCG عالي الجودة, XSH-RR, تهيئة ببذرة وتسلسل
# apl-source:26

# apl-source:27
م64 = 18446744073709551616
# apl-source:28

# apl-source:29
def بي_سي_جي(بذرة, تسلسل, عدد):
  # apl-source:30
  حالة = 0
  # apl-source:31
  زيادة = تسلسل * 2 + 1
  # apl-source:32
  حالة = (حالة * 6364136223846793005 + زيادة) % م64
  # apl-source:33
  حالة = (حالة + بذرة) % م64
  # apl-source:34
  ناتج = []
  # apl-source:35
  for ي in range(عدد + 1):
    # apl-source:36
    قديم = حالة
    # apl-source:37
    حالة = (قديم * 6364136223846793005 + زيادة) % م64
    # apl-source:38
    س = ((قديم >> 18) ^ قديم) >> 27
    # apl-source:39
    دوران = قديم >> 59
    # apl-source:40
    عكس = 32 - دوران
    # apl-source:41
    if دوران == 0:
      # apl-source:42
      ناتج.append(س)
    # apl-source:43
    else:
      # apl-source:44
      ناتج.append(((س >> دوران) | (س << عكس)) % 4294967296)
  # apl-source:45
  return ناتج
# apl-source:46

# apl-source:47
قيم = بي_سي_جي(42, 54, 3)
# apl-source:48
تأكد_يساوي(قيم[1], 3780903607, "أول قيمة")
# apl-source:49
تأكد_يساوي(قيم[2], 2068313097, "ثاني قيمة")
# apl-source:50
تأكد_يساوي(قيم[3], 3122508592, "ثالث قيمة")
# apl-source:51
تأكد_يساوي(len(قيم), 4, "تهيئة زائد ثلاث")
# apl-source:52
قيم2 = بي_سي_جي(42, 55, 1)
# apl-source:53
تأكد_يساوي(قيم2[1] != قيم[1] == False, False, "تسلسل مختلف يغير الناتج")
# apl-source:54
