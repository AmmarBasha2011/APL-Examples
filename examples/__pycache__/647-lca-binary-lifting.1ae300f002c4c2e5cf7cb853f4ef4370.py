
# apl-source:1
# مثال 647 — أدنى سلف مشترك بالرفع الثنائي
# apl-source:2
# LCA binary lifting
# apl-source:3
# Demonstrates: سلف مشترك، رفع ثنائي، قفزات أسية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/647-lca-binary-lifting.apl
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
# أدنى سلف مشترك بالرفع الثنائي
# apl-source:25
# Demonstrates: جدول أسلاف بقوى اثنين, تسوية الأعماق, قفزات أسية
# apl-source:26
# LCA في O(log n) بعد تجهيز O(n log n)
# apl-source:27

# apl-source:28
أب = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
# apl-source:29
عمق = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# apl-source:30
ن = 12
# apl-source:31

# apl-source:32
جدول = []
# apl-source:33
جدول.append(أب)
# apl-source:34
for ك in range(1, 4):
  # apl-source:35
  صف = []
  # apl-source:36
  for ع in range(ن):
    # apl-source:37
    صف.append(جدول[ك - 1][جدول[ك - 1][ع]])
  # apl-source:38
  جدول.append(صف)
# apl-source:39

# apl-source:40
def سلف_برفع(ع, خطوات):
  # apl-source:41
  ك = 0
  # apl-source:42
  while خطوات > 0:
    # apl-source:43
    if خطوات % 2 == 1:
      # apl-source:44
      ع = جدول[ك][ع]
    # apl-source:45
    خطوات = خطوات // 2
    # apl-source:46
    ك = ك + 1
  # apl-source:47
  return ع
# apl-source:48

# apl-source:49
def أدنى_سلف(أ, ب):
  # apl-source:50
  if عمق[أ] < عمق[ب]:
    # apl-source:51
    ت = أ
    # apl-source:52
    أ = ب
    # apl-source:53
    ب = ت
  # apl-source:54
  أ = سلف_برفع(أ, عمق[أ] - عمق[ب])
  # apl-source:55
  if أ == ب:
    # apl-source:56
    return أ
  # apl-source:57
  for ك in range(4):
    # apl-source:58
    ج = 3 - ك
    # apl-source:59
    if جدول[ج][أ] != جدول[ج][ب]:
      # apl-source:60
      أ = جدول[ج][أ]
      # apl-source:61
      ب = جدول[ج][ب]
  # apl-source:62
  return أب[أ]
# apl-source:63

# apl-source:64
def أدنى_سلف_بسيط(أ, ب):
  # apl-source:65
  while عمق[أ] > عمق[ب]:
    # apl-source:66
    أ = أب[أ]
  # apl-source:67
  while عمق[ب] > عمق[أ]:
    # apl-source:68
    ب = أب[ب]
  # apl-source:69
  while أ != ب:
    # apl-source:70
    أ = أب[أ]
    # apl-source:71
    ب = أب[ب]
  # apl-source:72
  return أ
# apl-source:73

# apl-source:74
for أ in range(ن):
  # apl-source:75
  for ب in range(ن):
    # apl-source:76
    if أدنى_سلف(أ, ب) != أدنى_سلف_بسيط(أ, ب):
      # apl-source:77
      print("فشل: تطابق مع المرجع عند", أ, ب)
      # apl-source:78
      قياسي_نظام_اخرج(1)
# apl-source:79
print("ناجح: تطابق مع المرجع لكل الأزواج")
# apl-source:80
تأكد_يساوي(أدنى_سلف(7, 8), 3, "سلف 7 و 8")
# apl-source:81
تأكد_يساوي(أدنى_سلف(8, 10), 1, "سلف 8 و 10")
# apl-source:82
تأكد_يساوي(أدنى_سلف(11, 6), 2, "سلف 11 و 6")
# apl-source:83
