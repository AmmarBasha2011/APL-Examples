
# apl-source:1
# مثال 682 — نملة لانغتون
# apl-source:2
# Langton's ant
# apl-source:3
# Demonstrates: نملة، اتجاهات دوارة، طريق سريع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/682-langton-ant.apl
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
# نملة لانغتون: فوضى ثم طريق سريع
# apl-source:25
# Demonstrates: آلة خلوية متحركة, اتجاهات دوارة, شبكة قابلة للالتفاف ممنوع
# apl-source:26
# الاتجاهات: 0=أعلى 1=يمين 2=أسفل 3=يسار
# apl-source:27

# apl-source:28
def محاكاة(خطوات, مقاس):
  # apl-source:29
  شبكة = []
  # apl-source:30
  for ي in range(مقاس):
    # apl-source:31
    صف = []
    # apl-source:32
    for ج in range(مقاس):
      # apl-source:33
      صف.append(0)
    # apl-source:34
    شبكة.append(صف)
  # apl-source:35
  ص = مقاس // 2
  # apl-source:36
  ع = مقاس // 2
  # apl-source:37
  اتجاه = 0
  # apl-source:38
  دص = [-1, 0, 1, 0]
  # apl-source:39
  دع = [0, 1, 0, -1]
  # apl-source:40
  for خ in range(خطوات):
    # apl-source:41
    if شبكة[ص][ع] == 0:
      # apl-source:42
      اتجاه = (اتجاه + 1) % 4
      # apl-source:43
      شبكة[ص][ع] = 1
    # apl-source:44
    else:
      # apl-source:45
      اتجاه = (اتجاه + 3) % 4
      # apl-source:46
      شبكة[ص][ع] = 0
    # apl-source:47
    ص = ص + دص[اتجاه]
    # apl-source:48
    ع = ع + دع[اتجاه]
  # apl-source:49
  سوداء = 0
  # apl-source:50
  for ص2 in range(مقاس):
    # apl-source:51
    for ع2 in range(مقاس):
      # apl-source:52
      سوداء = سوداء + شبكة[ص2][ع2]
  # apl-source:53
  return [سوداء, ص, ع, اتجاه]
# apl-source:54

# apl-source:55
ن4 = محاكاة(4, 21)
# apl-source:56
تأكد_يساوي(ن4[0], 4, "بعد 4 خطوات أربع خلايا سوداء")
# apl-source:57
ن10 = محاكاة(10, 21)
# apl-source:58
تأكد_يساوي(ن10[0], 6, "بعد 10 خطوات ست خلايا سوداء")
# apl-source:59
ن100 = محاكاة(100, 21)
# apl-source:60
تأكد_يساوي(ن100[0], 20, "بعد 100 خطوة 20 خلية سوداء")
# apl-source:61
ن11000 = محاكاة(11000, 101)
# apl-source:62
print("سوداء بعد 11000:", ن11000[0])
# apl-source:63
تأكد_يساوي(ن11000[0] > 700 and ن11000[0] < 900, True, "الطريق السريع شكل نمطا كثيفا")
# apl-source:64
