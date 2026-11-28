
# apl-source:1
# مثال 1027 — أطول أقواس صحيحة
# apl-source:2
# Longest valid parentheses
# apl-source:3
# Demonstrates: مكدس فهارس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1027-longest-valid-parens.apl
# apl-source:6

# apl-source:7
# نخزن في المكدس فهرس آخر موضع لا يصلح
# apl-source:8
# كل إغلاق مطابق يعطي طولاً من القمة الجديدة
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
def اطول_صحيح(نص_):
  # apl-source:19
  مكدس = [-1]
  # apl-source:20
  افضل = 0
  # apl-source:21
  for ع in range(len(نص_)):
    # apl-source:22
    if نص_[ع] == "(":
      # apl-source:23
      مكدس = مكدس + [ع]
    # apl-source:24
    else:
      # apl-source:25
      مكدس.pop()
      # apl-source:26
      if len(مكدس) == 0:
        # apl-source:27
        مكدس = مكدس + [ع]
      # apl-source:28
      else:
        # apl-source:29
        ط = ع - مكدس[len(مكدس) - 1]
        # apl-source:30
        if ط > افضل:
          # apl-source:31
          افضل = ط
  # apl-source:32
  return افضل
# apl-source:33

# apl-source:34
تأكد_يساوي(اطول_صحيح("(()"), 2, "فتح زائد")
# apl-source:35
تأكد_يساوي(اطول_صحيح(")()())"), 4, "وسط")
# apl-source:36
تأكد_يساوي(اطول_صحيح(""), 0, "فارغ")
# apl-source:37
تأكد_يساوي(اطول_صحيح("()(())"), 6, "كله")
# apl-source:38
