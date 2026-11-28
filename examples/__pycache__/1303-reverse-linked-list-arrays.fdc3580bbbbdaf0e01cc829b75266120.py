
# apl-source:1
# مثال 1303 — عكس قائمة مترابطة
# apl-source:2
# Reverse linked list with next array
# apl-source:3
# Demonstrates: مؤشرات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1303-reverse-linked-list-arrays.apl
# apl-source:6

# apl-source:7
# نعكس اتجاه كل وصلة
# apl-source:8
# ونتتبع السابق والحالي
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def اعكس_وصلات(تالي, رأس):
  # apl-source:19
  سابق = -1
  # apl-source:20
  حالي = رأس
  # apl-source:21
  جديد = list(تالي)
  # apl-source:22
  while حالي != -1:
    # apl-source:23
    ت = تالي[حالي]
    # apl-source:24
    جديد[حالي] = سابق
    # apl-source:25
    سابق = حالي
    # apl-source:26
    حالي = ت
  # apl-source:27
  return [جديد, سابق]
# apl-source:28

# apl-source:29
def امش(تالي, رأس):
  # apl-source:30
  ناتج = []
  # apl-source:31
  while رأس != -1:
    # apl-source:32
    ناتج = ناتج + [رأس]
    # apl-source:33
    رأس = تالي[رأس]
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
تالي = [1, 2, 3, -1]
# apl-source:37
نتيجة = اعكس_وصلات(تالي, 0)
# apl-source:38
تأكد_يساوي(امش(تالي, 0), [0, 1, 2, 3], "الأصل")
# apl-source:39
تأكد_يساوي(امش(نتيجة[0], نتيجة[1]), [3, 2, 1, 0], "المعكوس")
# apl-source:40
