
# apl-source:1
# مثال 726 — أزواج UTF-16 البديلة
# apl-source:2
# UTF-16 surrogate pairs
# apl-source:3
# Demonstrates: بدائل عليا ودنيا، إزاحة، وحدات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/726-utf16-surrogates.apl
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
# أزواج UTF-16 البديلة للمحارف فوق BMP
# apl-source:25
# Demonstrates: قسمة إلى عالٍ وواطئ, إزاحة 0x10000, فك معكوس
# apl-source:26
# الإيموجي كلها فوق BMP: تحتاج زوجا بديلا
# apl-source:27

# apl-source:28
def إلى_بدائل(نقطة):
  # apl-source:29
  if نقطة < 65536:
    # apl-source:30
    return [نقطة]
  # apl-source:31
  ق = نقطة - 65536
  # apl-source:32
  عال = 55296 + ق // 1024
  # apl-source:33
  واطئ = 56320 + ق % 1024
  # apl-source:34
  return [عال, واطئ]
# apl-source:35

# apl-source:36
def من_بدائل(وحدات):
  # apl-source:37
  نقاط = []
  # apl-source:38
  ي = 0
  # apl-source:39
  while ي < len(وحدات):
    # apl-source:40
    وح = وحدات[ي]
    # apl-source:41
    if وح >= 55296 and وح < 56320:
      # apl-source:42
      نقاط.append(65536 + (وح - 55296) * 1024 + وحدات[ي + 1] - 56320)
      # apl-source:43
      ي = ي + 2
    # apl-source:44
    else:
      # apl-source:45
      نقاط.append(وح)
      # apl-source:46
      ي = ي + 1
  # apl-source:47
  return نقاط
# apl-source:48

# apl-source:49
تأكد_يساوي(إلى_بدائل(65), [65], "A ضمن BMP")
# apl-source:50
تأكد_يساوي(إلى_بدائل(1571), [1571], "ألف ضمن BMP")
# apl-source:51
تأكد_يساوي(إلى_بدائل(128512), [55357, 56832], "وجه ضاحك D83D DE00")
# apl-source:52
تأكد_يساوي(إلى_بدائل(65536), [55296, 56320], "أول نقطة فوق BMP")
# apl-source:53
تأكد_يساوي(إلى_بدائل(131069), [55359, 57341], "قرب النهاية")
# apl-source:54
تأكد_يساوي(من_بدائل([55357, 56832]), [128512], "فك الوجه")
# apl-source:55
تأكد_يساوي(من_بدائل([65, 55357, 56832, 1571]), [65, 128512, 1571], "خليط")
# apl-source:56
for ن in [0, 65, 1571, 65536, 128512, 917999]:
  # apl-source:57
  تأكد_يساوي(من_بدائل(إلى_بدائل(ن)), [ن], "ذهاب وعودة")
# apl-source:58
print("بدائلا 😀:", إلى_بدائل(128512))
# apl-source:59
