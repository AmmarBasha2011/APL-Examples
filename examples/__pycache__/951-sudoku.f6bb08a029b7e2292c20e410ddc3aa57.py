
# apl-source:1
# مثال 951 — حل السودوكو
# apl-source:2
# Sudoku solver
# apl-source:3
# Demonstrates: تراجع مع فحص صلاحية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/951-sudoku.apl
# apl-source:6

# apl-source:7
# حل السودوكو بالتراجع: جرب رقماً صالحاً وتراجع عند الانسداد
# apl-source:8
# الصلاحية: لا تكرار في الصف أو العمود أو الصندوق
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
شبكة = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# apl-source:19

# apl-source:20
def صالح(صف, عمود, رقم):
  # apl-source:21
  for i in range(9):
    # apl-source:22
    if شبكة[صف][i] == رقم:
      # apl-source:23
      return False
    # apl-source:24
    if شبكة[i][عمود] == رقم:
      # apl-source:25
      return False
  # apl-source:26
  صف_صندوق = (صف // 3) * 3
  # apl-source:27
  عمود_صندوق = (عمود // 3) * 3
  # apl-source:28
  for i in range(3):
    # apl-source:29
    for ج in range(3):
      # apl-source:30
      if شبكة[صف_صندوق + i][عمود_صندوق + ج] == رقم:
        # apl-source:31
        return False
  # apl-source:32
  return 1 == 1
# apl-source:33

# apl-source:34
def احلل():
  # apl-source:35
  for صف in range(9):
    # apl-source:36
    for عمود in range(9):
      # apl-source:37
      if شبكة[صف][عمود] == 0:
        # apl-source:38
        for رقم in range(1, 10):
          # apl-source:39
          if صالح(صف, عمود, رقم):
            # apl-source:40
            شبكة[صف][عمود] = رقم
            # apl-source:41
            if احلل():
              # apl-source:42
              return 1 == 1
            # apl-source:43
            شبكة[صف][عمود] = 0
        # apl-source:44
        return False
  # apl-source:45
  return 1 == 1
# apl-source:46

# apl-source:47
if احلل():
  # apl-source:48
  print("حُلت")
# apl-source:49
else:
  # apl-source:50
  print("فشل: لا حل")
  # apl-source:51
  قياسي_نظام_اخرج(1)
# apl-source:52

# apl-source:53
# الصف الأول من الحل المعروف
# apl-source:54
متوقع = [5, 3, 4, 6, 7, 8, 9, 1, 2]
# apl-source:55
for ج in range(9):
  # apl-source:56
  تأكد_يساوي(شبكة[0][ج], متوقع[ج], "صف أول " + str(ج))
# apl-source:57

# apl-source:58
# لا أصفار ولا تكرار في أي صف
# apl-source:59
for صف in range(9):
  # apl-source:60
  مجموع = 0
  # apl-source:61
  for عمود in range(9):
    # apl-source:62
    مجموع = مجموع + شبكة[صف][عمود]
  # apl-source:63
  تأكد_يساوي(مجموع, 45, "مجموع صف " + str(صف))
# apl-source:64
