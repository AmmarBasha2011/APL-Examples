
# apl-source:1
# مثال 602 — الجدول المتناثر
# apl-source:2
# Sparse table RMQ
# apl-source:3
# Demonstrates: جدول متناثر، أدنى مدى، تجهيز مسبق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/602-sparse-table.apl
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
# الجدول المتناثر: أدنى مدى بزمن ثابت بعد تجهيز
# apl-source:25
# Demonstrates: قوى اثنين, تجهيز مسبق, استعلام O(1) لدالة idempotent
# apl-source:26
# مناسب للمصفوفات الثابتة كثيرة الاستعلامات
# apl-source:27

# apl-source:28
أرقام = [4, 6, 1, 5, 7, 3, 9, 2]
# apl-source:29
ن = len(أرقام)
# apl-source:30
سجل = [0] * (ن + 1)
# apl-source:31
for ي in range(2, ن + 1):
  # apl-source:32
  سجل[ي] = سجل[ي // 2] + 1
# apl-source:33
أعمدة = سجل[ن] + 1
# apl-source:34

# apl-source:35
جدول = []
# apl-source:36
for ي in range(ن):
  # apl-source:37
  جدول.append([0] * أعمدة)
# apl-source:38
for ي in range(ن):
  # apl-source:39
  جدول[ي][0] = أرقام[ي]
# apl-source:40
for ع in range(1, أعمدة):
  # apl-source:41
  طول_القفزة = 2 ** ع
  # apl-source:42
  نصف = طول_القفزة // 2
  # apl-source:43
  for ي in range(ن - طول_القفزة + 1):
    # apl-source:44
    جدول[ي][ع] = min(جدول[ي][ع - 1], جدول[ي + نصف][ع - 1])
# apl-source:45

# apl-source:46
def أدنى_مدى(أ, ب):
  # apl-source:47
  ع = سجل[ب - أ + 1]
  # apl-source:48
  طول_القفزة = 2 ** ع
  # apl-source:49
  return min(جدول[أ][ع], جدول[ب - طول_القفزة + 1][ع])
# apl-source:50

# apl-source:51
تأكد_يساوي(أدنى_مدى(0, 7), 1, "أدنى الكل")
# apl-source:52
تأكد_يساوي(أدنى_مدى(3, 6), 3, "أدنى مدى وسطي")
# apl-source:53
تأكد_يساوي(أدنى_مدى(2, 2), 1, "عنصر واحد")
# apl-source:54
تأكد_يساوي(أدنى_مدى(5, 7), 2, "مدى أخير")
# apl-source:55
print("أدنى المدى 1-4:", أدنى_مدى(1, 4))
# apl-source:56
