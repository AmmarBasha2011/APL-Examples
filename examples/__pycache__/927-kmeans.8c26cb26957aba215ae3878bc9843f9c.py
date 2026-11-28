
# apl-source:1
# مثال 927 — تجميع ك-المتوسطات
# apl-source:2
# K-means clustering
# apl-source:3
# Demonstrates: تخصيص وتحديث مراكز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/927-kmeans.apl
# apl-source:6

# apl-source:7
# تجميع ك-المتوسطات: تقسيم النقاط لك مجموعة بتكرار التخصيص والتحديث
# apl-source:8
# يتقارب لأقرب مراكز محلية
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
def ك_متوسطات(نقاط, ك, تكرارات):
  # apl-source:19
  # مراكز أولية: أول ك نقطة (حتمي)
  # apl-source:20
  مراكز = []
  # apl-source:21
  for i in range(ك):
    # apl-source:22
    مراكز = مراكز + [[نقاط[i][0], نقاط[i][1]]]
  # apl-source:23
  for _ in range(تكرارات):
    # apl-source:24
    مجموعات = []
    # apl-source:25
    for __ in range(ك):
      # apl-source:26
      مجموعات = مجموعات + [[]]
    # apl-source:27
    for ن in نقاط:
      # apl-source:28
      أقرب = 0
      # apl-source:29
      أقل = (ن[0] - مراكز[0][0]) ** 2 + (ن[1] - مراكز[0][1]) ** 2
      # apl-source:30
      for ج in range(1, ك):
        # apl-source:31
        مسافة = (ن[0] - مراكز[ج][0]) ** 2 + (ن[1] - مراكز[ج][1]) ** 2
        # apl-source:32
        if مسافة < أقل:
          # apl-source:33
          أقل = مسافة
          # apl-source:34
          أقرب = ج
      # apl-source:35
      مجموعات[أقرب] = مجموعات[أقرب] + [ن]
    # apl-source:36
    for ج in range(ك):
      # apl-source:37
      if len(مجموعات[ج]) > 0:
        # apl-source:38
        مجموع_س = 0
        # apl-source:39
        مجموع_ص = 0
        # apl-source:40
        for ن in مجموعات[ج]:
          # apl-source:41
          مجموع_س = مجموع_س + ن[0]
          # apl-source:42
          مجموع_ص = مجموع_ص + ن[1]
        # apl-source:43
        مراكز[ج] = [مجموع_س / len(مجموعات[ج]), مجموع_ص / len(مجموعات[ج])]
  # apl-source:44
  return مراكز
# apl-source:45

# apl-source:46
نقاط = [[1, 1], [2, 1], [1, 2], [10, 10], [11, 10], [10, 11]]
# apl-source:47
مراكز = ك_متوسطات(نقاط, 2, 20)
# apl-source:48
print("المراكز:", مراكز)
# apl-source:49

# apl-source:50
# المجموعة الأولى حول (4/3, 4/3) والثانية حول (31/3, 31/3)
# apl-source:51
تأكد_يساوي(round(مراكز[0][0], 4), 1.3333, "مركز أول س")
# apl-source:52
تأكد_يساوي(round(مراكز[0][1], 4), 1.3333, "مركز أول ص")
# apl-source:53
تأكد_يساوي(round(مراكز[1][0], 4), 10.3333, "مركز ثانٍ س")
# apl-source:54
تأكد_يساوي(round(مراكز[1][1], 4), 10.3333, "مركز ثانٍ ص")
# apl-source:55

# apl-source:56
# كل نقطة أقرب لمركز مجموعتها
# apl-source:57
مسافة_قريب = (1 - مراكز[0][0]) ** 2 + (1 - مراكز[0][1]) ** 2
# apl-source:58
مسافة_بعيد = (1 - مراكز[1][0]) ** 2 + (1 - مراكز[1][1]) ** 2
# apl-source:59
if مسافة_قريب >= مسافة_بعيد:
  # apl-source:60
  print("فشل: التخصيص غير سليم")
  # apl-source:61
  قياسي_نظام_اخرج(1)
# apl-source:62
print("ناجح: التخصيص سليم")
# apl-source:63
