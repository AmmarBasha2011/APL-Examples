
# apl-source:1
# مثال 592 — تربيع المصفوفات
# apl-source:2
# Matrix exponentiation
# apl-source:3
# Demonstrates: مصفوفات، رفع لقوة، تريبوناتشي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/592-matrix-exponentiation.apl
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
# تربيع المصفوفات لحساب تريبوناتشي بسرعة
# apl-source:25
# Demonstrates: ضرب مصفوفات 3x3, رفع لقوة بالتربيع المتكرر, متتالية من الدرجة الثالثة
# apl-source:26
# ت(0)=0, ت(1)=1, ت(2)=1, ت(ن) = ت(ن-1)+ت(ن-2)+ت(ن-3)
# apl-source:27

# apl-source:28
def اضرب(أ, ب):
  # apl-source:29
  ن = len(أ)
  # apl-source:30
  ناتج = []
  # apl-source:31
  for سطر_ي in range(ن):
    # apl-source:32
    ناتج.append([0] * ن)
  # apl-source:33
  for س in range(ن):
    # apl-source:34
    for ص in range(ن):
      # apl-source:35
      مجموع = 0
      # apl-source:36
      for ك in range(ن):
        # apl-source:37
        مجموع = مجموع + أ[س][ك] * ب[ك][ص]
      # apl-source:38
      ناتج[س][ص] = مجموع
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
def قوة(مصفوفة, أ):
  # apl-source:42
  ن = len(مصفوفة)
  # apl-source:43
  ناتج = []
  # apl-source:44
  for سطر_ي in range(ن):
    # apl-source:45
    ناتج.append([0] * ن)
  # apl-source:46
  for ي in range(ن):
    # apl-source:47
    ناتج[ي][ي] = 1
  # apl-source:48
  أساس = مصفوفة
  # apl-source:49
  while أ > 0:
    # apl-source:50
    if أ % 2 == 1:
      # apl-source:51
      ناتج = اضرب(ناتج, أساس)
    # apl-source:52
    أساس = اضرب(أساس, أساس)
    # apl-source:53
    أ = أ // 2
  # apl-source:54
  return ناتج
# apl-source:55

# apl-source:56
def تريبو(ن):
  # apl-source:57
  if ن == 0:
    # apl-source:58
    return 0
  # apl-source:59
  if ن <= 2:
    # apl-source:60
    return 1
  # apl-source:61
  تحويل = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
  # apl-source:62
  مرفوعة = قوة(تحويل, ن - 2)
  # apl-source:63
  return مرفوعة[0][0] * 1 + مرفوعة[0][1] * 1 + مرفوعة[0][2] * 0
# apl-source:64

# apl-source:65
تأكد_يساوي(تريبو(5), 7, "ت(5)")
# apl-source:66
تأكد_يساوي(تريبو(10), 149, "ت(10)")
# apl-source:67
تأكد_يساوي(تريبو(20), 66012, "ت(20)")
# apl-source:68
print("ت(20) =", تريبو(20))
# apl-source:69
