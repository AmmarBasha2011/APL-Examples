
# apl-source:1
# مثال 915 — فحص ثنائية المخطط
# apl-source:2
# Bipartite check
# apl-source:3
# Demonstrates: تلوين ثنائي عرضي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/915-bipartite-check.apl
# apl-source:6

# apl-source:7
# فحص ثنائية المخطط: تلوين ثنائي بالبحث العرضي
# apl-source:8
# المخطط ثنائي إن أمكن تلوينه بلونين بلا جارين بلون واحد
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
def ثنائي(مخطط):
  # apl-source:19
  ن = len(مخطط)
  # apl-source:20
  لون = []
  # apl-source:21
  for _ in range(ن):
    # apl-source:22
    لون = لون + [-1]
  # apl-source:23
  for بداية in range(ن):
    # apl-source:24
    if لون[بداية] == -1:
      # apl-source:25
      لون[بداية] = 0
      # apl-source:26
      طابور = [بداية]
      # apl-source:27
      while len(طابور) > 0:
        # apl-source:28
        ع = طابور[0]
        # apl-source:29
        طابور = طابور[1:]
        # apl-source:30
        for جار in range(ن):
          # apl-source:31
          if مخطط[ع][جار] == 1:
            # apl-source:32
            if لون[جار] == -1:
              # apl-source:33
              لون[جار] = 1 - لون[ع]
              # apl-source:34
              طابور = طابور + [جار]
            # apl-source:35
            elif لون[جار] == لون[ع]:
              # apl-source:36
              return False
  # apl-source:37
  return 1 == 1
# apl-source:38

# apl-source:39
# دورة زوجية (مربع): ثنائية
# apl-source:40
مربع = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
# apl-source:41
# مثلث: ليست ثنائية
# apl-source:42
مثلث = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
# apl-source:43
# نجمة: ثنائية
# apl-source:44
نجمة = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# apl-source:45

# apl-source:46
print("مربع:", ثنائي(مربع))
# apl-source:47
print("مثلث:", ثنائي(مثلث))
# apl-source:48
print("نجمة:", ثنائي(نجمة))
# apl-source:49

# apl-source:50
تأكد_يساوي(ثنائي(مربع), 1 == 1, "الدورة الزوجية ثنائية")
# apl-source:51
تأكد_يساوي(ثنائي(مثلث), False, "المثلث ليس ثنائياً")
# apl-source:52
تأكد_يساوي(ثنائي(نجمة), 1 == 1, "النجمة ثنائية")
# apl-source:53

# apl-source:54
# خماسية الأضلاع: فردية، ليست ثنائية
# apl-source:55
خماسي = [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
# apl-source:56
تأكد_يساوي(ثنائي(خماسي), False, "الدورة الفردية ليست ثنائية")
# apl-source:57
