
# apl-source:1
# مثال 1317 — حلال سودوكو
# apl-source:2
# Sudoku solver backtracking small
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1317-sudoku-solver-mini.apl
# apl-source:6

# apl-source:7
# نجرب كل رقم في أول خانة فارغة
# apl-source:8
# ونتراجع عند التعارض
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
def يصلح(ل, ص, ج, ق):
  # apl-source:19
  for ك in range(4):
    # apl-source:20
    if (ل[ص][ك] == ق) or (ل[ك][ج] == ق):
      # apl-source:21
      return False
  # apl-source:22
  ر0 = (ص // 2) * 2
  # apl-source:23
  ك0 = (ج // 2) * 2
  # apl-source:24
  for ر in range(2):
    # apl-source:25
    for ك in range(2):
      # apl-source:26
      if ل[ر0 + ر][ك0 + ك] == ق:
        # apl-source:27
        return False
  # apl-source:28
  return True
# apl-source:29

# apl-source:30
def حل(ل):
  # apl-source:31
  for ص in range(4):
    # apl-source:32
    for ج in range(4):
      # apl-source:33
      if ل[ص][ج] == 0:
        # apl-source:34
        for ق in [1, 2, 3, 4]:
          # apl-source:35
          if يصلح(ل, ص, ج, ق):
            # apl-source:36
            ل[ص][ج] = ق
            # apl-source:37
            if حل(ل):
              # apl-source:38
              return True
            # apl-source:39
            ل[ص][ج] = 0
        # apl-source:40
        return False
  # apl-source:41
  return True
# apl-source:42

# apl-source:43
ل = [[1,0,0,0],[0,0,3,0],[0,4,0,0],[0,0,0,2]]
# apl-source:44
تأكد_يساوي(حل(ل), True, "حُلت")
# apl-source:45
for صف in ل:
  # apl-source:46
  تأكد_يساوي(sorted(صف), [1,2,3,4], "صف سليم")
# apl-source:47
