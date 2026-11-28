
# apl-source:1
# مثال 620 — قائمة القفز
# apl-source:2
# Skip list
# apl-source:3
# Demonstrates: قائمة قفز، مستويات، بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/620-skip-list.apl
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
# قائمة القفز: بحث سريع في قائمة مرتبة بمستويات
# apl-source:25
# Demonstrates: مستويات احتمالية مثبتة البذرة, روابط أمامية, بحث بالقفز
# apl-source:26
# بديل عملي عن الأشجار المتزنة
# apl-source:27

# apl-source:28
def عشوائي_مثبت(بذرة):
  # apl-source:29
  return (بذرة * 1103515245 + 12345) % 2147483648
# apl-source:30

# apl-source:31
def مستوى_عقدة(قيمة):
  # apl-source:32
  بذرة = عشوائي_مثبت(قيمة * 7919)
  # apl-source:33
  مستوى = 1
  # apl-source:34
  while بذرة % 2 == 0 and مستوى < 4:
    # apl-source:35
    مستوى = مستوى + 1
    # apl-source:36
    بذرة = بذرة // 2
  # apl-source:37
  return مستوى
# apl-source:38

# apl-source:39
def أنشئ_قائمة():
  # apl-source:40
  return {"رأس": {"قيمة": -1, "أمام": [None, None, None, None]}}
# apl-source:41

# apl-source:42
def ابحث(قائمة, قيمة):
  # apl-source:43
  عقدة = قائمة["رأس"]
  # apl-source:44
  for مستوى in range(3, -1, -1):
    # apl-source:45
    while عقدة["أمام"][مستوى] != None and عقدة["أمام"][مستوى]["قيمة"] < قيمة:
      # apl-source:46
      عقدة = عقدة["أمام"][مستوى]
  # apl-source:47
  عقدة = عقدة["أمام"][0]
  # apl-source:48
  if عقدة != None and عقدة["قيمة"] == قيمة:
    # apl-source:49
    return True
  # apl-source:50
  return False
# apl-source:51

# apl-source:52
def أدرج(قائمة, قيمة):
  # apl-source:53
  تحديث = [قائمة["رأس"], قائمة["رأس"], قائمة["رأس"], قائمة["رأس"]]
  # apl-source:54
  عقدة = قائمة["رأس"]
  # apl-source:55
  for مستوى in range(3, -1, -1):
    # apl-source:56
    while عقدة["أمام"][مستوى] != None and عقدة["أمام"][مستوى]["قيمة"] < قيمة:
      # apl-source:57
      عقدة = عقدة["أمام"][مستوى]
    # apl-source:58
    تحديث[مستوى] = عقدة
  # apl-source:59
  مستويات = مستوى_عقدة(قيمة)
  # apl-source:60
  أمام = [None, None, None, None]
  # apl-source:61
  for مستوى in range(مستويات):
    # apl-source:62
    أمام[مستوى] = تحديث[مستوى]["أمام"][مستوى]
    # apl-source:63
    تحديث[مستوى]["أمام"][مستوى] = {"قيمة": قيمة, "أمام": أمام}
# apl-source:64

# apl-source:65
قائمة = أنشئ_قائمة()
# apl-source:66
for قيمة in [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]:
  # apl-source:67
  أدرج(قائمة, قيمة)
# apl-source:68
تأكد_يساوي(ابحث(قائمة, 19), True, "موجود")
# apl-source:69
تأكد_يساوي(ابحث(قائمة, 20), False, "غير موجود")
# apl-source:70
تأكد_يساوي(ابحث(قائمة, 3), True, "الأول")
# apl-source:71
تأكد_يساوي(ابحث(قائمة, 25), True, "الأخير")
# apl-source:72
مستويات = []
# apl-source:73
for ق in [3, 6, 7]:
  # apl-source:74
  مستويات.append(مستوى_عقدة(ق))
# apl-source:75
print("مستويات العقد:", مستويات)
# apl-source:76
