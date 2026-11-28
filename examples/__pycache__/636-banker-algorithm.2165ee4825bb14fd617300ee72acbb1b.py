
# apl-source:1
# مثال 636 — خوارزمية المصرفي
# apl-source:2
# Banker algorithm
# apl-source:3
# Demonstrates: جمود، حالة آمنة، موارد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/636-banker-algorithm.apl
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
# خوارزمية المصرفي: هل الحالة آمنة من الجمود؟
# apl-source:25
# Demonstrates: مصفوفات تخصيص واحتياج, بحث عن تسلسل آمن
# apl-source:26
# الحالة آمنة إذا وُجد ترتيب تكمل به كل العمليات
# apl-source:27

# apl-source:28
متاح = [3, 3, 2]
# apl-source:29
أقصى = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
# apl-source:30
مخصص = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
# apl-source:31

# apl-source:32
def آمنة(متاح, أقصى, مخصص):
  # apl-source:33
  ن = len(أقصى)
  # apl-source:34
  عمل = متاح.copy()
  # apl-source:35
  منتهية = [False] * ن
  # apl-source:36
  تسلسل = []
  # apl-source:37
  while len(تسلسل) < ن:
    # apl-source:38
    تقدم = False
    # apl-source:39
    for ي in range(ن):
      # apl-source:40
      if منتهية[ي] == False:
        # apl-source:41
        يكفي = True
        # apl-source:42
        for م in range(len(عمل)):
          # apl-source:43
          if أقصى[ي][م] - مخصص[ي][م] > عمل[م]:
            # apl-source:44
            يكفي = False
        # apl-source:45
        if يكفي:
          # apl-source:46
          for م in range(len(عمل)):
            # apl-source:47
            عمل[م] = عمل[م] + مخصص[ي][م]
          # apl-source:48
          منتهية[ي] = True
          # apl-source:49
          تسلسل.append(ي)
          # apl-source:50
          تقدم = True
    # apl-source:51
    if تقدم == False:
      # apl-source:52
      return []
  # apl-source:53
  return تسلسل
# apl-source:54

# apl-source:55
نتيجة = آمنة(متاح, أقصى, مخصص)
# apl-source:56
print("تسلسل آمن:", نتيجة)
# apl-source:57
تأكد_يساوي(len(نتيجة), 5, "المثال الكلاسيكي آمن")
# apl-source:58
تأكد_يساوي(نتيجة[0], 1, "العملية 1 أولا")
# apl-source:59
تأكد_يساوي(آمنة([1, 0, 0], أقصى, مخصص), [], "نقص الموارد غير آمن")
# apl-source:60
