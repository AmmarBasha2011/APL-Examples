
# apl-source:1
# مثال 865 — أعداد بيل للتقسيمات
# apl-source:2
# Bell numbers
# apl-source:3
# Demonstrates: مثلث بيل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/865-bell-numbers.apl
# apl-source:6

# apl-source:7
# أعداد بيل: عدد كل تقسيمات مجموعة من n عنصراً
# apl-source:8
# B(n) = مجموع S(n,k) لكل k، وتحسب أيضاً بمثلث بيل
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
# مثلث بيل: كل صف يبدأ بآخر عنصر من السابق
# apl-source:19
def بيل(ن):
  # apl-source:20
  مثلث = [[1]]
  # apl-source:21
  for صف in range(1, ن + 1):
    # apl-source:22
    سابق = مثلث[len(مثلث) - 1]
    # apl-source:23
    جديد = [سابق[len(سابق) - 1]]
    # apl-source:24
    for عنصر in سابق:
      # apl-source:25
      جديد = جديد + [جديد[len(جديد) - 1] + عنصر]
    # apl-source:26
    مثلث = مثلث + [جديد]
  # apl-source:27
  return مثلث[ن][0]
# apl-source:28

# apl-source:29
print("B0..B8:", [بيل(0), بيل(1), بيل(2), بيل(3), بيل(4), بيل(5), بيل(6), بيل(7), بيل(8)])
# apl-source:30

# apl-source:31
تأكد_يساوي(بيل(0), 1, "B0 = 1")
# apl-source:32
تأكد_يساوي(بيل(3), 5, "B3 = 5")
# apl-source:33
تأكد_يساوي(بيل(5), 52, "B5 = 52")
# apl-source:34
تأكد_يساوي(بيل(7), 877, "B7 = 877")
# apl-source:35
تأكد_يساوي(بيل(8), 4140, "B8 = 4140")
# apl-source:36
