
# apl-source:1
# مثال 1267 — كاشف الألغام
# apl-source:2
# Minesweeper neighbor counts
# apl-source:3
# Demonstrates: شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1267-minesweeper-count.apl
# apl-source:6

# apl-source:7
# نمر على الخانات ونعد الألغام في الجيران الثمانية
# apl-source:8
# ونتجاهل خانة اللغم نفسها
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
def عد_الغام(ش):
  # apl-source:19
  ر_ = len(ش)
  # apl-source:20
  ك_ = len(ش[0])
  # apl-source:21
  ناتج = []
  # apl-source:22
  for ص in range(ر_):
    # apl-source:23
    صف = []
    # apl-source:24
    for ج in range(ك_):
      # apl-source:25
      if ش[ص][ج] == "*":
        # apl-source:26
        صف = صف + ["*"]
      # apl-source:27
      else:
        # apl-source:28
        ع = 0
        # apl-source:29
        for د1 in [-1, 0, 1]:
          # apl-source:30
          for د2 in [-1, 0, 1]:
            # apl-source:31
            ر = ص + د1
            # apl-source:32
            ك = ج + د2
            # apl-source:33
            if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
              # apl-source:34
              if ش[ر][ك] == "*":
                # apl-source:35
                ع = ع + 1
        # apl-source:36
        صف = صف + [str(ع)]
    # apl-source:37
    ناتج = ناتج + [صف]
  # apl-source:38
  return ناتج
# apl-source:39

# apl-source:40
تأكد_يساوي(عد_الغام([[".","*","."],[".",".","."],["*",".","."]]), [["1","*","1"],["2","2","1"],["*","1","0"]], "لوحة صغيرة")
# apl-source:41
تأكد_يساوي(عد_الغام([["."]]), [["0"]], "خانة")
# apl-source:42
تأكد_يساوي(عد_الغام([["*","*"]]), [["*","*"]], "ألغام فقط")
# apl-source:43
