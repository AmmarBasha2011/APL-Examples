
# apl-source:1
# مثال 1385 — ثلاثيات جيدة
# apl-source:2
# Count good triplets
# apl-source:3
# Demonstrates: بحث شامل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1385-good-triplets-count.apl
# apl-source:6

# apl-source:7
# نجرب كل ثلاثة مواضع مرتبة
# apl-source:8
# ونتحقق من الفروق المطلقة الثلاثة
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
def abs(س):
  # apl-source:19
  if س < 0:
    # apl-source:20
    return -س
  # apl-source:21
  return س
# apl-source:22

# apl-source:23
def عد_جيدة(أرقام, أ, ب, ج):
  # apl-source:24
  عدد = 0
  # apl-source:25
  ن = len(أرقام)
  # apl-source:26
  for ي in range(ن):
    # apl-source:27
    for ك in range(ي + 1, ن):
      # apl-source:28
      if abs(أرقام[ي] - أرقام[ك]) <= أ:
        # apl-source:29
        for ل in range(ك + 1, ن):
          # apl-source:30
          if (abs(أرقام[ك] - أرقام[ل]) <= ب) and (abs(أرقام[ي] - أرقام[ل]) <= ج):
            # apl-source:31
            عدد = عدد + 1
  # apl-source:32
  return عدد
# apl-source:33

# apl-source:34
تأكد_يساوي(عد_جيدة([3,0,1,1,9,7], 7, 2, 3), 4, "أربع")
# apl-source:35
تأكد_يساوي(عد_جيدة([1,1,2,2,3], 0, 0, 1), 0, "لا شيء")
# apl-source:36
تأكد_يساوي(عد_جيدة([1,1,1], 0, 0, 0), 1, "ثلاثة متساوية")
# apl-source:37
