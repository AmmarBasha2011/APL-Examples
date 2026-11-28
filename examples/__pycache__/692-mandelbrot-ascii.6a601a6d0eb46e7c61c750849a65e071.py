
# apl-source:1
# مثال 692 — ماندلبروت نصي
# apl-source:2
# ASCII Mandelbrot
# apl-source:3
# Demonstrates: فركتلات، هروب، خريطة أحرف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/692-mandelbrot-ascii.apl
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
# مجموعة ماندلبروت برسم نصي
# apl-source:25
# Demonstrates: تكرار z=z^2+c بفصل الحقيقي والتخيلي, حد الهروب 4, خريطة أحرف
# apl-source:26
# النقطة 0+0i لا تهرب أبدا، والبعيدة تهرب فورا
# apl-source:27

# apl-source:28
def هروب(ج_حقيقي, ج_تخيلي, أقصى):
  # apl-source:29
  زر = 0.0
  # apl-source:30
  زي = 0.0
  # apl-source:31
  for ي in range(أقصى):
    # apl-source:32
    if زر * زر + زي * زي > 4.0:
      # apl-source:33
      return ي
    # apl-source:34
    زر2 = زر * زر - زي * زي + ج_حقيقي
    # apl-source:35
    زي = 2.0 * زر * زي + ج_تخيلي
    # apl-source:36
    زر = زر2
  # apl-source:37
  return أقصى
# apl-source:38

# apl-source:39
عرض = 41
# apl-source:40
ارتفاع = 17
# apl-source:41
أقصى = 30
# apl-source:42
سوداء = 0
# apl-source:43
صفوف = []
# apl-source:44
for ص in range(ارتفاع):
  # apl-source:45
  سطر = ""
  # apl-source:46
  for ع in range(عرض):
    # apl-source:47
    ج_حقيقي = -2.0 + 2.5 * ع / (عرض - 1)
    # apl-source:48
    ج_تخيلي = -1.0 + 2.0 * ص / (ارتفاع - 1)
    # apl-source:49
    if هروب(ج_حقيقي, ج_تخيلي, أقصى) >= أقصى:
      # apl-source:50
      سطر = سطر + "#"
      # apl-source:51
      سوداء = سوداء + 1
    # apl-source:52
    else:
      # apl-source:53
      سطر = سطر + " "
  # apl-source:54
  صفوف.append(سطر)
# apl-source:55

# apl-source:56
تأكد_يساوي(هروب(0.0, 0.0, أقصى), أقصى, "الصفر لا يهرب")
# apl-source:57
تأكد_يساوي(هروب(2.0, 2.0, أقصى), 1, "البعيدة تهرب فورا")
# apl-source:58
تأكد_يساوي(هروب(-1.0, 0.0, أقصى), أقصى, "ناقص واحد داخل المجموعة")
# apl-source:59
وسط = صفوف[8]
# apl-source:60
تأكد_يساوي(وسط[16], "#", "قلب قلب المجموعة أسود")
# apl-source:61
تأكد_يساوي(صفوف[0][0], " ", "الزاوية العليا بيضاء")
# apl-source:62
تأكد_يساوي(سوداء, 221, "مساحة المجموعة بهذا القرار")
# apl-source:63
for سطر in صفوف:
  # apl-source:64
  print(سطر)
# apl-source:65
print("نقاط داخلية:", سوداء)
# apl-source:66
