
# apl-source:1
# مثال 1683 — عكس قائمة مترابطة بمصفوفات
# apl-source:2
# Reverse linked list using next array
# apl-source:3
# Demonstrates: قوائم مترابطة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1683-linked-list-array-pairs-reverse.apl
# apl-source:6

# apl-source:7
# كل عقدة لها مؤشر لتاليها
# apl-source:8
# نعكس المؤشرات بالتتابع
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
def اعكس_روابط(تالي, رأس):
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
def اجمع_القيم(قيم, تالي, رأس):
  # apl-source:29
  خرج = []
  # apl-source:30
  ك = رأس
  # apl-source:31
  while ك != -1:
    # apl-source:32
    خرج.append(قيم[ك])
    # apl-source:33
    ك = تالي[ك]
  # apl-source:34
  return خرج
# apl-source:35

# apl-source:36
قيم = [10, 20, 30]
# apl-source:37
تالي = [1, 2, -1]
# apl-source:38
رأس_جديد = اعكس_روابط(تالي, 0)
# apl-source:39
تأكد_يساوي(اجمع_القيم(قيم, تالي, رأس_جديد), [30, 20, 10], "معكوسة")
# apl-source:40
