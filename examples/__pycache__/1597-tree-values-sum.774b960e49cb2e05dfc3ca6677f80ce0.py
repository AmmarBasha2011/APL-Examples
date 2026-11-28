
# apl-source:1
# مثال 1597 — مجموع قيم الشجرة
# apl-source:2
# Sum of tree values
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1597-tree-values-sum.apl
# apl-source:6

# apl-source:7
# قيمة الجذر زائد مجموع الفرعين
# apl-source:8
# الفارغة صفر
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
def مجموع_الشجرة(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return 0
  # apl-source:21
  return ش[0] + مجموع_الشجرة(ش[1]) + مجموع_الشجرة(ش[2])
# apl-source:22

# apl-source:23
تأكد_يساوي(مجموع_الشجرة([]), 0, "فارغة")
# apl-source:24
تأكد_يساوي(مجموع_الشجرة([5, [3, [], []], [8, [], []]]), 16, "ثلاث عقد")
# apl-source:25
تأكد_يساوي(مجموع_الشجرة([1, [-1, [], []], []]), 0, "سالب")
# apl-source:26
