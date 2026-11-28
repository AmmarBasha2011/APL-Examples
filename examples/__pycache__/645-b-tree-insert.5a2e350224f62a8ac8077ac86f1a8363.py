
# apl-source:1
# مثال 645 — إدخال في شجرة ب
# apl-source:2
# B-tree insert
# apl-source:3
# Demonstrates: شجرة ب، انقسام عقد، وسيط صاعد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/645-b-tree-insert.apl
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
# شجرة ب: إدخال مع انقسام العقد
# apl-source:25
# Demonstrates: عقد بحد أقصى 3 مفاتيح, انقسام العقدة الممتلئة, صعود الوسيط
# apl-source:26
# هكذا تبقي قواعد البيانات الشجرة متوازنة دائما
# apl-source:27

# apl-source:28
def عقدة(ورقة):
  # apl-source:29
  return {"م": [], "ف": [], "ورقة": ورقة}
# apl-source:30

# apl-source:31
def قسم(أب, ي):
  # apl-source:32
  طفل = أب["ف"][ي]
  # apl-source:33
  جديد = عقدة(طفل["ورقة"])
  # apl-source:34
  وسط = طفل["م"][1]
  # apl-source:35
  جديد["م"] = طفل["م"][2:]
  # apl-source:36
  طفل["م"] = طفل["م"][:1]
  # apl-source:37
  if not طفل["ورقة"]:
    # apl-source:38
    جديد["ف"] = طفل["ف"][2:]
    # apl-source:39
    طفل["ف"] = طفل["ف"][:2]
  # apl-source:40
  أب["م"].insert(ي, وسط)
  # apl-source:41
  أب["ف"].insert(ي + 1, جديد)
# apl-source:42

# apl-source:43
def أدخل_غير_ممتلئ(ع, مفتاح):
  # apl-source:44
  ي = len(ع["م"]) - 1
  # apl-source:45
  if ع["ورقة"]:
    # apl-source:46
    ع["م"].append(0)
    # apl-source:47
    while ي >= 0 and مفتاح < ع["م"][ي]:
      # apl-source:48
      ع["م"][ي + 1] = ع["م"][ي]
      # apl-source:49
      ي = ي - 1
    # apl-source:50
    ع["م"][ي + 1] = مفتاح
  # apl-source:51
  else:
    # apl-source:52
    while ي >= 0 and مفتاح < ع["م"][ي]:
      # apl-source:53
      ي = ي - 1
    # apl-source:54
    ي = ي + 1
    # apl-source:55
    if len(ع["ف"][ي]["م"]) == 3:
      # apl-source:56
      قسم(ع, ي)
      # apl-source:57
      if مفتاح > ع["م"][ي]:
        # apl-source:58
        ي = ي + 1
    # apl-source:59
    أدخل_غير_ممتلئ(ع["ف"][ي], مفتاح)
# apl-source:60

# apl-source:61
def أدخل(شجرة, مفتاح):
  # apl-source:62
  جذر = شجرة["جذر"]
  # apl-source:63
  if len(جذر["م"]) == 3:
    # apl-source:64
    جديد = عقدة(False)
    # apl-source:65
    جديد["ف"].append(جذر)
    # apl-source:66
    قسم(جديد, 0)
    # apl-source:67
    شجرة["جذر"] = جديد
    # apl-source:68
    أدخل_غير_ممتلئ(جديد, مفتاح)
  # apl-source:69
  else:
    # apl-source:70
    أدخل_غير_ممتلئ(جذر, مفتاح)
# apl-source:71

# apl-source:72
def تجول(ع, ناتج):
  # apl-source:73
  for ي in range(len(ع["م"])):
    # apl-source:74
    if not ع["ورقة"]:
      # apl-source:75
      تجول(ع["ف"][ي], ناتج)
    # apl-source:76
    ناتج.append(ع["م"][ي])
  # apl-source:77
  if not ع["ورقة"]:
    # apl-source:78
    تجول(ع["ف"][len(ع["م"])], ناتج)
# apl-source:79

# apl-source:80
شجرة = {"جذر": عقدة(True)}
# apl-source:81
for ق in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  # apl-source:82
  أدخل(شجرة, ق)
# apl-source:83
ناتج = []
# apl-source:84
تجول(شجرة["جذر"], ناتج)
# apl-source:85
تأكد_يساوي(ناتج, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "التجول مرتب")
# apl-source:86
تأكد_يساوي(len(ناتج), 10, "عدد المفاتيح")
# apl-source:87
تأكد_يساوي(شجرة["جذر"]["م"], [4], "الجذر بعد انقسامات متتالية")
# apl-source:88
print("جذر:", شجرة["جذر"]["م"])
# apl-source:89
