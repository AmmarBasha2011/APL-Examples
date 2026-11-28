
# apl-source:1
# مثال 1339 — مسار أقل جهد
# apl-source:2
# Path with minimum effort
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1339-path-min-effort.apl
# apl-source:6

# apl-source:7
# نبحث ثنائياً عن الجهد الأقصى
# apl-source:8
# ونختبر الوصول بالبحث بالعمق
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
def يصل_بجهد(ش, حد):
  # apl-source:19
  ر_ = len(ش)
  # apl-source:20
  ك_ = len(ش[0])
  # apl-source:21
  مرئي = []
  # apl-source:22
  for ع in range(ر_):
    # apl-source:23
    مرئي = مرئي + [[False] * ك_]
  # apl-source:24
  مكدس = [[0, 0]]
  # apl-source:25
  مرئي[0][0] = True
  # apl-source:26
  while len(مكدس) > 0:
    # apl-source:27
    ن = مكدس.pop()
    # apl-source:28
    if (ن[0] == ر_ - 1) and (ن[1] == ك_ - 1):
      # apl-source:29
      return True
    # apl-source:30
    for د in [[1,0],[-1,0],[0,1],[0,-1]]:
      # apl-source:31
      ص = ن[0] + د[0]
      # apl-source:32
      ج = ن[1] + د[1]
      # apl-source:33
      if (ص >= 0) and (ص < ر_) and (ج >= 0) and (ج < ك_):
        # apl-source:34
        if not مرئي[ص][ج]:
          # apl-source:35
          ف = ش[ص][ج] - ش[ن[0]][ن[1]]
          # apl-source:36
          if ف < 0:
            # apl-source:37
            ف = -ف
          # apl-source:38
          if ف <= حد:
            # apl-source:39
            مرئي[ص][ج] = True
            # apl-source:40
            مكدس = مكدس + [[ص, ج]]
  # apl-source:41
  return False
# apl-source:42

# apl-source:43
def اقل_جهد(ش):
  # apl-source:44
  ادنى = 0
  # apl-source:45
  اعلى = 1000000
  # apl-source:46
  while ادنى < اعلى:
    # apl-source:47
    وسط = (ادنى + اعلى) // 2
    # apl-source:48
    if يصل_بجهد(ش, وسط):
      # apl-source:49
      اعلى = وسط
    # apl-source:50
    else:
      # apl-source:51
      ادنى = وسط + 1
  # apl-source:52
  return ادنى
# apl-source:53

# apl-source:54
تأكد_يساوي(اقل_جهد([[1,2,2],[3,8,2],[5,3,5]]), 2, "جهد اثنان")
# apl-source:55
تأكد_يساوي(اقل_جهد([[1,2,3],[3,8,4],[5,3,5]]), 1, "جهد واحد")
# apl-source:56
تأكد_يساوي(اقل_جهد([[7]]), 0, "خلية")
# apl-source:57
