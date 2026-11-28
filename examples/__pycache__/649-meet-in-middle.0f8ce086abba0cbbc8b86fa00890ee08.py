
# apl-source:1
# مثال 649 — اللقاء في المنتصف
# apl-source:2
# Meet in the middle
# apl-source:3
# Demonstrates: تقسيم نصفين، تعداد أسس، قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/649-meet-in-middle.apl
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
# اللقاء في المنتصف: عد مجموعات جزئية بهدف
# apl-source:25
# Demonstrates: تقسيم النصفين, تعداد الأسس, عد بالقواميس
# apl-source:26
# 2^12 بدل 2^24 عندما ينقسم العمل نصفين
# apl-source:27

# apl-source:28
أوزان = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
# apl-source:29
هدف = 15
# apl-source:30

# apl-source:31
def مجموع_مجموعات(عناصر):
  # apl-source:32
  نتائج = {}
  # apl-source:33
  for قناع in range(2 ** len(عناصر)):
    # apl-source:34
    حاصل = 0
    # apl-source:35
    for ي in range(len(عناصر)):
      # apl-source:36
      if قناع & (1 << ي):
        # apl-source:37
        حاصل = حاصل + عناصر[ي]
    # apl-source:38
    if حاصل in نتائج:
      # apl-source:39
      نتائج[حاصل] = نتائج[حاصل] + 1
    # apl-source:40
    else:
      # apl-source:41
      نتائج[حاصل] = 1
  # apl-source:42
  return نتائج
# apl-source:43

# apl-source:44
يسار = مجموع_مجموعات(أوزان[:6])
# apl-source:45
يمين = مجموع_مجموعات(أوزان[6:])
# apl-source:46
عدد = 0
# apl-source:47
for ح in يسار.keys():
  # apl-source:48
  باقي = هدف - ح
  # apl-source:49
  if باقي in يمين:
    # apl-source:50
    عدد = عدد + يسار[ح] * يمين[باقي]
# apl-source:51

# apl-source:52
مرجع = 0
# apl-source:53
for قناع in range(4096):
  # apl-source:54
  حاصل = 0
  # apl-source:55
  for ي in range(12):
    # apl-source:56
    if قناع & (1 << ي):
      # apl-source:57
      حاصل = حاصل + أوزان[ي]
  # apl-source:58
  if حاصل == هدف:
    # apl-source:59
    مرجع = مرجع + 1
# apl-source:60

# apl-source:61
تأكد_يساوي(عدد, مرجع, "يطابق التعداد الشامل")
# apl-source:62
تأكد_يساوي(عدد, 91, "العدد الدقيق")
# apl-source:63
print("عدد المجموعات:", عدد)
# apl-source:64
