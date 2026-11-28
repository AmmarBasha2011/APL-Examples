
# apl-source:1
# مثال 916 — جسور المخطط
# apl-source:2
# Graph bridges
# apl-source:3
# Demonstrates: تارجان بأوقات الدخول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/916-bridges.apl
# apl-source:6

# apl-source:7
# جسور المخطط: أضلاع يؤدي حذفها لفصل المخطط
# apl-source:8
# خوارزمية تارجان بأوقات الدخول والقيم الدنيا
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
def جسور_المخطط(مخطط):
  # apl-source:19
  ن = len(مخطط)
  # apl-source:20
  دخول = []
  # apl-source:21
  دنيا = []
  # apl-source:22
  جسور = []
  # apl-source:23
  مؤقت = [0]
  # apl-source:24
  for _ in range(ن):
    # apl-source:25
    دخول.append(-1)
    # apl-source:26
    دنيا.append(0)
  # apl-source:27
  def تعمق(ع, أب):
    # apl-source:28
    دخول[ع] = مؤقت[0]
    # apl-source:29
    دنيا[ع] = مؤقت[0]
    # apl-source:30
    مؤقت[0] = مؤقت[0] + 1
    # apl-source:31
    for جار in range(ن):
      # apl-source:32
      if مخطط[ع][جار] == 1 and جار != أب:
        # apl-source:33
        if دخول[جار] != -1:
          # apl-source:34
          if دخول[جار] < دنيا[ع]:
            # apl-source:35
            دنيا[ع] = دخول[جار]
        # apl-source:36
        else:
          # apl-source:37
          تعمق(جار, ع)
          # apl-source:38
          if دنيا[جار] < دنيا[ع]:
            # apl-source:39
            دنيا[ع] = دنيا[جار]
          # apl-source:40
          if دنيا[جار] > دخول[ع]:
            # apl-source:41
            if ع < جار:
              # apl-source:42
              جسور.append([ع, جار])
            # apl-source:43
            else:
              # apl-source:44
              جسور.append([جار, ع])
  # apl-source:45
  for i in range(ن):
    # apl-source:46
    if دخول[i] == -1:
      # apl-source:47
      تعمق(i, -1)
  # apl-source:48
  return جسور
# apl-source:49

# apl-source:50
# مثلث {0,1,2} مع ذيل 1-3-4: الجسور (1,3) و(3,4)
# apl-source:51
مخطط = [[0, 1, 1, 0, 0], [1, 0, 1, 1, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 0]]
# apl-source:52
جسور = جسور_المخطط(مخطط)
# apl-source:53
print("الجسور:", جسور)
# apl-source:54

# apl-source:55
تأكد_يساوي(len(جسور), 2, "جسران")
# apl-source:56
# الترتيب غير مضمون: نتحقق من العضوية
# apl-source:57
وجد_أول = 0
# apl-source:58
وجد_ثان = 0
# apl-source:59
for ج in جسور:
  # apl-source:60
  if ج[0] == 1 and ج[1] == 3:
    # apl-source:61
    وجد_أول = 1
  # apl-source:62
  if ج[0] == 3 and ج[1] == 4:
    # apl-source:63
    وجد_ثان = 1
# apl-source:64
تأكد_يساوي(وجد_أول, 1, "الجسر (1,3) موجود")
# apl-source:65
تأكد_يساوي(وجد_ثان, 1, "الجسر (3,4) موجود")
# apl-source:66

# apl-source:67
# مثلث كامل بلا جسور
# apl-source:68
مثلث = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
# apl-source:69
تأكد_يساوي(len(جسور_المخطط(مثلث)), 0, "لا جسور في دورة")
# apl-source:70

# apl-source:71
# مسار خطي: كل ضلع جسر
# apl-source:72
مسار = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
# apl-source:73
تأكد_يساوي(len(جسور_المخطط(مسار)), 2, "المسار كله جسور")
# apl-source:74
