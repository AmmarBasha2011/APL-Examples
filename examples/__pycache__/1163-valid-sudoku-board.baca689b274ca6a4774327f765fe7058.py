
# apl-source:1
# مثال 1163 — لوحة سودوكو صالحة
# apl-source:2
# Validate sudoku board
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1163-valid-sudoku-board.apl
# apl-source:6

# apl-source:7
# لا يتكرر رقم في صف ولا عمود ولا مربع 3x3
# apl-source:8
# نستخدم قائمة مرئيات لكل وحدة
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
def صالحة(لوحة):
  # apl-source:19
  صفوف = []
  # apl-source:20
  اعمدة = []
  # apl-source:21
  مربعات = []
  # apl-source:22
  for ع in range(9):
    # apl-source:23
    صفوف = صفوف + [[]]
    # apl-source:24
    اعمدة = اعمدة + [[]]
    # apl-source:25
    مربعات = مربعات + [[]]
  # apl-source:26
  for ص in range(9):
    # apl-source:27
    for ج in range(9):
      # apl-source:28
      ق = لوحة[ص][ج]
      # apl-source:29
      if ق != ".":
        # apl-source:30
        م = (ص // 3) * 3 + (ج // 3)
        # apl-source:31
        if ق in صفوف[ص]:
          # apl-source:32
          return False
        # apl-source:33
        if ق in اعمدة[ج]:
          # apl-source:34
          return False
        # apl-source:35
        if ق in مربعات[م]:
          # apl-source:36
          return False
        # apl-source:37
        صفوف[ص] = صفوف[ص] + [ق]
        # apl-source:38
        اعمدة[ج] = اعمدة[ج] + [ق]
        # apl-source:39
        مربعات[م] = مربعات[م] + [ق]
  # apl-source:40
  return True
# apl-source:41

# apl-source:42
فارغ = []
# apl-source:43
for ع in range(9):
  # apl-source:44
  فارغ = فارغ + [["."] * 9]
# apl-source:45
تأكد_يساوي(صالحة(فارغ), True, "فارغة")
# apl-source:46
فارغ[0][0] = "5"
# apl-source:47
فارغ[0][5] = "5"
# apl-source:48
تأكد_يساوي(صالحة(فارغ), False, "تكرار في صف")
# apl-source:49
فارغ[0][5] = "."
# apl-source:50
فارغ[7][0] = "5"
# apl-source:51
تأكد_يساوي(صالحة(فارغ), False, "تكرار في عمود")
# apl-source:52
فارغ[7][0] = "."
# apl-source:53
فارغ[1][1] = "5"
# apl-source:54
تأكد_يساوي(صالحة(فارغ), False, "تكرار في مربع")
# apl-source:55
