
# apl-source:1
# مثال 707 — حلال SAT بـDPLL
# apl-source:2
# DPLL SAT solver
# apl-source:3
# Demonstrates: نشر وحدة، فرع، رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/707-dpll-sat-lite.apl
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
# حلال SAT بخوارزمية DPLL المصغرة
# apl-source:25
# Demonstrates: نشر الوحدة, اختيار حرف, عودية مع رجوع
# apl-source:26
# الصيغة قائمة عبارات، كل عبارة قائمة حروف موجبة أو سالبة
# apl-source:27

# apl-source:28
def بسط(عبارات, حرف):
  # apl-source:29
  جديد = []
  # apl-source:30
  for عبارة in عبارات:
    # apl-source:31
    if حرف in عبارة:
      # apl-source:32
      جديد = جديد
    # apl-source:33
    else:
      # apl-source:34
      مصفاة = []
      # apl-source:35
      for ح in عبارة:
        # apl-source:36
        if ح != -حرف:
          # apl-source:37
          مصفاة.append(ح)
      # apl-source:38
      جديد.append(مصفاة)
  # apl-source:39
  return جديد
# apl-source:40

# apl-source:41
def وحدة(عبارات):
  # apl-source:42
  for عبارة in عبارات:
    # apl-source:43
    if len(عبارة) == 1:
      # apl-source:44
      return عبارة[0]
  # apl-source:45
  return 0
# apl-source:46

# apl-source:47
def dpll(عبارات, تعيين):
  # apl-source:48
  while True:
    # apl-source:49
    ح_وحدة = وحدة(عبارات)
    # apl-source:50
    if ح_وحدة == 0:
      # apl-source:51
      return فرع(عبارات, تعيين)
    # apl-source:52
    تعيين.append(ح_وحدة)
    # apl-source:53
    عبارات = بسط(عبارات, ح_وحدة)
    # apl-source:54
    if [] in عبارات:
      # apl-source:55
      return None
# apl-source:56

# apl-source:57
def فرع(عبارات, تعيين):
  # apl-source:58
  if len(عبارات) == 0:
    # apl-source:59
    return تعيين
  # apl-source:60
  if [] in عبارات:
    # apl-source:61
    return None
  # apl-source:62
  حرف = عبارات[0][0]
  # apl-source:63
  تعيين_ص = تعيين + [حرف]
  # apl-source:64
  نتيجة = dpll(بسط(عبارات, حرف), تعيين_ص)
  # apl-source:65
  if نتيجة != None:
    # apl-source:66
    return نتيجة
  # apl-source:67
  تعيين_خ = تعيين + [-حرف]
  # apl-source:68
  return dpll(بسط(عبارات, -حرف), تعيين_خ)
# apl-source:69

# apl-source:70
# (أ ∨ ب) ∧ (¬أ ∨ ب) ∧ (¬ب): غير قابلة للإشباع
# apl-source:71
تأكد_يساوي(dpll([[1, 2], [-1, 2], [-2]], []), None, "غير قابلة")
# apl-source:72
# (أ ∨ ب) ∧ (¬أ ∨ ج): قابلة
# apl-source:73
ن = dpll([[1, 2], [-1, 3]], [])
# apl-source:74
تأكد_يساوي(ن != None, True, "قابلة للإشباع")
# apl-source:75
# تحقق من صحة التعيين
# apl-source:76
def صحح(عبارات, تعيين):
  # apl-source:77
  for عبارة in عبارات:
    # apl-source:78
    صحيحة = False
    # apl-source:79
    for ح in عبارة:
      # apl-source:80
      if ح in تعيين:
        # apl-source:81
        صحيحة = True
    # apl-source:82
    if صحيحة == False:
      # apl-source:83
      return False
  # apl-source:84
  return True
# apl-source:85

# apl-source:86
تأكد_يساوي(صحح([[1, 2], [-1, 3]], ن), True, "التعيين يحقق الصيغة")
# apl-source:87
ن2 = dpll([[1], [-1, 2], [-2, 3]], [])
# apl-source:88
تأكد_يساوي(صحح([[1], [-1, 2], [-2, 3]], ن2), True, "سلسلة نشر وحدة")
# apl-source:89
تأكد_يساوي(1 in ن2, True, "أ حقيقية")
# apl-source:90
print("تعيين:", ن)
# apl-source:91
