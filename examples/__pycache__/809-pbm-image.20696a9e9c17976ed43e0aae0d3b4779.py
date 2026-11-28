
# apl-source:1
# مثال 809 — صورة PBM
# apl-source:2
# PBM image
# apl-source:3
# Demonstrates: نسق P1 نصي، إطار، تحليل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/809-pbm-image.apl
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
# صورة نقطية PBM بنسق P1 النصي: كتابة الرأس والبتات وقراءتها
# apl-source:25
# Demonstrates: تنسيق netpbm النصي, إطار حدود, تحليل عكسي
# apl-source:26

# apl-source:27
def إطار(عرض, ارتفاع):
  # apl-source:28
  شبكة = []
  # apl-source:29
  for ص in range(ارتفاع):
    # apl-source:30
    سطر = []
    # apl-source:31
    for ع in range(عرض):
      # apl-source:32
      if ص == 0 or ص == ارتفاع - 1 or ع == 0 or ع == عرض - 1:
        # apl-source:33
        سطر.append(1)
      # apl-source:34
      else:
        # apl-source:35
        سطر.append(0)
    # apl-source:36
    شبكة.append(سطر)
  # apl-source:37
  return شبكة
# apl-source:38

# apl-source:39
def إلى_pbm(شبكة):
  # apl-source:40
  مخرج = "P1\n" + str(len(شبكة[0])) + " " + str(len(شبكة)) + "\n"
  # apl-source:41
  for سطر in شبكة:
    # apl-source:42
    خلايا = []
    # apl-source:43
    for خلية in سطر:
      # apl-source:44
      خلايا.append(str(خلية))
    # apl-source:45
    مخرج = مخرج + " ".join(خلايا) + "\n"
  # apl-source:46
  return مخرج
# apl-source:47

# apl-source:48
def من_pbm(مدخل):
  # apl-source:49
  أسطر = مدخل.split("\n")
  # apl-source:50
  أبعاد = أسطر[1].split(" ")
  # apl-source:51
  شبكة = []
  # apl-source:52
  for ي in range(2, 2 + int(أبعاد[1])):
    # apl-source:53
    سطر = []
    # apl-source:54
    for خلية in أسطر[ي].split(" "):
      # apl-source:55
      سطر.append(int(خلية))
    # apl-source:56
    شبكة.append(سطر)
  # apl-source:57
  return شبكة
# apl-source:58

# apl-source:59
شبكة = إطار(8, 6)
# apl-source:60
تأكد_يساوي(شبكة[0], [1, 1, 1, 1, 1, 1, 1, 1], "الحد العلوي")
# apl-source:61
تأكد_يساوي(شبكة[2], [1, 0, 0, 0, 0, 0, 0, 1], "سطر وسطي")
# apl-source:62
مشفر = إلى_pbm(شبكة)
# apl-source:63
تأكد_يساوي(مشفر.split("\n")[0], "P1", "رقم سحري")
# apl-source:64
تأكد_يساوي(مشفر.split("\n")[1], "8 6", "الأبعاد")
# apl-source:65
مفكوك = من_pbm(مشفر)
# apl-source:66
تأكد_يساوي(مفكوك, شبكة, "دورة كاملة")
# apl-source:67
مجموع = 0
# apl-source:68
for سطر in شبكة:
  # apl-source:69
  for خلية in سطر:
    # apl-source:70
    مجموع = مجموع + خلية
# apl-source:71
تأكد_يساوي(مجموع, 24, "عدد بتات الإطار")
# apl-source:72
