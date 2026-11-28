
# apl-source:1
# مثال 599 — خوارزمية ماناكر
# apl-source:2
# Manacher algorithm
# apl-source:3
# Demonstrates: ماناكر، متناظرة، مراكز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/599-manacher.apl
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
# خوارزمية ماناكر: أطول سلسلة متناظرة بخطية
# apl-source:25
# Demonstrates: توسيع حول مراكز مع مرايا, نص مفصول بعلامات
# apl-source:26
# أسرع من البرمجة الديناميكية لهذه المسألة
# apl-source:27

# apl-source:28
def أطول_متناظرة(نص):
  # apl-source:29
  مفصول = "#"
  # apl-source:30
  for حرف in نص:
    # apl-source:31
    مفصول = مفصول + حرف + "#"
  # apl-source:32
  ن = len(مفصول)
  # apl-source:33
  نصف = [0] * ن
  # apl-source:34
  مركز = 0
  # apl-source:35
  يمين = 0
  # apl-source:36
  for ي in range(ن):
    # apl-source:37
    مرآة = 2 * مركز - ي
    # apl-source:38
    if ي < يمين:
      # apl-source:39
      نصف[ي] = min(يمين - ي, نصف[مرآة])
    # apl-source:40
    أ = ي + نصف[ي] + 1
    # apl-source:41
    ب = ي - نصف[ي] - 1
    # apl-source:42
    while أ < ن and ب >= 0 and مفصول[أ] == مفصول[ب]:
      # apl-source:43
      نصف[ي] = نصف[ي] + 1
      # apl-source:44
      أ = أ + 1
      # apl-source:45
      ب = ب - 1
    # apl-source:46
    if ي + نصف[ي] > يمين:
      # apl-source:47
      مركز = ي
      # apl-source:48
      يمين = ي + نصف[ي]
  # apl-source:49
  أقصى = 0
  # apl-source:50
  for قيمة in نصف:
    # apl-source:51
    if قيمة > أقصى:
      # apl-source:52
      أقصى = قيمة
  # apl-source:53
  return أقصى
# apl-source:54

# apl-source:55
تأكد_يساوي(أطول_متناظرة("abacaba"), 7, "كامل النص متناظر")
# apl-source:56
تأكد_يساوي(أطول_متناظرة("abaxyzx"), 3, "أطولها aba")
# apl-source:57
تأكد_يساوي(أطول_متناظرة("abba"), 4, "زوجي الطول")
# apl-source:58
print("أطول متناظرة في abacaba:", أطول_متناظرة("abacaba"))
# apl-source:59
