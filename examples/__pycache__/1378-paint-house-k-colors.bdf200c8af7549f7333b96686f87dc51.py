
# apl-source:1
# مثال 1378 — طلاء بيوت بألوان كثيرة
# apl-source:2
# Paint house II minimum cost
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1378-paint-house-k-colors.apl
# apl-source:6

# apl-source:7
# نحتفظ بأصغر تكلفتين من الصف السابق
# apl-source:8
# اللون المماثل لأصغرهما يأخذ ثانيهما
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
def اقل_تكلفة_طلاء(تكاليف):
  # apl-source:19
  ك = len(تكاليف[0])
  # apl-source:20
  سابق = [0] * ك
  # apl-source:21
  for صف in تكاليف:
    # apl-source:22
    ادنى1 = 1000000000
    # apl-source:23
    ادنى2 = 1000000000
    # apl-source:24
    موضع = -1
    # apl-source:25
    for ج in range(ك):
      # apl-source:26
      if سابق[ج] < ادنى1:
        # apl-source:27
        ادنى2 = ادنى1
        # apl-source:28
        ادنى1 = سابق[ج]
        # apl-source:29
        موضع = ج
      # apl-source:30
      elif سابق[ج] < ادنى2:
        # apl-source:31
        ادنى2 = سابق[ج]
    # apl-source:32
    جديد = [0] * ك
    # apl-source:33
    for ج in range(ك):
      # apl-source:34
      if ج == موضع:
        # apl-source:35
        جديد[ج] = صف[ج] + ادنى2
      # apl-source:36
      else:
        # apl-source:37
        جديد[ج] = صف[ج] + ادنى1
    # apl-source:38
    سابق = جديد
  # apl-source:39
  افضل = سابق[0]
  # apl-source:40
  for ق in سابق:
    # apl-source:41
    if ق < افضل:
      # apl-source:42
      افضل = ق
  # apl-source:43
  return افضل
# apl-source:44

# apl-source:45
تأكد_يساوي(اقل_تكلفة_طلاء([[1,5,3],[2,9,4]]), 5, "بيتان")
# apl-source:46
تأكد_يساوي(اقل_تكلفة_طلاء([[1,3],[2,4]]), 5, "لونان")
# apl-source:47
تأكد_يساوي(اقل_تكلفة_طلاء([[3,1,2]]), 1, "بيت واحد")
# apl-source:48
