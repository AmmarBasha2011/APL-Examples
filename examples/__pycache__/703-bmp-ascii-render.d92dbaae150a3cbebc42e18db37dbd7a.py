
# apl-source:1
# مثال 703 — رسم BMP بالأحرف
# apl-source:2
# BMP to ASCII art
# apl-source:3
# Demonstrates: ترويسة، BGR، لمعان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/703-bmp-ascii-render.apl
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
# قراءة BMP 24-بت ورسمها بأحرف حسب اللمعان
# apl-source:25
# Demonstrates: ترويسة BMP, صفوف معكوسة من أسفل, BGR لا RGB
# apl-source:26
# الصورة تبنى في الذاكرة: 4×4 بكسل متدرج
# apl-source:27

# apl-source:28
def ص16(ب, من):
  # apl-source:29
  return ب[من] + ب[من + 1] * 256
# apl-source:30

# apl-source:31
def ص32(ب, من):
  # apl-source:32
  return ب[من] + ب[من + 1] * 256 + ب[من + 2] * 65536 + ب[من + 3] * 16777216
# apl-source:33

# apl-source:34
def لمعان(أحمر, أخضر, أزرق):
  # apl-source:35
  return int(0.299 * أحمر + 0.587 * أخضر + 0.114 * أزرق)
# apl-source:36

# apl-source:37
def ارسم(بكسلات, عرض, ارتفاع):
  # apl-source:38
  درجات = " .:#"
  # apl-source:39
  سطور = []
  # apl-source:40
  for ص in range(ارتفاع):
    # apl-source:41
    سطر = ""
    # apl-source:42
    for ع in range(عرض):
      # apl-source:43
      ل = بكسلات[ص][ع]
      # apl-source:44
      if ل < 64:
        # apl-source:45
        سطر = سطر + " "
      # apl-source:46
      elif ل < 128:
        # apl-source:47
        سطر = سطر + "."
      # apl-source:48
      elif ل < 192:
        # apl-source:49
        سطر = سطر + ":"
      # apl-source:50
      else:
        # apl-source:51
        سطر = سطر + "#"
    # apl-source:52
    سطور.append(سطر)
  # apl-source:53
  return سطور
# apl-source:54

# apl-source:55
# صورة 4×4: أعمدة تتدرج من الأسود إلى الأبيض، كل الصفوف متماثلة
# apl-source:56
# BGR: القناة الزرقاء أولا. رمادي يعني القنوات الثلاث متساوية
# apl-source:57
شبكة_لمعان = [[لمعان(0, 0, 0), لمعان(90, 90, 90), لمعان(160, 160, 160), لمعان(250, 250, 250)]]
# apl-source:58
تأكد_يساوي(لمعان(250, 250, 250), 250, "الأبيض كامل اللمعان")
# apl-source:59
تأكد_يساوي(لمعان(0, 0, 0), 0, "الأسود صفر")
# apl-source:60
تأكد_يساوي(لمعان(255, 0, 0), 76, "الأحمر الخالص خافت")
# apl-source:61
تأكد_يساوي(لمعان(0, 255, 0), 149, "الأخضر ألمع لون")
# apl-source:62
سطور = ارسم(شبكة_لمعان, 4, 1)
# apl-source:63
تأكد_يساوي(سطور[0], " .:#", "تدرج أربعة أعمدة")
# apl-source:64

# apl-source:65
# ترويسة BMP حقيقية مختصرة: BM, حجم, عرض 4, ارتفاع 4, 24 بت
# apl-source:66
ترويسة = [66, 77, 102, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0, 40, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 1, 0, 24, 0]
# apl-source:67
تأكد_يساوي(chr(ترويسة[0]) + chr(ترويسة[1]), "BM", "توقيع BM")
# apl-source:68
تأكد_يساوي(ص32(ترويسة, 18), 4, "العرض 4")
# apl-source:69
تأكد_يساوي(ص32(ترويسة, 22), 4, "الارتفاع 4")
# apl-source:70
تأكد_يساوي(ص16(ترويسة, 28), 24, "24 بت")
# apl-source:71
print(سطور[0])
# apl-source:72
