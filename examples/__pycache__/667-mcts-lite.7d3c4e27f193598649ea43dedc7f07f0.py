
# apl-source:1
# مثال 667 — نواة UCB1 لبحث مونت كارلو
# apl-source:2
# UCB1 MCTS core
# apl-source:3
# Demonstrates: UCB1، استكشاف، استغلال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/667-mcts-lite.apl
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
# UCB1: نواة بحث مونت كارلو الشجري
# apl-source:25
# Demonstrates: حد ثقة أعلى, استكشاف واستغلال, بذرة ثابتة
# apl-source:26
# نفس معادلة الاختيار التي تقود MCTS الكامل
# apl-source:27

# apl-source:28
بذرة = [1]
# apl-source:29
def تالي(ب):
  # apl-source:30
  ب[0] = (ب[0] * 1103515245 + 12345) % 2147483648
  # apl-source:31
  return ب[0]
# apl-source:32

# apl-source:33
def محاولة(ذراع):
  # apl-source:34
  حد = [500, 700, 900]
  # apl-source:35
  return تالي(بذرة) % 1000 < حد[ذراع]
# apl-source:36

# apl-source:37
def جذر_تقريبي(ن):
  # apl-source:38
  س = ن * 1.0
  # apl-source:39
  for ي in range(20):
    # apl-source:40
    س = (س + ن / س) / 2.0
  # apl-source:41
  return س
# apl-source:42

# apl-source:43
def لوغ_تقريبي(س):
  # apl-source:44
  if س <= 0.0:
    # apl-source:45
    return 0.0
  # apl-source:46
  ن = 0.0
  # apl-source:47
  بينما = س
  # apl-source:48
  while بينما > 2.718281828:
    # apl-source:49
    بينما = بينما / 2.718281828
    # apl-source:50
    ن = ن + 1.0
  # apl-source:51
  باقي = بينما - 1.0
  # apl-source:52
  return ن + باقي - باقي * باقي / 2.0 + باقي * باقي * باقي / 3.0
# apl-source:53

# apl-source:54
زيارات = [1, 1, 1]
# apl-source:55
فوز = [0, 0, 0]
# apl-source:56
for ذراع in range(3):
  # apl-source:57
  if محاولة(ذراع):
    # apl-source:58
    فوز[ذراع] = فوز[ذراع] + 1
# apl-source:59

# apl-source:60
def اختر_ucb(زيارات, فوز, كلي):
  # apl-source:61
  أفضل = 0
  # apl-source:62
  أعلى = -1.0
  # apl-source:63
  for ذراع in range(3):
    # apl-source:64
    معدل = فوز[ذراع] * 1.0 / زيارات[ذراع]
    # apl-source:65
    استكشاف = 2.0 * لوغ_تقريبي(كلي) / زيارات[ذراع]
    # apl-source:66
    قيمة = معدل + جذر_تقريبي(استكشاف * 100.0) / 10.0
    # apl-source:67
    if قيمة > أعلى:
      # apl-source:68
      أعلى = قيمة
      # apl-source:69
      أفضل = ذراع
  # apl-source:70
  return أفضل
# apl-source:71

# apl-source:72
for دورة in range(300):
  # apl-source:73
  كلي = زيارات[0] + زيارات[1] + زيارات[2]
  # apl-source:74
  ذراع = اختر_ucb(زيارات, فوز, كلي * 1.0)
  # apl-source:75
  زيارات[ذراع] = زيارات[ذراع] + 1
  # apl-source:76
  if محاولة(ذراع):
    # apl-source:77
    فوز[ذراع] = فوز[ذراع] + 1
# apl-source:78

# apl-source:79
تأكد_يساوي(زيارات[2] > زيارات[0], True, "الأفضل جرب أكثر")
# apl-source:80
تأكد_يساوي(زيارات[2] > زيارات[1], True, "الأفضل جرب أكثر من الوسط")
# apl-source:81
تأكد_يساوي(زيارات[0] + زيارات[1] + زيارات[2], 303, "عدد المحاولات")
# apl-source:82
print("زيارات:", زيارات)
# apl-source:83
