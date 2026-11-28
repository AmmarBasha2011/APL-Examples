
# apl-source:1
# مثال 709 — بيج رانك مصغر
# apl-source:2
# PageRank lite
# apl-source:3
# Demonstrates: تخميد، تكرار، تطبيع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/709-pagerank-lite.apl
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
# بيج رانك مصغر على رسم ويب صغير
# apl-source:25
# Demonstrates: تخميد 0.85, تكرار حتى التقارب, تطبيع المجموع 1
# apl-source:26
# أربع صفحات: 0 -> 1,2 ; 1 -> 2 ; 2 -> 0 ; 3 -> 2
# apl-source:27

# apl-source:28
def رتب(روابط, ن, تخميد, دورات):
  # apl-source:29
  رتبة = []
  # apl-source:30
  for ي in range(ن):
    # apl-source:31
    رتبة.append(1.0 / ن)
  # apl-source:32
  خارجة = []
  # apl-source:33
  for ي in range(ن):
    # apl-source:34
    خارجة.append(len(روابط[ي]))
  # apl-source:35
  for دورة in range(دورات):
    # apl-source:36
    جديد = []
    # apl-source:37
    for ي in range(ن):
      # apl-source:38
      جديد.append((1.0 - تخميد) / ن)
    # apl-source:39
    for مصدر in range(ن):
      # apl-source:40
      if خارجة[مصدر] > 0:
        # apl-source:41
        حصة = تخميد * رتبة[مصدر] / خارجة[مصدر]
        # apl-source:42
        for هدف in روابط[مصدر]:
          # apl-source:43
          جديد[هدف] = جديد[هدف] + حصة
      # apl-source:44
      else:
        # apl-source:45
        حصة = تخميد * رتبة[مصدر] / ن
        # apl-source:46
        for ي in range(ن):
          # apl-source:47
          جديد[ي] = جديد[ي] + حصة
    # apl-source:48
    رتبة = جديد
  # apl-source:49
  return رتبة
# apl-source:50

# apl-source:51
روابط = [[1, 2], [2], [0], [2]]
# apl-source:52
رتبة = رتب(روابط, 4, 0.85, 40)
# apl-source:53
مجموع = رتبة[0] + رتبة[1] + رتبة[2] + رتبة[3]
# apl-source:54
تأكد_يساوي(round(مجموع, 6), 1.0, "المجموع واحد")
# apl-source:55
تأكد_يساوي(رتبة[2] > رتبة[0], True, "الصفحة 2 الأقوى")
# apl-source:56
تأكد_يساوي(رتبة[0] > رتبة[1], True, "صفر أقوى من واحد")
# apl-source:57
تأكد_يساوي(رتبة[1] > رتبة[3], True, "واحد أقوى من ثلاثة")
# apl-source:58
تأكد_يساوي(round(رتبة[2], 3), 0.394, "رتبة الصفحة 2")
# apl-source:59
print("الرتب:", رتبة)
# apl-source:60
