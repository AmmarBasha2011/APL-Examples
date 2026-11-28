
# apl-source:1
# مثال 1596 — عدد أوراق الشجرة
# apl-source:2
# Count leaves in a binary tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1596-tree-leaf-count.apl
# apl-source:6

# apl-source:7
# الورقة فرعاها فارغان
# apl-source:8
# نجمع أوراق الفرعين
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
def عدد_الأوراق(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return 0
  # apl-source:21
  if ش[1] == [] and ش[2] == []:
    # apl-source:22
    return 1
  # apl-source:23
  return عدد_الأوراق(ش[1]) + عدد_الأوراق(ش[2])
# apl-source:24

# apl-source:25
تأكد_يساوي(عدد_الأوراق([]), 0, "فارغة")
# apl-source:26
تأكد_يساوي(عدد_الأوراق([1, [], []]), 1, "جذر فقط")
# apl-source:27
تأكد_يساوي(عدد_الأوراق([1, [2, [4, [], []], []], [3, [], []]]), 2, "ورقتان")
# apl-source:28
