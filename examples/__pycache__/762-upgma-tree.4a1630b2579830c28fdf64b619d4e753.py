
# apl-source:1
# مثال 762 — تجميع UPGMA
# apl-source:2
# UPGMA clustering
# apl-source:3
# Demonstrates: أقرب زوج، متوسط مجموعات، ارتفاع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/762-upgma-tree.apl
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
# تجميع UPGMA: بناء شجرة تطور من مصفوفة مسافات
# apl-source:25
# Demonstrates: أقرب زوج, مسافة متوسط المجموعات, ارتفاعات الدمج
# apl-source:26
# الارتفاع = نصف المسافة، والدمج يعيد حساب المسافات بالمتوسط
# apl-source:27

# apl-source:28
مسافات = {
  # apl-source:29
  "A,B": 2.0, "A,C": 4.0, "A,D": 6.0,
  # apl-source:30
  "B,C": 4.0, "B,D": 6.0, "C,D": 5.0
# apl-source:31
}
# apl-source:32

# apl-source:33
def مسافة(أ, ب):
  # apl-source:34
  مفتاح = أ + "," + ب
  # apl-source:35
  if مفتاح in مسافات:
    # apl-source:36
    return مسافات[مفتاح]
  # apl-source:37
  return مسافات[ب + "," + أ]
# apl-source:38

# apl-source:39
def مسافة_مجموعتين(ع1, ع2):
  # apl-source:40
  مجموع = 0.0
  # apl-source:41
  عدد = 0
  # apl-source:42
  for أ in ع1:
    # apl-source:43
    for ب in ع2:
      # apl-source:44
      مجموع = مجموع + مسافة(أ, ب)
      # apl-source:45
      عدد = عدد + 1
  # apl-source:46
  return مجموع / عدد
# apl-source:47

# apl-source:48
def ابن_شجرة(أصناف):
  # apl-source:49
  مجموعات = []
  # apl-source:50
  for صنف in أصناف:
    # apl-source:51
    مجموعات.append([صنف])
  # apl-source:52
  دمج = []
  # apl-source:53
  while len(مجموعات) > 1:
    # apl-source:54
    أدنى = 1000000.0
    # apl-source:55
    أفضل_أ = 0
    # apl-source:56
    أفضل_ب = 1
    # apl-source:57
    for ي in range(len(مجموعات)):
      # apl-source:58
      for ج in range(ي + 1, len(مجموعات)):
        # apl-source:59
        د = مسافة_مجموعتين(مجموعات[ي], مجموعات[ج])
        # apl-source:60
        if د < أدنى:
          # apl-source:61
          أدنى = د
          # apl-source:62
          أفضل_أ = ي
          # apl-source:63
          أفضل_ب = ج
    # apl-source:64
    دمج.append([مجموعات[أفضل_أ] + مجموعات[أفضل_ب], round(أدنى / 2, 2)])
    # apl-source:65
    جديدة = مجموعات[أفضل_أ] + مجموعات[أفضل_ب]
    # apl-source:66
    باقية = []
    # apl-source:67
    for ي in range(len(مجموعات)):
      # apl-source:68
      if ي != أفضل_أ and ي != أفضل_ب:
        # apl-source:69
        باقية.append(مجموعات[ي])
    # apl-source:70
    باقية.append(جديدة)
    # apl-source:71
    مجموعات = باقية
  # apl-source:72
  return دمج
# apl-source:73

# apl-source:74
def نص_مجموعة(ع):
  # apl-source:75
  ناتج = ع[0]
  # apl-source:76
  for ي in range(1, len(ع)):
    # apl-source:77
    ناتج = ناتج + ع[ي]
  # apl-source:78
  return ناتج
# apl-source:79

# apl-source:80
دمج = ابن_شجرة(["A", "B", "C", "D"])
# apl-source:81

# apl-source:82
تأكد_يساوي(len(دمج), 3, "ثلاث خطوات دمج")
# apl-source:83
تأكد_يساوي(دمج[0][1], 1.0, "أول ارتفاع")
# apl-source:84
تأكد_يساوي(دمج[1][1], 2.0, "ثاني ارتفاع")
# apl-source:85
تأكد_يساوي(دمج[2][1], 2.83, "الجذر")
# apl-source:86
تأكد_يساوي(نص_مجموعة(دمج[0][0]), "AB", "A وB الأقرب")
# apl-source:87
تأكد_يساوي(نص_مجموعة(دمج[1][0]), "CAB", "انضمام C")
# apl-source:88
تأكد_يساوي(نص_مجموعة(دمج[2][0]), "DCAB", "انضمام D أخيراً")
# apl-source:89

# apl-source:90
print("الدمج الأول:", نص_مجموعة(دمج[0][0]), "عند", دمج[0][1])
# apl-source:91
