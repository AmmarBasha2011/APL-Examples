
# apl-source:1
# مثال 601 — شجرة AVL
# apl-source:2
# AVL tree
# apl-source:3
# Demonstrates: AVL، تدويرات، اتزان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/601-avl-tree.apl
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
# شجرة AVL: شجرة بحث ذاتية الاتزان بالتدويرات
# apl-source:25
# Demonstrates: تدوير يمين ويسار, عامل الاتزان, إدراج متزن
# apl-source:26
# إدراج 10 ثم 20 ثم 30 يسبب تدويرا يساريا
# apl-source:27

# apl-source:28
def ارتفاع(عقدة):
  # apl-source:29
  if عقدة == None:
    # apl-source:30
    return 0
  # apl-source:31
  return عقدة["ارتفاع"]
# apl-source:32

# apl-source:33
def حدّث_ارتفاع(عقدة):
  # apl-source:34
  عقدة["ارتفاع"] = 1 + max(ارتفاع(عقدة["يسار"]), ارتفاع(عقدة["يمين"]))
# apl-source:35

# apl-source:36
def دوّر_يسار(جذر):
  # apl-source:37
  جديد = جذر["يمين"]
  # apl-source:38
  جذر["يمين"] = جديد["يسار"]
  # apl-source:39
  جديد["يسار"] = جذر
  # apl-source:40
  حدّث_ارتفاع(جذر)
  # apl-source:41
  حدّث_ارتفاع(جديد)
  # apl-source:42
  return جديد
# apl-source:43

# apl-source:44
def دوّر_يمين(جذر):
  # apl-source:45
  جديد = جذر["يسار"]
  # apl-source:46
  جذر["يسار"] = جديد["يمين"]
  # apl-source:47
  جديد["يمين"] = جذر
  # apl-source:48
  حدّث_ارتفاع(جذر)
  # apl-source:49
  حدّث_ارتفاع(جديد)
  # apl-source:50
  return جديد
# apl-source:51

# apl-source:52
def أدرج(عقدة, قيمة):
  # apl-source:53
  if عقدة == None:
    # apl-source:54
    return {"قيمة": قيمة, "يسار": None, "يمين": None, "ارتفاع": 1}
  # apl-source:55
  if قيمة < عقدة["قيمة"]:
    # apl-source:56
    عقدة["يسار"] = أدرج(عقدة["يسار"], قيمة)
  # apl-source:57
  else:
    # apl-source:58
    عقدة["يمين"] = أدرج(عقدة["يمين"], قيمة)
  # apl-source:59
  حدّث_ارتفاع(عقدة)
  # apl-source:60
  اتزان = ارتفاع(عقدة["يسار"]) - ارتفاع(عقدة["يمين"])
  # apl-source:61
  if اتزان < -1:
    # apl-source:62
    if قيمة < عقدة["يمين"]["قيمة"]:
      # apl-source:63
      عقدة["يمين"] = دوّر_يمين(عقدة["يمين"])
    # apl-source:64
    return دوّر_يسار(عقدة)
  # apl-source:65
  if اتزان > 1:
    # apl-source:66
    if قيمة > عقدة["يسار"]["قيمة"]:
      # apl-source:67
      عقدة["يسار"] = دوّر_يسار(عقدة["يسار"])
    # apl-source:68
    return دوّر_يمين(عقدة)
  # apl-source:69
  return عقدة
# apl-source:70

# apl-source:71
جذر = None
# apl-source:72
for قيمة in [10, 20, 30, 40, 50, 25]:
  # apl-source:73
  جذر = أدرج(جذر, قيمة)
# apl-source:74
print("الجذر:", جذر["قيمة"], " والارتفاع:", جذر["ارتفاع"])
# apl-source:75
تأكد_يساوي(جذر["قيمة"], 30, "الجذر بعد التدويرات")
# apl-source:76
تأكد_يساوي(جذر["ارتفاع"], 3, "ارتفاع متزن لست قيم")
# apl-source:77
تأكد_يساوي(جذر["يسار"]["قيمة"], 20, "يسار الجذر")
# apl-source:78
