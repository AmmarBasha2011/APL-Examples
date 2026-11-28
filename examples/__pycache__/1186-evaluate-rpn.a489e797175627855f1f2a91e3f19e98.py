
# apl-source:1
# مثال 1186 — تقييم الصيغة العكسية
# apl-source:2
# Evaluate reverse polish notation
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1186-evaluate-rpn.apl
# apl-source:6

# apl-source:7
# الأرقام تدخل المكدس
# apl-source:8
# والعملية تأخذ آخر رقمين وتدفع الناتج
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
def قيّم(رموز):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ر in رموز:
    # apl-source:21
    if ر in ["+", "-", "*", "/"]:
      # apl-source:22
      ب = مكدس.pop()
      # apl-source:23
      أ = مكدس.pop()
      # apl-source:24
      if ر == "+":
        # apl-source:25
        مكدس = مكدس + [أ + ب]
      # apl-source:26
      elif ر == "-":
        # apl-source:27
        مكدس = مكدس + [أ - ب]
      # apl-source:28
      elif ر == "*":
        # apl-source:29
        مكدس = مكدس + [أ * ب]
      # apl-source:30
      else:
        # apl-source:31
        مكدس = مكدس + [int(أ / ب)]
    # apl-source:32
    else:
      # apl-source:33
      مكدس = مكدس + [int(ر)]
  # apl-source:34
  return مكدس[0]
# apl-source:35

# apl-source:36
تأكد_يساوي(قيّم(["2","1","+","3","*"]), 9, "مثال أول")
# apl-source:37
تأكد_يساوي(قيّم(["4","13","5","/","+"]), 6, "قسمة")
# apl-source:38
تأكد_يساوي(قيّم(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22, "طويل")
# apl-source:39
تأكد_يساوي(قيّم(["7"]), 7, "رقم واحد")
# apl-source:40
