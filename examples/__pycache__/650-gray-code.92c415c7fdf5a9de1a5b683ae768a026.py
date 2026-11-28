
# apl-source:1
# مثال 650 — شفرة جراي
# apl-source:2
# Gray code
# apl-source:3
# Demonstrates: شفرة جراي، بت واحد، دورة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/650-gray-code.apl
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
# شفرة جراي: تتابع يختلف في بت واحد
# apl-source:25
# Demonstrates: صيغة ي ^ (ي >> 1), خاصية الجوار, دورة مغلقة
# apl-source:26
# ترتيب يقلل الأخطاء في المشفرات الدوارة
# apl-source:27

# apl-source:28
def عد_البتات(س):
  # apl-source:29
  عدد = 0
  # apl-source:30
  while س > 0:
    # apl-source:31
    عدد = عدد + س % 2
    # apl-source:32
    س = س // 2
  # apl-source:33
  return عدد
# apl-source:34

# apl-source:35
ن = 3
# apl-source:36
رمز = []
# apl-source:37
for ي in range(2 ** ن):
  # apl-source:38
  رمز.append(ي ^ (ي // 2))
# apl-source:39
تأكد_يساوي(رمز, [0, 1, 3, 2, 6, 7, 5, 4], "شفرة جراي لثلاثة بتات")
# apl-source:40
for ي in range(len(رمز) - 1):
  # apl-source:41
  تأكد_يساوي(عد_البتات(رمز[ي] ^ رمز[ي + 1]), 1, "بت واحد بين متتاليتين")
# apl-source:42
تأكد_يساوي(عد_البتات(رمز[0] ^ رمز[len(رمز) - 1]), 1, "الدورة مغلقة")
# apl-source:43
print("الشفرة:", رمز)
# apl-source:44
