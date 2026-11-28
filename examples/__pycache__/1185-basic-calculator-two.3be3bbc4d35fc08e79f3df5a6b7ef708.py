
# apl-source:1
# مثال 1185 — حاسبة بأولويات
# apl-source:2
# Basic calculator with precedence
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1185-basic-calculator-two.apl
# apl-source:6

# apl-source:7
# الضرب والقسمة يُنفذان فوراً
# apl-source:8
# والجمع والطرح يدخلان المكدس بعلامتهما
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
def احسب_اولويات(س):
  # apl-source:19
  س = س.replace(" ", "")
  # apl-source:20
  مكدس = []
  # apl-source:21
  رقم = 0
  # apl-source:22
  عملية = "+"
  # apl-source:23
  for ع in range(len(س)):
    # apl-source:24
    ح = س[ع]
    # apl-source:25
    if ح.isdigit():
      # apl-source:26
      رقم = رقم * 10 + int(ح)
    # apl-source:27
    if (ح in "+-*/") or (ع == len(س) - 1):
      # apl-source:28
      if ح != " ":
        # apl-source:29
        if عملية == "+":
          # apl-source:30
          مكدس = مكدس + [رقم]
        # apl-source:31
        elif عملية == "-":
          # apl-source:32
          مكدس = مكدس + [-رقم]
        # apl-source:33
        elif عملية == "*":
          # apl-source:34
          مكدس = مكدس + [مكدس.pop() * رقم]
        # apl-source:35
        else:
          # apl-source:36
          ق = مكدس.pop()
          # apl-source:37
          if ق < 0:
            # apl-source:38
            مكدس = مكدس + [-((-ق) // رقم)]
          # apl-source:39
          else:
            # apl-source:40
            مكدس = مكدس + [ق // رقم]
        # apl-source:41
        عملية = ح
        # apl-source:42
        رقم = 0
  # apl-source:43
  مج = 0
  # apl-source:44
  for ق in مكدس:
    # apl-source:45
    مج = مج + ق
  # apl-source:46
  return مج
# apl-source:47

# apl-source:48
تأكد_يساوي(احسب_اولويات("3+2*2"), 7, "ضرب أولاً")
# apl-source:49
تأكد_يساوي(احسب_اولويات(" 3/2 "), 1, "قسمة")
# apl-source:50
تأكد_يساوي(احسب_اولويات(" 3+5 / 2 "), 5, "مختلط")
# apl-source:51
تأكد_يساوي(احسب_اولويات("14-3/2"), 13, "طرح وقسمة")
# apl-source:52
