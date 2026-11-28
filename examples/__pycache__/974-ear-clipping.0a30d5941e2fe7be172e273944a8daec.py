
# apl-source:1
# مثال 974 — قص الأذن للتثليث
# apl-source:2
# Ear clipping triangulation
# apl-source:3
# Demonstrates: رأس محدب خالٍ من النقاط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/974-ear-clipping.apl
# apl-source:6

# apl-source:7
# تثليث المضلع بقص الأذن: نزع مثلثات محدبة تباعاً
# apl-source:8
# الأذن رأس محدب لا يقع داخل مثلثه أي رأس آخر
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
def متقاطع(أ, ب, ج):
  # apl-source:19
  return ((ب[0] - أ[0]) * (ج[1] - ب[1])) - ((ب[1] - أ[1]) * (ج[0] - ب[0]))
# apl-source:20

# apl-source:21
def داخل(ن, أ, ب, ج):
  # apl-source:22
  د1 = متقاطع(أ, ب, ن)
  # apl-source:23
  د2 = متقاطع(ب, ج, ن)
  # apl-source:24
  د3 = متقاطع(ج, أ, ن)
  # apl-source:25
  if (د1 < 0) or (د2 < 0) or (د3 < 0):
    # apl-source:26
    if (د1 > 0) or (د2 > 0) or (د3 > 0):
      # apl-source:27
      return 0
  # apl-source:28
  return 1
# apl-source:29

# apl-source:30
def قص_أذن(نقاط):
  # apl-source:31
  باقي = نقاط
  # apl-source:32
  عدد = 0
  # apl-source:33
  مساحة = 0
  # apl-source:34
  while len(باقي) > 3:
    # apl-source:35
    ن = len(باقي)
    # apl-source:36
    وجد = 0
    # apl-source:37
    i = 0
    # apl-source:38
    while (وجد == 0) and (i < ن):
      # apl-source:39
      سابق = باقي[((i + ن) - 1) % ن]
      # apl-source:40
      حالي = باقي[i]
      # apl-source:41
      تال = باقي[(i + 1) % ن]
      # apl-source:42
      تقاطع = متقاطع(سابق, حالي, تال)
      # apl-source:43
      if تقاطع > 0:
        # apl-source:44
        خال = 1
        # apl-source:45
        for j in range(ن):
          # apl-source:46
          if ((j != i) and (j != ((i + ن) - 1) % ن)) and (j != (i + 1) % ن):
            # apl-source:47
            if داخل(باقي[j], سابق, حالي, تال) == 1:
              # apl-source:48
              خال = 0
        # apl-source:49
        if خال == 1:
          # apl-source:50
          مساحة = مساحة + (تقاطع / 2)
          # apl-source:51
          عدد = عدد + 1
          # apl-source:52
          باقي = باقي[:i] + باقي[i + 1:]
          # apl-source:53
          وجد = 1
      # apl-source:54
      i = i + 1
    # apl-source:55
    if وجد == 0:
      # apl-source:56
      print("لا أذن صالحة")
      # apl-source:57
      قياسي_نظام_اخرج(1)
  # apl-source:58
  مساحة = مساحة + (متقاطع(باقي[0], باقي[1], باقي[2]) / 2)
  # apl-source:59
  عدد = عدد + 1
  # apl-source:60
  return [عدد, مساحة]
# apl-source:61

# apl-source:62
مربع = قص_أذن([[0, 0], [4, 0], [4, 4], [0, 4]])
# apl-source:63
خماسي = قص_أذن([[0, 0], [2, 0], [3, 2], [1, 3], [0, 2]])
# apl-source:64
تأكد_يساوي(مربع[0], 2, "مثلثات المربع")
# apl-source:65
تأكد_يساوي(مربع[1], 16, "مساحة المربع")
# apl-source:66
تأكد_يساوي(خماسي[0], 3, "مثلثات الخماسي")
# apl-source:67
تأكد_يساوي(round(خماسي[1], 6), 6.5, "مساحة الخماسي")
# apl-source:68
