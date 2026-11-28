
# apl-source:1
# مثال 1209 — أقرب سلف مشترك
# apl-source:2
# Lowest common ancestor in BST
# apl-source:3
# Demonstrates: شجرة بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1209-tree-lca.apl
# apl-source:6

# apl-source:7
# لو كان العقدتان أصغر من الجذر نذهب يساراً
# apl-source:8
# ولو أكبر نذهب يميناً وإلا فالجذر هو الجواب
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
def سلف(ش, أ, ب):
  # apl-source:19
  while len(ش) > 0:
    # apl-source:20
    if (أ < ش[0]) and (ب < ش[0]):
      # apl-source:21
      ش = ش[1]
    # apl-source:22
    elif (أ > ش[0]) and (ب > ش[0]):
      # apl-source:23
      ش = ش[2]
    # apl-source:24
    else:
      # apl-source:25
      return ش[0]
  # apl-source:26
  return -1
# apl-source:27

# apl-source:28
شجرة = [6, [2, [0, [], []], [4, [3, [], []], [5, [], []]]], [8, [7, [], []], [9, [], []]]]
# apl-source:29
تأكد_يساوي(سلف(شجرة, 2, 8), 6, "عبر الجذر")
# apl-source:30
تأكد_يساوي(سلف(شجرة, 2, 4), 2, "العقدة نفسها")
# apl-source:31
تأكد_يساوي(سلف(شجرة, 3, 5), 4, "داخل اليسار")
# apl-source:32
تأكد_يساوي(سلف(شجرة, 7, 9), 8, "داخل اليمين")
# apl-source:33
