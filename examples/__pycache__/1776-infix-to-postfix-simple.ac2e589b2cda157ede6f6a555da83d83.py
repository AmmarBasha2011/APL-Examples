
# apl-source:1
# مثال 1776 — من الصيغة العادية إلى اللاحقة
# apl-source:2
# Infix to postfix conversion
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1776-infix-to-postfix-simple.apl
# apl-source:6

# apl-source:7
# الضرب والقسمة أعلى أولوية
# apl-source:8
# نفرغ المكدس في النهاية
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
def أولوية(ع):
  # apl-source:19
  if ع == "*" or ع == "/":
    # apl-source:20
    return 2
  # apl-source:21
  return 1
# apl-source:22

# apl-source:23
def للاحقة(رموز):
  # apl-source:24
  خرج = []
  # apl-source:25
  مكدس = []
  # apl-source:26
  for ر in رموز:
    # apl-source:27
    if ر.isdigit():
      # apl-source:28
      خرج.append(ر)
    # apl-source:29
    else:
      # apl-source:30
      while len(مكدس) > 0 and أولوية(مكدس[len(مكدس) - 1]) >= أولوية(ر):
        # apl-source:31
        خرج.append(مكدس.pop())
      # apl-source:32
      مكدس.append(ر)
  # apl-source:33
  while len(مكدس) > 0:
    # apl-source:34
    خرج.append(مكدس.pop())
  # apl-source:35
  return خرج
# apl-source:36

# apl-source:37
تأكد_يساوي(للاحقة(["1", "+", "2", "*", "3"]), ["1", "2", "3", "*", "+"], "أولوية")
# apl-source:38
تأكد_يساوي(للاحقة(["1", "*", "2", "+", "3"]), ["1", "2", "*", "3", "+"], "عكس")
# apl-source:39
تأكد_يساوي(للاحقة(["4"]), ["4"], "عدد")
# apl-source:40
