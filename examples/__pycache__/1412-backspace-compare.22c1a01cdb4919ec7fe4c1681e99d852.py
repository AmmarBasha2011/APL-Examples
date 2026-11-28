
# apl-source:1
# مثال 1412 — مقارنة مع المسح
# apl-source:2
# Backspace string compare
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1412-backspace-compare.apl
# apl-source:6

# apl-source:7
# نبني كل نص بمكدس
# apl-source:8
# العلامة تخرج آخر حرف إن وجد
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
def ابن(نص_):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح == "#":
      # apl-source:22
      if len(مكدس) > 0:
        # apl-source:23
        مكدس.pop()
    # apl-source:24
    else:
      # apl-source:25
      مكدس = مكدس + [ح]
  # apl-source:26
  return مكدس
# apl-source:27

# apl-source:28
def متساويان_بعد_المسح(أ, ب):
  # apl-source:29
  return ابن(أ) == ابن(ب)
# apl-source:30

# apl-source:31
تأكد_يساوي(متساويان_بعد_المسح("ab#c", "ad#c"), True, "ac")
# apl-source:32
تأكد_يساوي(متساويان_بعد_المسح("ab##", "c#d#"), True, "فارغان")
# apl-source:33
تأكد_يساوي(متساويان_بعد_المسح("a#c", "b"), False, "مختلفان")
# apl-source:34
