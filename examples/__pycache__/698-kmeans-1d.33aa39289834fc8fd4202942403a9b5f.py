
# apl-source:1
# مثال 698 — تجميع k-means أحادي
# apl-source:2
# 1D k-means
# apl-source:3
# Demonstrates: مراكز، إسناد، تقارب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/698-kmeans-1d.apl
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
# تجميع k-means على بيانات أحادية البعد
# apl-source:25
# Demonstrates: إسناد لأقرب مركز, إعادة حساب المتوسطات, تقارب
# apl-source:26
# البذرة: أول وآخر قيمة، فتكون النتيجة حتمية
# apl-source:27

# apl-source:28
def ك_متوسطات(بيانات, ك):
  # apl-source:29
  مراكز = [بيانات[0] * 1.0, بيانات[len(بيانات) - 1] * 1.0]
  # apl-source:30
  إسناد = []
  # apl-source:31
  for ي in range(len(بيانات)):
    # apl-source:32
    إسناد.append(0)
  # apl-source:33
  دورات = 0
  # apl-source:34
  for دورة in range(20):
    # apl-source:35
    تغير = False
    # apl-source:36
    for ي in range(len(بيانات)):
      # apl-source:37
      ق = بيانات[ي]
      # apl-source:38
      د0 = ق - مراكز[0]
      # apl-source:39
      if د0 < 0:
        # apl-source:40
        د0 = -د0
      # apl-source:41
      د1 = ق - مراكز[1]
      # apl-source:42
      if د1 < 0:
        # apl-source:43
        د1 = -د1
      # apl-source:44
      جديد = 0
      # apl-source:45
      if د1 < د0:
        # apl-source:46
        جديد = 1
      # apl-source:47
      if جديد != إسناد[ي]:
        # apl-source:48
        إسناد[ي] = جديد
        # apl-source:49
        تغير = True
    # apl-source:50
    جديدان = [0.0, 0.0]
    # apl-source:51
    أعداد = [0, 0]
    # apl-source:52
    for ي in range(len(بيانات)):
      # apl-source:53
      جديدان[إسناد[ي]] = جديدان[إسناد[ي]] + بيانات[ي]
      # apl-source:54
      أعداد[إسناد[ي]] = أعداد[إسناد[ي]] + 1
    # apl-source:55
    for ج in range(2):
      # apl-source:56
      if أعداد[ج] > 0:
        # apl-source:57
        جديدان[ج] = جديدان[ج] / أعداد[ج]
      # apl-source:58
      else:
        # apl-source:59
        جديدان[ج] = مراكز[ج]
    # apl-source:60
    مراكز = جديدان
    # apl-source:61
    دورات = دورات + 1
    # apl-source:62
    if تغير == False:
      # apl-source:63
      return [مراكز, إسناد, دورات]
  # apl-source:64
  return [مراكز, إسناد, دورات]
# apl-source:65

# apl-source:66
ناتج = ك_متوسطات([1, 2, 3, 10, 11, 12], 2)
# apl-source:67
تأكد_يساوي(ناتج[0], [2.0, 11.0], "مركزا العنقودين")
# apl-source:68
تأكد_يساوي(ناتج[1], [0, 0, 0, 1, 1, 1], "الإسنادات")
# apl-source:69
تأكد_يساوي(ناتج[2], 2, "تقارب بعد دورتين")
# apl-source:70
ناتج2 = ك_متوسطات([5, 1, 9, 2, 8, 1], 2)
# apl-source:71
تأكد_يساوي(ناتج2[1][0], ناتج2[1][2], "الكبار معا")
# apl-source:72
تأكد_يساوي(ناتج2[1][1], ناتج2[1][3], "الصغار معا")
# apl-source:73
print("المراكز:", ناتج[0])
# apl-source:74
