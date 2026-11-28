
# apl-source:1
# مثال 1605 — أقل عمق في شجرة
# apl-source:2
# Minimum depth of a binary tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1605-tree-minimum-depth.apl
# apl-source:6

# apl-source:7
# العقدة بابن واحد تتبع ذلك الابن
# apl-source:8
# وإلا نأخذ الأقل من الفرعين
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
def أقل_عمق(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return 0
  # apl-source:21
  if ش[1] == []:
    # apl-source:22
    return 1 + أقل_عمق(ش[2])
  # apl-source:23
  if ش[2] == []:
    # apl-source:24
    return 1 + أقل_عمق(ش[1])
  # apl-source:25
  return 1 + min(أقل_عمق(ش[1]), أقل_عمق(ش[2]))
# apl-source:26

# apl-source:27
تأكد_يساوي(أقل_عمق([]), 0, "فارغة")
# apl-source:28
تأكد_يساوي(أقل_عمق([3, [9, [], []], [20, [15, [], []], [7, [], []]]]), 2, "ورقة قريبة")
# apl-source:29
تأكد_يساوي(أقل_عمق([1, [2, [3, [], []], []], []]), 3, "سلسلة")
# apl-source:30
