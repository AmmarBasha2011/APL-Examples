
# apl-source:1
# مثال 803 — الجيران الأقرب
# apl-source:2
# k-NN classifier
# apl-source:3
# Demonstrates: مسافة مربعة، تصويت أغلبية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/803-knn-classifier.apl
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
# مصنف الجيران الأقرب k-NN: تصويت الأغلبية بين أقرب النقاط
# apl-source:25
# Demonstrates: مسافة إقليدية مربعة, فرز بالاختيار, تصويت أغلبية
# apl-source:26

# apl-source:27
بيانات = [[[0, 0], "أ"], [[1, 1], "أ"], [[0, 2], "أ"], [[5, 5], "ب"], [[6, 5], "ب"], [[5, 6], "ب"]]
# apl-source:28

# apl-source:29
def صنّف(استعلام, ك):
  # apl-source:30
  مسافات = []
  # apl-source:31
  for عينة in بيانات:
    # apl-source:32
    فرق1 = استعلام[0] - عينة[0][0]
    # apl-source:33
    فرق2 = استعلام[1] - عينة[0][1]
    # apl-source:34
    مسافات.append([فرق1 * فرق1 + فرق2 * فرق2, عينة[1]])
  # apl-source:35
  for ي in range(len(مسافات)):
    # apl-source:36
    أدنى = ي
    # apl-source:37
    for ج in range(ي + 1, len(مسافات)):
      # apl-source:38
      if مسافات[ج][0] < مسافات[أدنى][0]:
        # apl-source:39
        أدنى = ج
    # apl-source:40
    مؤقت = مسافات[ي]
    # apl-source:41
    مسافات[ي] = مسافات[أدنى]
    # apl-source:42
    مسافات[أدنى] = مؤقت
  # apl-source:43
  أصوات = []
  # apl-source:44
  فئات = []
  # apl-source:45
  for ي in range(ك):
    # apl-source:46
    فئة = مسافات[ي][1]
    # apl-source:47
    if (فئة in فئات) == False:
      # apl-source:48
      فئات.append(فئة)
      # apl-source:49
      أصوات.append(0)
    # apl-source:50
    أصوات[فئات.index(فئة)] = أصوات[فئات.index(فئة)] + 1
  # apl-source:51
  أفضل = 0
  # apl-source:52
  for ي in range(1, len(أصوات)):
    # apl-source:53
    if أصوات[ي] > أصوات[أفضل]:
      # apl-source:54
      أفضل = ي
  # apl-source:55
  return فئات[أفضل]
# apl-source:56

# apl-source:57
تأكد_يساوي(صنّف([1, 0], 3), "أ", "نقطة قرب العنقود أ")
# apl-source:58
تأكد_يساوي(صنّف([6, 6], 3), "ب", "نقطة قرب العنقود ب")
# apl-source:59
تأكد_يساوي(صنّف([4, 5], 1), "ب", "جار واحد")
# apl-source:60
تأكد_يساوي(صنّف([0, 1], 5), "أ", "خمسة جيران")
# apl-source:61
