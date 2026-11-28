
# apl-source:1
# مثال 1266 — فائز إكس أو
# apl-source:2
# Tic tac toe winner detection
# apl-source:3
# Demonstrates: فحص خطوط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1266-tic-tac-toe-winner.apl
# apl-source:6

# apl-source:7
# نفحص الصفوف والأعمدة والقطرين
# apl-source:8
# اللوحة المكتملة بلا فائز تعادل
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
  خطوط = []
  # apl-source:20
  for ص in range(3):
    # apl-source:21
    خطوط = خطوط + [[ل[ص][0], ل[ص][1], ل[ص][2]]]
    # apl-source:22
    خطوط = خطوط + [[ل[0][ص], ل[1][ص], ل[2][ص]]]
  # apl-source:23
  خطوط = خطوط + [[ل[0][0], ل[1][1], ل[2][2]]]
  # apl-source:24
  خطوط = خطوط + [[ل[0][2], ل[1][1], ل[2][0]]]
  # apl-source:25
  for خ in خطوط:
    # apl-source:26
    if (خ[0] != " ") and (خ[0] == خ[1]) and (خ[1] == خ[2]):
      # apl-source:27
      return خ[0]
  # apl-source:28
  for صف in ل:
    # apl-source:29
    if " " in صف:
      # apl-source:30
      return "جارية"
  # apl-source:31
  return "تعادل"
# apl-source:32

# apl-source:33
تأكد_يساوي(فائز([["X","X","X"],["O","O"," "],[" "," "," "]]), "X", "صف")
# apl-source:34
تأكد_يساوي(فائز([["O","X"," "],["O","X"," "],["O"," ","X"]]), "O", "عمود")
# apl-source:35
تأكد_يساوي(فائز([["X","O"," "],["O","X"," "],[" "," ","X"]]), "X", "قطر")
# apl-source:36
تأكد_يساوي(فائز([["X","O","X"],["X","O","O"],["O","X","X"]]), "تعادل", "تعادل")
# apl-source:37
تأكد_يساوي(فائز([["X"," "," "],[" "," "," "],[" "," "," "]]), "جارية", "جارية")
# apl-source:38
