
# apl-source:1
# مثال 760 — تحليل نيويك
# apl-source:2
# Newick tree parsing
# apl-source:3
# Demonstrates: نزول عودي، أطوال فروع، عقد داخلية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/760-newick-parse.apl
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
# تحليل صيغة نيويك لأشجار التطور: (A:0.1,B:0.2,(C:0.3,D:0.4):0.5)
# apl-source:25
# Demonstrates: نزول عودي بمؤشر قابل للتغيير, أطوال فروع, عقد داخلية
# apl-source:26
# المؤشر قائمة من عنصر واحد لأن APL يمرر القيم بالنسخ
# apl-source:27

# apl-source:28
def حلل_عشري(رقم):
  # apl-source:29
  أجزاء = رقم.split(".")
  # apl-source:30
  if len(أجزاء) == 1:
    # apl-source:31
    return int(رقم) * 1.0
  # apl-source:32
  مقام = 1
  # apl-source:33
  for ي in range(len(أجزاء[1])):
    # apl-source:34
    مقام = مقام * 10
  # apl-source:35
  return int(أجزاء[0]) + int(أجزاء[1]) / مقام
# apl-source:36

# apl-source:37
def عقدة(نص, مؤشر):
  # apl-source:38
  أبناء = []
  # apl-source:39
  اسم = ""
  # apl-source:40
  طول_فرع = 0.0
  # apl-source:41
  if نص[مؤشر[0]] == "(":
    # apl-source:42
    مؤشر[0] = مؤشر[0] + 1
    # apl-source:43
    مستمر = True
    # apl-source:44
    while مستمر:
      # apl-source:45
      أبناء.append(عقدة(نص, مؤشر))
      # apl-source:46
      if نص[مؤشر[0]] == ",":
        # apl-source:47
        مؤشر[0] = مؤشر[0] + 1
      # apl-source:48
      elif نص[مؤشر[0]] == ")":
        # apl-source:49
        مؤشر[0] = مؤشر[0] + 1
        # apl-source:50
        مستمر = False
  # apl-source:51
  while مؤشر[0] < len(نص) and نص[مؤشر[0]] != "," and نص[مؤشر[0]] != ")" and نص[مؤشر[0]] != ":" and نص[مؤشر[0]] != ";":
    # apl-source:52
    اسم = اسم + نص[مؤشر[0]]
    # apl-source:53
    مؤشر[0] = مؤشر[0] + 1
  # apl-source:54
  if مؤشر[0] < len(نص) and نص[مؤشر[0]] == ":":
    # apl-source:55
    مؤشر[0] = مؤشر[0] + 1
    # apl-source:56
    رقم = ""
    # apl-source:57
    while مؤشر[0] < len(نص) and نص[مؤشر[0]] != "," and نص[مؤشر[0]] != ")" and نص[مؤشر[0]] != ";":
      # apl-source:58
      رقم = رقم + نص[مؤشر[0]]
      # apl-source:59
      مؤشر[0] = مؤشر[0] + 1
    # apl-source:60
    طول_فرع = حلل_عشري(رقم)
  # apl-source:61
  return {"اسم": اسم, "طول": طول_فرع, "أبناء": أبناء}
# apl-source:62

# apl-source:63
def أوراق(عقدة):
  # apl-source:64
  if len(عقدة["أبناء"]) == 0:
    # apl-source:65
    return [عقدة["اسم"]]
  # apl-source:66
  ناتج = []
  # apl-source:67
  for ابن in عقدة["أبناء"]:
    # apl-source:68
    for ورقة in أوراق(ابن):
      # apl-source:69
      ناتج.append(ورقة)
  # apl-source:70
  return ناتج
# apl-source:71

# apl-source:72
def مجموع_الأطوال(عقدة):
  # apl-source:73
  مجموع = عقدة["طول"]
  # apl-source:74
  for ابن in عقدة["أبناء"]:
    # apl-source:75
    مجموع = مجموع + مجموع_الأطوال(ابن)
  # apl-source:76
  return مجموع
# apl-source:77

# apl-source:78
def عقد_داخلية(عقدة):
  # apl-source:79
  if len(عقدة["أبناء"]) == 0:
    # apl-source:80
    return 0
  # apl-source:81
  مجموع = 1
  # apl-source:82
  for ابن in عقدة["أبناء"]:
    # apl-source:83
    مجموع = مجموع + عقد_داخلية(ابن)
  # apl-source:84
  return مجموع
# apl-source:85

# apl-source:86
شجرة = عقدة("(A:0.1,B:0.2,(C:0.3,D:0.4):0.5);", [0])
# apl-source:87

# apl-source:88
تأكد_يساوي(أوراق(شجرة), ["A", "B", "C", "D"], "أربع أوراق")
# apl-source:89
تأكد_يساوي(round(مجموع_الأطوال(شجرة), 4), 1.5, "مجموع الأطوال")
# apl-source:90
تأكد_يساوي(عقد_داخلية(شجرة), 2, "عقدتان داخليتان")
# apl-source:91
تأكد_يساوي(شجرة["أبناء"][2]["طول"], 0.5, "فرع العقدة الداخلية")
# apl-source:92

# apl-source:93
بسيطة = عقدة("(X:1.0,Y:2.0)", [0])
# apl-source:94
تأكد_يساوي(أوراق(بسيطة), ["X", "Y"], "شجرة بسيطة")
# apl-source:95
تأكد_يساوي(عقد_داخلية(بسيطة), 1, "جذر فقط")
# apl-source:96

# apl-source:97
print("الأوراق:", أوراق(شجرة))
# apl-source:98
