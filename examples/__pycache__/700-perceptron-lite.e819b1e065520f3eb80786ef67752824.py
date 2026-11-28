
# apl-source:1
# مثال 700 — بيرسيبترون يتعلم AND
# apl-source:2
# Perceptron learns AND
# apl-source:3
# Demonstrates: قاعدة تحديث، عتبة، فصل خطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/700-perceptron-lite.apl
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
# بيرسيبترون أحادي الطبقة يتعلم بوابة AND
# apl-source:25
# Demonstrates: قاعدة تحديث بيرسيبترون, عتبة, تقارب مضمون للفصل الخطي
# apl-source:26
# XOR لا تنفع معه: ليست فصلا خطيا
# apl-source:27

# apl-source:28
def تنبؤ(أوزان, انحياز, س1, س2):
  # apl-source:29
  مجموع = أوزان[0] * س1 + أوزان[1] * س2 + انحياز
  # apl-source:30
  if مجموع > 0:
    # apl-source:31
    return 1
  # apl-source:32
  return 0
# apl-source:33

# apl-source:34
def درب(حقائب, أهداف, عصور):
  # apl-source:35
  أوزان = [0, 0]
  # apl-source:36
  انحياز = 0
  # apl-source:37
  for عصر in range(عصور):
    # apl-source:38
    أخطاء = 0
    # apl-source:39
    for ي in range(len(حقائب)):
      # apl-source:40
      س1 = حقائب[ي][0]
      # apl-source:41
      س2 = حقائب[ي][1]
      # apl-source:42
      تنب = تنبؤ(أوزان, انحياز, س1, س2)
      # apl-source:43
      خطا = أهداف[ي] - تنب
      # apl-source:44
      if خطا != 0:
        # apl-source:45
        أخطاء = أخطاء + 1
        # apl-source:46
        أوزان[0] = أوزان[0] + خطا * س1
        # apl-source:47
        أوزان[1] = أوزان[1] + خطا * س2
        # apl-source:48
        انحياز = انحياز + خطا
    # apl-source:49
    if أخطاء == 0:
      # apl-source:50
      return [أوزان, انحياز, عصر]
  # apl-source:51
  return [أوزان, انحياز, عصور]
# apl-source:52

# apl-source:53
حقائب = [[0, 0], [0, 1], [1, 0], [1, 1]]
# apl-source:54
أهداف = [0, 0, 0, 1]
# apl-source:55
نموذج = درب(حقائب, أهداف, 10)
# apl-source:56
تأكد_يساوي(نموذج[0], [2, 1], "الأوزان المتعلمة")
# apl-source:57
تأكد_يساوي(نموذج[1], -2, "الانحياز المتعلم")
# apl-source:58
تأكد_يساوي(نموذج[2], 5, "تقارب في العصر الخامس")
# apl-source:59
تأكد_يساوي(تنبؤ(نموذج[0], نموذج[1], 0, 0), 0, "AND(0,0)")
# apl-source:60
تأكد_يساوي(تنبؤ(نموذج[0], نموذج[1], 0, 1), 0, "AND(0,1)")
# apl-source:61
تأكد_يساوي(تنبؤ(نموذج[0], نموذج[1], 1, 0), 0, "AND(1,0)")
# apl-source:62
تأكد_يساوي(تنبؤ(نموذج[0], نموذج[1], 1, 1), 1, "AND(1,1)")
# apl-source:63
print("النموذج:", نموذج)
# apl-source:64
