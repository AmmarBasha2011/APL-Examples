
# apl-source:1
# مثال 646 — شجرة تريب
# apl-source:2
# Treap
# apl-source:3
# Demonstrates: تريب، أولويات، دورات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/646-treap.apl
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
# تريب: شجرة بحث بأولويات كومة
# apl-source:25
# Demonstrates: أولوية ثابتة مشتقة من المفتاح, دورات يمين ويسار, خاصيتا BST وكومة
# apl-source:26
# شجرة متوازنة عشوائيا بلا مولد أرقام خارجي
# apl-source:27

# apl-source:28
def أولوية(مفتاح):
  # apl-source:29
  return ((مفتاح * 1103515245 + 12345) % 2147483648) % 1000
# apl-source:30

# apl-source:31
def عقدة_جديدة(مفتاح):
  # apl-source:32
  return {"مفتاح": مفتاح, "أولوية": أولوية(مفتاح), "يسار": None, "يمين": None}
# apl-source:33

# apl-source:34
def أدخل(ع, مفتاح):
  # apl-source:35
  if ع == None:
    # apl-source:36
    return عقدة_جديدة(مفتاح)
  # apl-source:37
  if مفتاح < ع["مفتاح"]:
    # apl-source:38
    ع["يسار"] = أدخل(ع["يسار"], مفتاح)
    # apl-source:39
    if ع["يسار"]["أولوية"] > ع["أولوية"]:
      # apl-source:40
      جديد = ع["يسار"]
      # apl-source:41
      ع["يسار"] = جديد["يمين"]
      # apl-source:42
      جديد["يمين"] = ع
      # apl-source:43
      return جديد
  # apl-source:44
  else:
    # apl-source:45
    ع["يمين"] = أدخل(ع["يمين"], مفتاح)
    # apl-source:46
    if ع["يمين"]["أولوية"] > ع["أولوية"]:
      # apl-source:47
      جديد = ع["يمين"]
      # apl-source:48
      ع["يمين"] = جديد["يسار"]
      # apl-source:49
      جديد["يسار"] = ع
      # apl-source:50
      return جديد
  # apl-source:51
  return ع
# apl-source:52

# apl-source:53
def تجول(ع, ناتج):
  # apl-source:54
  if ع == None:
    # apl-source:55
    return
  # apl-source:56
  تجول(ع["يسار"], ناتج)
  # apl-source:57
  ناتج.append(ع["مفتاح"])
  # apl-source:58
  تجول(ع["يمين"], ناتج)
# apl-source:59

# apl-source:60
def تحقق_كومة(ع):
  # apl-source:61
  if ع == None:
    # apl-source:62
    return True
  # apl-source:63
  if ع["يسار"] != None and ع["يسار"]["أولوية"] > ع["أولوية"]:
    # apl-source:64
    return False
  # apl-source:65
  if ع["يمين"] != None and ع["يمين"]["أولوية"] > ع["أولوية"]:
    # apl-source:66
    return False
  # apl-source:67
  return تحقق_كومة(ع["يسار"]) and تحقق_كومة(ع["يمين"])
# apl-source:68

# apl-source:69
جذر = None
# apl-source:70
for م in [5, 3, 8, 1, 4, 7, 9, 2, 6]:
  # apl-source:71
  جذر = أدخل(جذر, م)
# apl-source:72
ناتج = []
# apl-source:73
تجول(جذر, ناتج)
# apl-source:74
تأكد_يساوي(ناتج, [1, 2, 3, 4, 5, 6, 7, 8, 9], "ترتيب BST")
# apl-source:75
تأكد_يساوي(تحقق_كومة(جذر), True, "خاصية الكومة")
# apl-source:76
تأكد_يساوي(جذر["مفتاح"], 9, "أعلى أولوية في الجذر")
# apl-source:77
print("أولوية الجذر:", جذر["أولوية"])
# apl-source:78
