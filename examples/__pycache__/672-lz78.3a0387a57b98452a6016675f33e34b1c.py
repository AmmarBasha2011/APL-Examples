
# apl-source:1
# مثال 672 — ضغط LZ78
# apl-source:2
# LZ78 compression
# apl-source:3
# Demonstrates: قاموس عبارات، ضغط، فك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/672-lz78.apl
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
# ضغط LZ78: قاموس عبارات متنامي
# apl-source:25
# Demonstrates: أزواج مرجع وحرف, قاموس مبني أثناء القراءة, فك بالمثل
# apl-source:26
# عبارة جديدة = عبارة معروفة + حرف واحد
# apl-source:27

# apl-source:28
def شفر(نص):
  # apl-source:29
  قاموس = {}
  # apl-source:30
  ناتج = []
  # apl-source:31
  جاري = ""
  # apl-source:32
  تالي = 1
  # apl-source:33
  for حرف in نص:
    # apl-source:34
    مركب = جاري + حرف
    # apl-source:35
    if قاموس.get(مركب, None) != None:
      # apl-source:36
      جاري = مركب
    # apl-source:37
    else:
      # apl-source:38
      ناتج.append([قاموس.get(جاري, 0), حرف])
      # apl-source:39
      قاموس[مركب] = تالي
      # apl-source:40
      تالي = تالي + 1
      # apl-source:41
      جاري = ""
  # apl-source:42
  if جاري != "":
    # apl-source:43
    ناتج.append([قاموس.get(جاري, 0), ""])
  # apl-source:44
  return ناتج
# apl-source:45

# apl-source:46
def فك(ناتج):
  # apl-source:47
  عبارات = [""]
  # apl-source:48
  نص = ""
  # apl-source:49
  for زوج in ناتج:
    # apl-source:50
    عبارة = عبارات[زوج[0]] + زوج[1]
    # apl-source:51
    نص = نص + عبارة
    # apl-source:52
    if زوج[1] != "":
      # apl-source:53
      عبارات.append(عبارة)
  # apl-source:54
  return نص
# apl-source:55

# apl-source:56
ناتج = شفر("ABABABABA")
# apl-source:57
تأكد_يساوي(ناتج[0], [0, "A"], "أول زوج")
# apl-source:58
تأكد_يساوي(ناتج[1], [0, "B"], "ثاني زوج")
# apl-source:59
تأكد_يساوي(ناتج[2], [1, "B"], "مرجع لعبارة A")
# apl-source:60
تأكد_يساوي(فك(ناتج), "ABABABABA", "فك يعيد النص")
# apl-source:61
تأكد_يساوي(فك(شفر("AAAAAA")), "AAAAAA", "نص متكرر")
# apl-source:62
تأكد_يساوي(فك(شفر("")), "", "فارغ")
# apl-source:63
print("أزواج:", ناتج)
# apl-source:64
