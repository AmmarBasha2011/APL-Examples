
# apl-source:1
# مثال 1429 — أقصى عمق للأقواس
# apl-source:2
# Maximum nesting depth of parentheses
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1429-max-nesting-depth.apl
# apl-source:6

# apl-source:7
# نزيد العداد عند القوس المفتوح
# apl-source:8
# ونسجل أكبر قيمة وصل إليها
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
def اقصى_عمق(تعبير):
  # apl-source:19
  عمق = 0
  # apl-source:20
  اقصى = 0
  # apl-source:21
  for ح in تعبير:
    # apl-source:22
    if ح == "(":
      # apl-source:23
      عمق = عمق + 1
      # apl-source:24
      if عمق > اقصى:
        # apl-source:25
        اقصى = عمق
    # apl-source:26
    elif ح == ")":
      # apl-source:27
      عمق = عمق - 1
  # apl-source:28
  return اقصى
# apl-source:29

# apl-source:30
تأكد_يساوي(اقصى_عمق("(1+(2*3)+((8)/4))+1"), 3, "ثلاثة")
# apl-source:31
تأكد_يساوي(اقصى_عمق("(1)+((2))+(((3)))"), 3, "ثلاثة ثانية")
# apl-source:32
تأكد_يساوي(اقصى_عمق("1"), 0, "بلا أقواس")
# apl-source:33
