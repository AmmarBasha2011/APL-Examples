
# apl-source:1
# مثال 1904 — عكس قائمة مرتبطة بالمصفوفات
# apl-source:2
# Reverse a linked list stored in arrays
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1904-linked-list-reverse-by-arrays.apl
# apl-source:6

# apl-source:7
# القيم في مصفوفة والتالي في مصفوفة أخرى
# apl-source:8
# نعكس مؤشر كل عقدة
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
def اعكس(تالي, رأس):
  # apl-source:19
  سابق = -1
  # apl-source:20
  حالي = رأس
  # apl-source:21
  while حالي != -1:
    # apl-source:22
    ت = تالي[حالي]
    # apl-source:23
    تالي[حالي] = سابق
    # apl-source:24
    سابق = حالي
    # apl-source:25
    حالي = ت
  # apl-source:26
  return سابق
# apl-source:27

# apl-source:28
def ترتيب(قيم, تالي, رأس):
  # apl-source:29
  خرج = []
  # apl-source:30
  حالي = رأس
  # apl-source:31
  while حالي != -1:
    # apl-source:32
    خرج = خرج + [قيم[حالي]]
    # apl-source:33
    حالي = تالي[حالي]
  # apl-source:34
  return خرج
# apl-source:35

# apl-source:36
قيم = [10, 20, 30, 40]
# apl-source:37
تالي = [1, 2, 3, -1]
# apl-source:38
تأكد_يساوي(ترتيب(قيم, تالي, 0), [10, 20, 30, 40], "الأصلي")
# apl-source:39
رأس = اعكس(تالي, 0)
# apl-source:40
تأكد_يساوي(رأس, 3, "الرأس الجديد")
# apl-source:41
تأكد_يساوي(ترتيب(قيم, تالي, رأس), [40, 30, 20, 10], "المعكوس")
# apl-source:42
