
# apl-source:1
# مثال 1775 — تقييم التعبير اللاحق
# apl-source:2
# Evaluate postfix expression
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1775-postfix-expression-evaluate.apl
# apl-source:6

# apl-source:7
# نقسم التعبير بالمسافات
# apl-source:8
# نطبق العملية على آخر عددين
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
def قيّم(تعبير):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ر in تعبير.split(" "):
    # apl-source:21
    if ر.isdigit():
      # apl-source:22
      مكدس.append(int(ر))
    # apl-source:23
    else:
      # apl-source:24
      ب = مكدس.pop()
      # apl-source:25
      أ = مكدس.pop()
      # apl-source:26
      if ر == "+":
        # apl-source:27
        مكدس.append(أ + ب)
      # apl-source:28
      elif ر == "-":
        # apl-source:29
        مكدس.append(أ - ب)
      # apl-source:30
      elif ر == "*":
        # apl-source:31
        مكدس.append(أ * ب)
      # apl-source:32
      else:
        # apl-source:33
        مكدس.append(أ // ب)
  # apl-source:34
  return مكدس[0]
# apl-source:35

# apl-source:36
تأكد_يساوي(قيّم("2 3 +"), 5, "جمع")
# apl-source:37
تأكد_يساوي(قيّم("5 1 2 + 4 * + 3 -"), 14, "مركب")
# apl-source:38
تأكد_يساوي(قيّم("8 2 /"), 4, "قسمة")
# apl-source:39
