
# apl-source:1
# مثال 894 — إقران كانتور
# apl-source:2
# Cantor pairing
# apl-source:3
# Demonstrates: تشفير زوج في عدد واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/894-cantor-pairing.apl
# apl-source:6

# apl-source:7
# دالة كانتور للإقران: تشفير زوج أعداد طبيعية في عدد واحد
# apl-source:8
# π(a,b) = (a+b)(a+b+1)/2 + b قابلة للعكس حسابياً
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
def أقرن(أ, ب):
  # apl-source:19
  مجموع = أ + ب
  # apl-source:20
  return مجموع * (مجموع + 1) // 2 + ب
# apl-source:21

# apl-source:22
def فك_إقران(ز):
  # apl-source:23
  # أكبر مثلثي لا يتجاوز ز بالبحث الثنائي
  # apl-source:24
  أدنى = 0
  # apl-source:25
  أعلى = 1
  # apl-source:26
  while أعلى * (أعلى + 1) // 2 <= ز:
    # apl-source:27
    أعلى = أعلى * 2
  # apl-source:28
  while أدنى + 1 < أعلى:
    # apl-source:29
    وسط = (أدنى + أعلى) // 2
    # apl-source:30
    if وسط * (وسط + 1) // 2 <= ز:
      # apl-source:31
      أدنى = وسط
    # apl-source:32
    else:
      # apl-source:33
      أعلى = وسط
  # apl-source:34
  مثلثي = أدنى * (أدنى + 1) // 2
  # apl-source:35
  ب = ز - مثلثي
  # apl-source:36
  أ = أدنى - ب
  # apl-source:37
  return [أ, ب]
# apl-source:38

# apl-source:39
print("π(3,5) =", أقرن(3, 5))
# apl-source:40
print("π(0,0) =", أقرن(0, 0))
# apl-source:41
print("π(4,1) =", أقرن(4, 1))
# apl-source:42

# apl-source:43
تأكد_يساوي(أقرن(3, 5), 41, "π(3,5) = 41")
# apl-source:44
تأكد_يساوي(أقرن(0, 0), 0, "π(0,0) = 0")
# apl-source:45
تأكد_يساوي(أقرن(4, 1), 16, "π(4,1) = 16")
# apl-source:46

# apl-source:47
# الفك يعيد الزوج
# apl-source:48
زوج = فك_إقران(41)
# apl-source:49
تأكد_يساوي(زوج[0], 3, "فك 41: الأول")
# apl-source:50
تأكد_يساوي(زوج[1], 5, "فك 41: الثاني")
# apl-source:51

# apl-source:52
# طي وفك لشبكة 10x10
# apl-source:53
for أ in range(10):
  # apl-source:54
  for ب in range(10):
    # apl-source:55
    مفكوك = فك_إقران(أقرن(أ, ب))
    # apl-source:56
    تأكد_يساوي(مفكوك[0], أ, "فك أ عند " + str(أ) + "," + str(ب))
    # apl-source:57
    تأكد_يساوي(مفكوك[1], ب, "فك ب عند " + str(أ) + "," + str(ب))
# apl-source:58
