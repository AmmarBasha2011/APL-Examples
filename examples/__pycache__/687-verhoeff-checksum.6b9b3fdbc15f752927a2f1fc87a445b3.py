
# apl-source:1
# مثال 687 — رقم تحقق فيرهوف
# apl-source:2
# Verhoeff checksum
# apl-source:3
# Demonstrates: زمرة دايهدرال، تبديلات، كشف أخطاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/687-verhoeff-checksum.apl
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
# خوارزمية فيرهوف لرقم التحقق
# apl-source:25
# Demonstrates: زمرة دايهدرال D5, جدول تبديل, كشف تبديل الخانات المتجاورة
# apl-source:26
# أقوى من لون: يكشف أيضا تبديل أي خانتين متجاورتين
# apl-source:27

# apl-source:28
ض = [
  # apl-source:29
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  # apl-source:30
  [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
  # apl-source:31
  [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
  # apl-source:32
  [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
  # apl-source:33
  [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
  # apl-source:34
  [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
  # apl-source:35
  [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
  # apl-source:36
  [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
  # apl-source:37
  [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
  # apl-source:38
  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# apl-source:39
]
# apl-source:40
ت = [
  # apl-source:41
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  # apl-source:42
  [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
  # apl-source:43
  [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
  # apl-source:44
  [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
  # apl-source:45
  [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
  # apl-source:46
  [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
  # apl-source:47
  [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
  # apl-source:48
  [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
# apl-source:49
]
# apl-source:50
عكس = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]
# apl-source:51

# apl-source:52
def تحقق(رقم):
  # apl-source:53
  ج = 0
  # apl-source:54
  ن = len(رقم)
  # apl-source:55
  for ي in range(ن):
    # apl-source:56
    خانة = int(رقم[ن - 1 - ي])
    # apl-source:57
    ج = ض[ج][ت[ي % 8][خانة]]
  # apl-source:58
  return ج == 0
# apl-source:59

# apl-source:60
def رقم_تحقق(رقم):
  # apl-source:61
  ج = 0
  # apl-source:62
  ن = len(رقم)
  # apl-source:63
  for ي in range(ن):
    # apl-source:64
    خانة = int(رقم[ن - 1 - ي])
    # apl-source:65
    ج = ض[ج][ت[(ي + 1) % 8][خانة]]
  # apl-source:66
  return عكس[ج]
# apl-source:67

# apl-source:68
تأكد_يساوي(رقم_تحقق("236"), 3, "رقم تحقق 236 هو 3")
# apl-source:69
تأكد_يساوي(تحقق("2363"), True, "2363 صحيح")
# apl-source:70
تأكد_يساوي(تحقق("2364"), False, "2364 خاطئ")
# apl-source:71
تأكد_يساوي(تحقق("3263"), False, "تبديل أول خانتين يكشف")
# apl-source:72
تأكد_يساوي(تحقق("2633"), False, "تبديل خانتين متجاورتين يكشف")
# apl-source:73
ر = رقم_تحقق("12345")
# apl-source:74
تأكد_يساوي(تحقق("12345" + str(ر)), True, "الرقم المولد يتحقق")
# apl-source:75
print("رقم تحقق 12345:", ر)
# apl-source:76
