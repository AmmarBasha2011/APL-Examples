
# apl-source:1
# مثال 1198 — المحيطان
# apl-source:2
# Pacific Atlantic water flow
# apl-source:3
# Demonstrates: بحث بالعمق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1198-pacific-atlantic.apl
# apl-source:6

# apl-source:7
# نبدأ من حافة كل محيط ونصعد إلى الأعلى ارتفاعاً
# apl-source:8
# والتقاطع هو الخانات المطلوبة
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
def وصول(ش, بدايات):
  # apl-source:19
  ر_ = len(ش)
  # apl-source:20
  ك_ = len(ش[0])
  # apl-source:21
  مرئي = []
  # apl-source:22
  for ص in range(ر_):
    # apl-source:23
    مرئي = مرئي + [[False] * ك_]
  # apl-source:24
  مكدس = list(بدايات)
  # apl-source:25
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:26
  for ب in بدايات:
    # apl-source:27
    مرئي[ب[0]][ب[1]] = True
  # apl-source:28
  while len(مكدس) > 0:
    # apl-source:29
    ن = مكدس.pop()
    # apl-source:30
    for د in اتجاهات:
      # apl-source:31
      ر = ن[0] + د[0]
      # apl-source:32
      ك = ن[1] + د[1]
      # apl-source:33
      if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
        # apl-source:34
        if (not مرئي[ر][ك]) and (ش[ر][ك] >= ش[ن[0]][ن[1]]):
          # apl-source:35
          مرئي[ر][ك] = True
          # apl-source:36
          مكدس = مكدس + [[ر, ك]]
  # apl-source:37
  return مرئي
# apl-source:38

# apl-source:39
def محيطان(ش):
  # apl-source:40
  ر_ = len(ش)
  # apl-source:41
  ك_ = len(ش[0])
  # apl-source:42
  هادي = []
  # apl-source:43
  اطلسي = []
  # apl-source:44
  for ص in range(ر_):
    # apl-source:45
    هادي = هادي + [[ص, 0]]
    # apl-source:46
    اطلسي = اطلسي + [[ص, ك_ - 1]]
  # apl-source:47
  for ج in range(ك_):
    # apl-source:48
    هادي = هادي + [[0, ج]]
    # apl-source:49
    اطلسي = اطلسي + [[ر_ - 1, ج]]
  # apl-source:50
  أ = وصول(ش, هادي)
  # apl-source:51
  ب = وصول(ش, اطلسي)
  # apl-source:52
  ناتج = []
  # apl-source:53
  for ص in range(ر_):
    # apl-source:54
    for ج in range(ك_):
      # apl-source:55
      if أ[ص][ج] and ب[ص][ج]:
        # apl-source:56
        ناتج = ناتج + [[ص, ج]]
  # apl-source:57
  return ناتج
# apl-source:58

# apl-source:59
م = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# apl-source:60
تأكد_يساوي(محيطان(م), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]], "مثال أول")
# apl-source:61
تأكد_يساوي(محيطان([[1]]), [[0,0]], "خلية")
# apl-source:62
