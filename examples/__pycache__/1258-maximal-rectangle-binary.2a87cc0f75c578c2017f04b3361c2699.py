
# apl-source:1
# مثال 1258 — أكبر مستطيل
# apl-source:2
# Maximal rectangle of ones
# apl-source:3
# Demonstrates: مدرج تكراري
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1258-maximal-rectangle-binary.apl
# apl-source:6

# apl-source:7
# نبني مدرجاً تكرارياً لكل صف
# apl-source:8
# ونحسب أكبر مستطيل فيه بمكدس
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
def اكبر_مدرج(ارتفاعات):
  # apl-source:19
  مكدس = []
  # apl-source:20
  اقصى = 0
  # apl-source:21
  ح = ارتفاعات + [0]
  # apl-source:22
  for ع in range(len(ح)):
    # apl-source:23
    while (len(مكدس) > 0) and (ح[مكدس[-1]] >= ح[ع]):
      # apl-source:24
      ارتفاع = ح[مكدس.pop()]
      # apl-source:25
      عرض = ع
      # apl-source:26
      if len(مكدس) > 0:
        # apl-source:27
        عرض = ع - مكدس[-1] - 1
      # apl-source:28
      if ارتفاع * عرض > اقصى:
        # apl-source:29
        اقصى = ارتفاع * عرض
    # apl-source:30
    مكدس = مكدس + [ع]
  # apl-source:31
  return اقصى
# apl-source:32

# apl-source:33
def اكبر_مستطيل(م):
  # apl-source:34
  if len(م) == 0:
    # apl-source:35
    return 0
  # apl-source:36
  ارتفاعات = [0] * len(م[0])
  # apl-source:37
  اقصى = 0
  # apl-source:38
  for صف in م:
    # apl-source:39
    for ج in range(len(صف)):
      # apl-source:40
      if صف[ج] == "1":
        # apl-source:41
        ارتفاعات[ج] = ارتفاعات[ج] + 1
      # apl-source:42
      else:
        # apl-source:43
        ارتفاعات[ج] = 0
    # apl-source:44
    ق = اكبر_مدرج(ارتفاعات)
    # apl-source:45
    if ق > اقصى:
      # apl-source:46
      اقصى = ق
  # apl-source:47
  return اقصى
# apl-source:48

# apl-source:49
م = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# apl-source:50
تأكد_يساوي(اكبر_مستطيل(م), 6, "مثال أول")
# apl-source:51
تأكد_يساوي(اكبر_مستطيل([["0"]]), 0, "صفر")
# apl-source:52
تأكد_يساوي(اكبر_مستطيل([["1"]]), 1, "واحد")
# apl-source:53
تأكد_يساوي(اكبر_مستطيل([]), 0, "فارغة")
# apl-source:54
