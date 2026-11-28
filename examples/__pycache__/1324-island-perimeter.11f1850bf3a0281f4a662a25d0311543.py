
# apl-source:1
# مثال 1324 — محيط جزيرة
# apl-source:2
# Island perimeter
# apl-source:3
# Demonstrates: شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1324-island-perimeter.apl
# apl-source:6

# apl-source:7
# كل خلية أرض تضيف أربعة أضلاع
# apl-source:8
# ونطرح ضلعين لكل جارين من الأرض
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
def محيط(ش):
  # apl-source:19
  م = 0
  # apl-source:20
  for ص in range(len(ش)):
    # apl-source:21
    for ج in range(len(ش[0])):
      # apl-source:22
      if ش[ص][ج] == 1:
        # apl-source:23
        م = م + 4
        # apl-source:24
        if (ص > 0) and (ش[ص - 1][ج] == 1):
          # apl-source:25
          م = م - 2
        # apl-source:26
        if (ج > 0) and (ش[ص][ج - 1] == 1):
          # apl-source:27
          م = م - 2
  # apl-source:28
  return م
# apl-source:29

# apl-source:30
تأكد_يساوي(محيط([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), 16, "مثال أول")
# apl-source:31
تأكد_يساوي(محيط([[1]]), 4, "خلية")
# apl-source:32
تأكد_يساوي(محيط([[1,0]]), 4, "خلية مع ماء")
# apl-source:33
