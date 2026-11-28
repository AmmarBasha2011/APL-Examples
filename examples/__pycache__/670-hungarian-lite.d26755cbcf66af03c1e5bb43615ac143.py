
# apl-source:1
# مثال 670 — المجرية المصغرة للإسناد
# apl-source:2
# Hungarian-lite assignment
# apl-source:3
# Demonstrates: إسناد، مصفوفة كلفة، جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/670-hungarian-lite.apl
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
# الخوارزمية المجرية: تعيين بأقل كلفة
# apl-source:25
# Demonstrates: إمكانات الصفوف والأعمدة, شجرة متناوبة, مسار زيادة
# apl-source:26
# يوزع العمال على المهام بأقل كلفة كلية في O(n^3)
# apl-source:27

# apl-source:28
ن = 3
# apl-source:29
لانهائي = 1000000
# apl-source:30
كلفة = [[4, 1, 3], [2, 0, 5], [3, 2, 2]]
# apl-source:31

# apl-source:32
def وسع_عمود(أ, ف, ق, ع, مسار, ص):
  # apl-source:33
  ع[0] = ص
  # apl-source:34
  أدنى = [لانهائي, لانهائي, لانهائي, لانهائي]
  # apl-source:35
  مستخدم = [False, False, False, False]
  # apl-source:36
  ج0 = 0
  # apl-source:37
  while True:
    # apl-source:38
    مستخدم[ج0] = True
    # apl-source:39
    ص0 = ع[ج0]
    # apl-source:40
    دلتا = لانهائي
    # apl-source:41
    ج1 = 0
    # apl-source:42
    for ج in range(1, ن + 1):
      # apl-source:43
      if مستخدم[ج] == False:
        # apl-source:44
        حالية = أ[ص0 - 1][ج - 1] - ف[ص0] - ق[ج]
        # apl-source:45
        if حالية < أدنى[ج]:
          # apl-source:46
          أدنى[ج] = حالية
          # apl-source:47
          مسار[ج] = ج0
        # apl-source:48
        if أدنى[ج] < دلتا:
          # apl-source:49
          دلتا = أدنى[ج]
          # apl-source:50
          ج1 = ج
    # apl-source:51
    for ج in range(0, ن + 1):
      # apl-source:52
      if مستخدم[ج]:
        # apl-source:53
        ف[ع[ج]] = ف[ع[ج]] + دلتا
        # apl-source:54
        ق[ج] = ق[ج] - دلتا
      # apl-source:55
      else:
        # apl-source:56
        أدنى[ج] = أدنى[ج] - دلتا
    # apl-source:57
    ج0 = ج1
    # apl-source:58
    if ع[ج0] == 0:
      # apl-source:59
      return ج0
# apl-source:60

# apl-source:61
def مجري(أ):
  # apl-source:62
  ف = [0, 0, 0, 0]
  # apl-source:63
  ق = [0, 0, 0, 0]
  # apl-source:64
  ع = [0, 0, 0, 0]
  # apl-source:65
  مسار = [0, 0, 0, 0]
  # apl-source:66
  for ص in range(1, ن + 1):
    # apl-source:67
    ج0 = وسع_عمود(أ, ف, ق, ع, مسار, ص)
    # apl-source:68
    while ج0 != 0:
      # apl-source:69
      ج1 = مسار[ج0]
      # apl-source:70
      ع[ج0] = ع[ج1]
      # apl-source:71
      ج0 = ج1
  # apl-source:72
  return [0 - ق[0], ع]
# apl-source:73

# apl-source:74
نتيجة = مجري(كلفة)
# apl-source:75
تأكد_يساوي(نتيجة[0], 5, "أقل كلفة كلية")
# apl-source:76
تعيين = نتيجة[1]
# apl-source:77
تأكد_يساوي(كلفة[تعيين[1] - 1][0] + كلفة[تعيين[2] - 1][1] + كلفة[تعيين[3] - 1][2], 5, "التعيين يحقق الكلفة")
# apl-source:78
print("كلفة:", نتيجة[0])
# apl-source:79
print("تعيين الأعمدة إلى الصفوف:", تعيين)
# apl-source:80
