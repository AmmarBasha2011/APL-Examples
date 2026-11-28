
# apl-source:1
# مثال 1595 — عدد عقد الشجرة
# apl-source:2
# Count nodes in a binary tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1595-tree-node-count.apl
# apl-source:6

# apl-source:7
# الشجرة الفارغة لا عقد فيها
# apl-source:8
# العدد = 1 + عقد اليسار + عقد اليمين
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
def عدد_العقد(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return 0
  # apl-source:21
  return 1 + عدد_العقد(ش[1]) + عدد_العقد(ش[2])
# apl-source:22

# apl-source:23
تأكد_يساوي(عدد_العقد([]), 0, "فارغة")
# apl-source:24
تأكد_يساوي(عدد_العقد([1, [2, [], []], [3, [4, [], []], []]]), 4, "أربع عقد")
# apl-source:25
