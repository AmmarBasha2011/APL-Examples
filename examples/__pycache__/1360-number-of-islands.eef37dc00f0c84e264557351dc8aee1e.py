
# apl-source:1
# مثال 1360 — عدد الجزر
# apl-source:2
# Number of islands
# apl-source:3
# Demonstrates: بحث بالعمق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1360-number-of-islands.apl
# apl-source:6

# apl-source:7
# نمشي بالعمق من كل أرض جديدة
# apl-source:8
# ونعلم كل ما نصل إليه كمزور
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
def عد_الجزر(ش):
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
  عدد = 0
  # apl-source:25
  for ص in range(ر_):
    # apl-source:26
    for ج in range(ك_):
      # apl-source:27
      if (ش[ص][ج] == 1) and (not مرئي[ص][ج]):
        # apl-source:28
        عدد = عدد + 1
        # apl-source:29
        مرئي[ص][ج] = True
        # apl-source:30
        مكدس = [[ص, ج]]
        # apl-source:31
        while len(مكدس) > 0:
          # apl-source:32
          ن = مكدس.pop()
          # apl-source:33
          for د in [[1,0],[-1,0],[0,1],[0,-1]]:
            # apl-source:34
            ر = ن[0] + د[0]
            # apl-source:35
            ك = ن[1] + د[1]
            # apl-source:36
            if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
              # apl-source:37
              if (ش[ر][ك] == 1) and (not مرئي[ر][ك]):
                # apl-source:38
                مرئي[ر][ك] = True
                # apl-source:39
                مكدس = مكدس + [[ر, ك]]
  # apl-source:40
  return عدد
# apl-source:41

# apl-source:42
تأكد_يساوي(عد_الجزر([[1,1,0],[0,1,0],[0,0,1]]), 2, "جزيرتان")
# apl-source:43
تأكد_يساوي(عد_الجزر([[1,0,1],[0,1,0],[1,0,1]]), 5, "خمس جزر")
# apl-source:44
تأكد_يساوي(عد_الجزر([[0]]), 0, "ماء")
# apl-source:45
