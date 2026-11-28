
# apl-source:1
# مثال 1096 — لعبة البيسبول
# apl-source:2
# Baseball game scoring
# apl-source:3
# Demonstrates: مكدس النتائج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1096-baseball-game.apl
# apl-source:6

# apl-source:7
# العدد يضاف نقاطاً وC يلغي آخر نقطة وD يضاعفها و + يجمع آخر نقطتين
# apl-source:8
# نخزن النقاط في مكدس ونجمعها في النهاية
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
def نقاط(عمليات):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ع in عمليات:
    # apl-source:21
    if ع == "C":
      # apl-source:22
      مكدس.pop()
    # apl-source:23
    elif ع == "D":
      # apl-source:24
      مكدس = مكدس + [مكدس[len(مكدس) - 1] * 2]
    # apl-source:25
    elif ع == "+":
      # apl-source:26
      مكدس = مكدس + [مكدس[len(مكدس) - 1] + مكدس[len(مكدس) - 2]]
    # apl-source:27
    else:
      # apl-source:28
      مكدس = مكدس + [int(ع)]
  # apl-source:29
  مجموع_ = 0
  # apl-source:30
  for س in مكدس:
    # apl-source:31
    مجموع_ = مجموع_ + س
  # apl-source:32
  return مجموع_
# apl-source:33

# apl-source:34
تأكد_يساوي(نقاط(["5", "2", "C", "D", "+"]), 30, "مثال أول")
# apl-source:35
تأكد_يساوي(نقاط(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27, "مثال ثان")
# apl-source:36
تأكد_يساوي(نقاط(["1"]), 1, "نقطة واحدة")
# apl-source:37
