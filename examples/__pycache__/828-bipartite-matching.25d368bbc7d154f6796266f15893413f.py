
# apl-source:1
# مثال 828 — التطابق الثنائي
# apl-source:2
# Bipartite matching
# apl-source:3
# Demonstrates: مسارات تحسينية بDFS
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/828-bipartite-matching.apl
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
# تطابق أقصى في مخطط ثنائي بمسارات تحسينية (خوارزمية كون)
# apl-source:25
# Demonstrates: مسار متناوب بDFS, إعادة إسناد, تطابق أقصى
# apl-source:26

# apl-source:27
جوار = [[1, 2], [1], [2, 3]]
# apl-source:28
عدد_يسار = 3
# apl-source:29

# apl-source:30
def تطابق_أقصى():
  # apl-source:31
  تطابق = [-1, -1, -1, -1]
  # apl-source:32
  def حاول(عقدة, مزار):
    # apl-source:33
    for يمين in جوار[عقدة]:
      # apl-source:34
      if (يمين in مزار) == False:
        # apl-source:35
        مزار.append(يمين)
        # apl-source:36
        if تطابق[يمين] == -1 or حاول(تطابق[يمين], مزار):
          # apl-source:37
          تطابق[يمين] = عقدة
          # apl-source:38
          return 1
    # apl-source:39
    return 0
  # apl-source:40
  عدد = 0
  # apl-source:41
  for عقدة in range(عدد_يسار):
    # apl-source:42
    if حاول(عقدة, []) == 1:
      # apl-source:43
      عدد = عدد + 1
  # apl-source:44
  return [عدد, تطابق]
# apl-source:45

# apl-source:46
نتيجة = تطابق_أقصى()
# apl-source:47
تأكد_يساوي(نتيجة[0], 3, "تطابق كامل")
# apl-source:48
تأكد_يساوي(نتيجة[1], [-1, 1, 0, 2], "الإسناد النهائي")
# apl-source:49
جوار2 = [[1], [1], [2]]
# apl-source:50
جوار = جوار2
# apl-source:51
نتيجة2 = تطابق_أقصى()
# apl-source:52
تأكد_يساوي(نتيجة2[0], 2, "تطابق جزئي")
# apl-source:53
