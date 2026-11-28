
# apl-source:1
# مثال 706 — توحيد برولوج
# apl-source:2
# Prolog unification
# apl-source:3
# Demonstrates: متغيرات، ربط، حدود مركبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/706-prolog-unify-lite.apl
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
# توحيد برولوج مصغر على الحدود
# apl-source:25
# Demonstrates: متغيرات, ربط, فحص occurrence مبسط
# apl-source:26
# الحد: ["ثابت", قيمة] أو ["متغير", اسم] أو ["مركب", رمز, وسائط]
# apl-source:27

# apl-source:28
def ثابت(ق):
  # apl-source:29
  return ["ثابت", ق]
# apl-source:30

# apl-source:31
def متغير(اسم):
  # apl-source:32
  return ["متغير", اسم]
# apl-source:33

# apl-source:34
def مركب(رمز, وسائط):
  # apl-source:35
  return ["مركب", رمز, وسائط]
# apl-source:36

# apl-source:37
def طبق(حد, ربط):
  # apl-source:38
  if حد[0] == "متغير":
    # apl-source:39
    بديل = ربط.get(حد[1], None)
    # apl-source:40
    if بديل != None:
      # apl-source:41
      return طبق(بديل, ربط)
  # apl-source:42
  return حد
# apl-source:43

# apl-source:44
def وحد(أ, ب, ربط):
  # apl-source:45
  أ2 = طبق(أ, ربط)
  # apl-source:46
  ب2 = طبق(ب, ربط)
  # apl-source:47
  if أ2[0] == "متغير":
    # apl-source:48
    ربط[أ2[1]] = ب2
    # apl-source:49
    return ربط
  # apl-source:50
  if ب2[0] == "متغير":
    # apl-source:51
    ربط[ب2[1]] = أ2
    # apl-source:52
    return ربط
  # apl-source:53
  if أ2[0] != ب2[0]:
    # apl-source:54
    return None
  # apl-source:55
  if أ2[0] == "ثابت":
    # apl-source:56
    if أ2[1] == ب2[1]:
      # apl-source:57
      return ربط
    # apl-source:58
    return None
  # apl-source:59
  if أ2[1] != ب2[1] or len(أ2[2]) != len(ب2[2]):
    # apl-source:60
    return None
  # apl-source:61
  for ي in range(len(أ2[2])):
    # apl-source:62
    ربط = وحد(أ2[2][ي], ب2[2][ي], ربط)
    # apl-source:63
    if ربط == None:
      # apl-source:64
      return None
  # apl-source:65
  return ربط
# apl-source:66

# apl-source:67
# f(X, b) مع f(a, Y)
# apl-source:68
ر = وحد(مركب("f", [متغير("X"), ثابت("b")]), مركب("f", [ثابت("a"), متغير("Y")]), {})
# apl-source:69
تأكد_يساوي(ر["X"], ["ثابت", "a"], "X تربط بأ")
# apl-source:70
تأكد_يساوي(ر["Y"], ["ثابت", "b"], "Y تربط بب")
# apl-source:71
# f(X, X) مع f(a, b) يفشل
# apl-source:72
ر2 = وحد(مركب("f", [متغير("X"), متغير("X")]), مركب("f", [ثابت("a"), ثابت("b")]), {})
# apl-source:73
تأكد_يساوي(ر2, None, "توحيد متناقض يفشل")
# apl-source:74
# g(X, X) مع g(a, a) ينجح
# apl-source:75
ر3 = وحد(مركب("g", [متغير("X"), متغير("X")]), مركب("g", [ثابت("a"), ثابت("a")]), {})
# apl-source:76
تأكد_يساوي(ر3["X"], ["ثابت", "a"], "توحيد متسق ينجح")
# apl-source:77
# رموز مختلفة تفشل
# apl-source:78
تأكد_يساوي(وحد(مركب("f", []), مركب("g", []), {}), None, "رموز مختلفة")
# apl-source:79
# متغير مع متغير
# apl-source:80
ر4 = وحد(متغير("X"), متغير("Y"), {})
# apl-source:81
تأكد_يساوي(ر4["X"], ["متغير", "Y"], "متغير يربط بمتغير")
# apl-source:82
print("ربط أول:", ر)
# apl-source:83
