
# apl-source:1
# مثال 826 — كوساراجو
# apl-source:2
# Kosaraju SCC
# apl-source:3
# Demonstrates: ترتيب إنهاء، مخطط مقلوب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/826-kosaraju.apl
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
# خوارزمية كوساراجو للمكونات القوية: تمريرا DFS أحدهما على المقلوب
# apl-source:25
# Demonstrates: ترتيب إنهاء, مخطط مقلوب, مكونات متصلة قوياً
# apl-source:26

# apl-source:27
جوار = [[1], [2, 3], [0], [4], [5], [3]]
# apl-source:28

# apl-source:29
def ترتيب_إنهاء():
  # apl-source:30
  مزار = []
  # apl-source:31
  for ي in range(6):
    # apl-source:32
    مزار.append(0)
  # apl-source:33
  ترتيب = []
  # apl-source:34
  def زر(عقدة):
    # apl-source:35
    مزار[عقدة] = 1
    # apl-source:36
    for جار in جوار[عقدة]:
      # apl-source:37
      if مزار[جار] == 0:
        # apl-source:38
        زر(جار)
    # apl-source:39
    ترتيب.append(عقدة)
  # apl-source:40
  for ي in range(6):
    # apl-source:41
    if مزار[ي] == 0:
      # apl-source:42
      زر(ي)
  # apl-source:43
  return ترتيب
# apl-source:44

# apl-source:45
def مكونات():
  # apl-source:46
  ترتيب = ترتيب_إنهاء()
  # apl-source:47
  مقلوب = [[], [], [], [], [], []]
  # apl-source:48
  for ي in range(6):
    # apl-source:49
    for جار in جوار[ي]:
      # apl-source:50
      مقلوب[جار].append(ي)
  # apl-source:51
  مزار = []
  # apl-source:52
  for ي in range(6):
    # apl-source:53
    مزار.append(0)
  # apl-source:54
  كل = []
  # apl-source:55
  def اجمع(عقدة, مكون):
    # apl-source:56
    مزار[عقدة] = 1
    # apl-source:57
    مكون.append(عقدة)
    # apl-source:58
    for جار in مقلوب[عقدة]:
      # apl-source:59
      if مزار[جار] == 0:
        # apl-source:60
        اجمع(جار, مكون)
  # apl-source:61
  ي = len(ترتيب) - 1
  # apl-source:62
  while ي >= 0:
    # apl-source:63
    عقدة = ترتيب[ي]
    # apl-source:64
    if مزار[عقدة] == 0:
      # apl-source:65
      مكون = []
      # apl-source:66
      اجمع(عقدة, مكون)
      # apl-source:67
      كل.append(مكون)
    # apl-source:68
    ي = ي - 1
  # apl-source:69
  return كل
# apl-source:70

# apl-source:71
تأكد_يساوي(ترتيب_إنهاء(), [2, 5, 4, 3, 1, 0], "ترتيب الإنهاء")
# apl-source:72
نتيجة = مكونات()
# apl-source:73
تأكد_يساوي(len(نتيجة), 2, "مكونان")
# apl-source:74
تأكد_يساوي(نتيجة[0], [0, 2, 1], "دورة أولى")
# apl-source:75
تأكد_يساوي(نتيجة[1], [3, 5, 4], "دورة ثانية")
# apl-source:76
