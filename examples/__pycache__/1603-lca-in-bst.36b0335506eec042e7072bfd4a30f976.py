
# apl-source:1
# مثال 1603 — أقرب جد مشترك في شجرة بحث
# apl-source:2
# Lowest common ancestor in a BST
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1603-lca-in-bst.apl
# apl-source:6

# apl-source:7
# إن كانت القيمتان أصغر من العقدة نذهب يساراً
# apl-source:8
# وإن كانتا أكبر نذهب يميناً وإلا فهذه العقدة
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
def أقرب_جد(ش, أ, ب):
  # apl-source:19
  if أ < ش[0] and ب < ش[0]:
    # apl-source:20
    return أقرب_جد(ش[1], أ, ب)
  # apl-source:21
  if أ > ش[0] and ب > ش[0]:
    # apl-source:22
    return أقرب_جد(ش[2], أ, ب)
  # apl-source:23
  return ش[0]
# apl-source:24

# apl-source:25
شجرة = [6, [2, [0, [], []], [4, [3, [], []], [5, [], []]]], [8, [7, [], []], [9, [], []]]]
# apl-source:26
تأكد_يساوي(أقرب_جد(شجرة, 2, 8), 6, "الجذر")
# apl-source:27
تأكد_يساوي(أقرب_جد(شجرة, 2, 4), 2, "أحدهما الجد")
# apl-source:28
تأكد_يساوي(أقرب_جد(شجرة, 3, 5), 4, "عقدة وسطى")
# apl-source:29
