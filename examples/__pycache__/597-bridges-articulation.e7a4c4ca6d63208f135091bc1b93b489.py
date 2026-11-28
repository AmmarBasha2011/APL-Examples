
# apl-source:1
# مثال 597 — الجسور ونقاط الارتكاز
# apl-source:2
# Bridges and articulation points
# apl-source:3
# Demonstrates: جسور، نقاط ارتكاز، DFS بأزمنة دخول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/597-bridges-articulation.apl
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
# الجسور ونقاط الارتكاز في رسم غير موجه
# apl-source:25
# Demonstrates: DFS بأزمنة دخول, قيم دنيا, كشف الحواف الحرجة
# apl-source:26
# حذف جسر أو نقطة ارتكاز يفصل الرسم إلى قسمين
# apl-source:27

# apl-source:28
جوار = {0: [1], 1: [0, 2, 3], 2: [1], 3: [1, 4], 4: [3]}
# apl-source:29
ن = 5
# apl-source:30
دخول = [-1] * ن
# apl-source:31
أدنى = [-1] * ن
# apl-source:32
جسور = []
# apl-source:33
ارتكاز = []
# apl-source:34
عداد = [0]
# apl-source:35

# apl-source:36
def غاص(عقدة, أب):
  # apl-source:37
  دخول[عقدة] = عداد[0]
  # apl-source:38
  أدنى[عقدة] = عداد[0]
  # apl-source:39
  عداد[0] = عداد[0] + 1
  # apl-source:40
  أبناء = 0
  # apl-source:41
  هو_ارتكاز = False
  # apl-source:42
  for جار in جوار[عقدة]:
    # apl-source:43
    if جار != أب:
      # apl-source:44
      if دخول[جار] != -1:
        # apl-source:45
        أدنى[عقدة] = min(أدنى[عقدة], دخول[جار])
      # apl-source:46
      else:
        # apl-source:47
        غاص(جار, عقدة)
        # apl-source:48
        أدنى[عقدة] = min(أدنى[عقدة], أدنى[جار])
        # apl-source:49
        if أدنى[جار] > دخول[عقدة]:
          # apl-source:50
          جسور.append([عقدة, جار])
        # apl-source:51
        if أدنى[جار] >= دخول[عقدة] and أب != -1:
          # apl-source:52
          هو_ارتكاز = True
        # apl-source:53
        أبناء = أبناء + 1
  # apl-source:54
  if أب == -1 and أبناء > 1:
    # apl-source:55
    هو_ارتكاز = True
  # apl-source:56
  if هو_ارتكاز:
    # apl-source:57
    ارتكاز.append(عقدة)
# apl-source:58

# apl-source:59
غاص(0, -1)
# apl-source:60
print("الجسور:", جسور)
# apl-source:61
print("نقاط الارتكاز:", ارتكاز)
# apl-source:62
جسور.sort()
# apl-source:63
تأكد_يساوي(جسور, [[0, 1], [1, 2], [1, 3], [3, 4]], "أربعة جسور (شجرة)")
# apl-source:64
ارتكاز.sort()
# apl-source:65
تأكد_يساوي(ارتكاز, [1, 3], "نقطتا ارتكاز")
# apl-source:66
