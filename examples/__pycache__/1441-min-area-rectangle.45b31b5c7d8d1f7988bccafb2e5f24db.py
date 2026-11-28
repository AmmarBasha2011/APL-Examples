
# apl-source:1
# مثال 1441 — أصغر مستطيل
# apl-source:2
# Minimum area axis-parallel rectangle
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1441-min-area-rectangle.apl
# apl-source:6

# apl-source:7
# نجرب كل زوج كقطر
# apl-source:8
# ونتحقق من وجود الرأسين الآخرين
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
def اصغر_مساحة(نقاط):
  # apl-source:19
  موجود = {}
  # apl-source:20
  for ن in نقاط:
    # apl-source:21
    موجود[str(ن[0]) + "," + str(ن[1])] = True
  # apl-source:22
  افضل = 0
  # apl-source:23
  for ي in range(len(نقاط)):
    # apl-source:24
    for ك in range(ي + 1, len(نقاط)):
      # apl-source:25
      أ = نقاط[ي]
      # apl-source:26
      ب = نقاط[ك]
      # apl-source:27
      if (أ[0] != ب[0]) and (أ[1] != ب[1]):
        # apl-source:28
        ج = str(أ[0]) + "," + str(ب[1])
        # apl-source:29
        د = str(ب[0]) + "," + str(أ[1])
        # apl-source:30
        if موجود.get(ج, False) and موجود.get(د, False):
          # apl-source:31
          ع = ب[0] - أ[0]
          # apl-source:32
          if ع < 0:
            # apl-source:33
            ع = -ع
          # apl-source:34
          ط = ب[1] - أ[1]
          # apl-source:35
          if ط < 0:
            # apl-source:36
            ط = -ط
          # apl-source:37
          if (افضل == 0) or (ع * ط < افضل):
            # apl-source:38
            افضل = ع * ط
  # apl-source:39
  return افضل
# apl-source:40

# apl-source:41
تأكد_يساوي(اصغر_مساحة([[1,1],[1,3],[3,1],[3,3],[2,2]]), 4, "أربعة")
# apl-source:42
تأكد_يساوي(اصغر_مساحة([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]), 2, "اثنان")
# apl-source:43
تأكد_يساوي(اصغر_مساحة([[0,0],[1,1]]), 0, "لا مستطيل")
# apl-source:44
