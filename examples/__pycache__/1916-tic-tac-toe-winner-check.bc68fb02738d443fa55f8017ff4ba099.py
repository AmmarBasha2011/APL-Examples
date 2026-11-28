
# apl-source:1
# مثال 1916 — فحص فائز لعبة إكس أو
# apl-source:2
# Tic tac toe winner check
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1916-tic-tac-toe-winner-check.apl
# apl-source:6

# apl-source:7
# ثمانية خطوط ممكنة للفوز
# apl-source:8
# نبحث عن خط من رمز واحد
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
def فائز(ل):
  # apl-source:19
  خطوط = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  # apl-source:20
  for خ in خطوط:
    # apl-source:21
    if ل[خ[0]] != "." and ل[خ[0]] == ل[خ[1]] and ل[خ[1]] == ل[خ[2]]:
      # apl-source:22
      return ل[خ[0]]
  # apl-source:23
  return "-"
# apl-source:24

# apl-source:25
تأكد_يساوي(فائز("XXXOO...."), "X", "صف")
# apl-source:26
تأكد_يساوي(فائز("OXXXOO.OX"), "-", "لا فائز")
# apl-source:27
تأكد_يساوي(فائز("XO.XO.X.."), "X", "عمود")
# apl-source:28
تأكد_يساوي(فائز("O.X.OX..O"), "O", "قطر")
# apl-source:29
