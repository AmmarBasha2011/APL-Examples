
# apl-source:1
# مثال 665 — بحث عرضي ثنائي
# apl-source:2
# Bidirectional BFS
# apl-source:3
# Demonstrates: بحث ثنائي، جبهتان، أقصر طريق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/665-bidirectional-bfs.apl
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
# بحث عرضي ثنائي الاتجاه
# apl-source:25
# Demonstrates: جبهتان متعاكستان, لقاء في المنتصف, طول أقصر طريق
# apl-source:26
# نصفان من البحث أسرع من بحث كامل
# apl-source:27

# apl-source:28
رسم = {"أ": ["ب", "ج"], "ب": ["أ", "د", "ه"], "ج": ["أ", "و"], "د": ["ب"], "ه": ["ب", "ز"], "و": ["ج", "ح"], "ز": ["ه"], "ح": ["و", "ط"], "ط": ["ح"]}
# apl-source:29

# apl-source:30
def أقصر_ثنائي(بداية, نهاية):
  # apl-source:31
  if بداية == نهاية:
    # apl-source:32
    return 0
  # apl-source:33
  أمام = {بداية: 0}
  # apl-source:34
  خلف = {نهاية: 0}
  # apl-source:35
  while True:
    # apl-source:36
    أصغر = -1
    # apl-source:37
    for عقدة in أمام:
      # apl-source:38
      if عقدة in خلف:
        # apl-source:39
        م = أمام[عقدة] + خلف[عقدة]
        # apl-source:40
        if أصغر == -1 or م < أصغر:
          # apl-source:41
          أصغر = م
    # apl-source:42
    if أصغر != -1:
      # apl-source:43
      return أصغر
    # apl-source:44
    جديدة = {}
    # apl-source:45
    for عقدة in أمام:
      # apl-source:46
      if أمام[عقدة] == أعمق(أمام):
        # apl-source:47
        for جار in رسم[عقدة]:
          # apl-source:48
          if (جار in أمام) == False:
            # apl-source:49
            جديدة[جار] = أمام[عقدة] + 1
    # apl-source:50
    for مفتاح in جديدة:
      # apl-source:51
      أمام[مفتاح] = جديدة[مفتاح]
    # apl-source:52
    if len(أمام) >= 100:
      # apl-source:53
      return -1
    # apl-source:54
    ت = أمام
    # apl-source:55
    أمام = خلف
    # apl-source:56
    خلف = ت
  # apl-source:57
  return -1
# apl-source:58

# apl-source:59
def أعمق(قاموس):
  # apl-source:60
  أقصى = 0
  # apl-source:61
  for مفتاح in قاموس:
    # apl-source:62
    if قاموس[مفتاح] > أقصى:
      # apl-source:63
      أقصى = قاموس[مفتاح]
  # apl-source:64
  return أقصى
# apl-source:65

# apl-source:66
تأكد_يساوي(أقصر_ثنائي("أ", "ط"), 4, "من أ إلى ط")
# apl-source:67
تأكد_يساوي(أقصر_ثنائي("د", "ز"), 3, "من د إلى ز")
# apl-source:68
تأكد_يساوي(أقصر_ثنائي("أ", "أ"), 0, "نفس العقدة")
# apl-source:69
تأكد_يساوي(أقصر_ثنائي("ز", "ط"), 7, "من ز إلى ط")
# apl-source:70
print("انتهى البحث")
# apl-source:71
