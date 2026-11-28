
# apl-source:1
# مثال 1350 — السباحة في الماء المرتفع
# apl-source:2
# Swim in rising water
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1350-swim-rising-water.apl
# apl-source:6

# apl-source:7
# الزمن هو أكبر ارتفاع على المسار
# apl-source:8
# نبحث ثنائياً عن أقل زمن يسمح بالوصول
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
def يمكن_العبور(ش, زمن):
  # apl-source:19
  ن = len(ش)
  # apl-source:20
  if ش[0][0] > زمن:
    # apl-source:21
    return False
  # apl-source:22
  مرئي = []
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    مرئي = مرئي + [[False] * ن]
  # apl-source:25
  مرئي[0][0] = True
  # apl-source:26
  مكدس = [[0, 0]]
  # apl-source:27
  while len(مكدس) > 0:
    # apl-source:28
    ق = مكدس.pop()
    # apl-source:29
    if (ق[0] == ن - 1) and (ق[1] == ن - 1):
      # apl-source:30
      return True
    # apl-source:31
    for د in [[1,0],[-1,0],[0,1],[0,-1]]:
      # apl-source:32
      ص = ق[0] + د[0]
      # apl-source:33
      ج = ق[1] + د[1]
      # apl-source:34
      if (ص >= 0) and (ص < ن) and (ج >= 0) and (ج < ن):
        # apl-source:35
        if (not مرئي[ص][ج]) and (ش[ص][ج] <= زمن):
          # apl-source:36
          مرئي[ص][ج] = True
          # apl-source:37
          مكدس = مكدس + [[ص, ج]]
  # apl-source:38
  return False
# apl-source:39

# apl-source:40
def اقل_زمن(ش):
  # apl-source:41
  ادنى = 0
  # apl-source:42
  اعلى = len(ش) * len(ش)
  # apl-source:43
  while ادنى < اعلى:
    # apl-source:44
    وسط = (ادنى + اعلى) // 2
    # apl-source:45
    if يمكن_العبور(ش, وسط):
      # apl-source:46
      اعلى = وسط
    # apl-source:47
    else:
      # apl-source:48
      ادنى = وسط + 1
  # apl-source:49
  return ادنى
# apl-source:50

# apl-source:51
تأكد_يساوي(اقل_زمن([[0,2],[1,3]]), 3, "شبكة صغيرة")
# apl-source:52
تأكد_يساوي(اقل_زمن([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]), 16, "شبكة كبيرة")
# apl-source:53
تأكد_يساوي(اقل_زمن([[0]]), 0, "خلية")
# apl-source:54
