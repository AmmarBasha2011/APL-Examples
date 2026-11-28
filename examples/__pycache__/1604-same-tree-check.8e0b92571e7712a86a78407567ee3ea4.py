
# apl-source:1
# مثال 1604 — هل الشجرتان متطابقتان
# apl-source:2
# Same tree check
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1604-same-tree-check.apl
# apl-source:6

# apl-source:7
# الفارغتان متطابقتان
# apl-source:8
# نقارن الجذر ثم الفرعين
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
def متطابقتان(أ, ب):
  # apl-source:19
  if أ == [] and ب == []:
    # apl-source:20
    return True
  # apl-source:21
  if أ == [] or ب == []:
    # apl-source:22
    return False
  # apl-source:23
  if أ[0] != ب[0]:
    # apl-source:24
    return False
  # apl-source:25
  return متطابقتان(أ[1], ب[1]) and متطابقتان(أ[2], ب[2])
# apl-source:26

# apl-source:27
تأكد_يساوي(متطابقتان([1, [2, [], []], []], [1, [2, [], []], []]), True, "متطابقتان")
# apl-source:28
تأكد_يساوي(متطابقتان([1, [2, [], []], []], [1, [], [2, [], []]]), False, "شكل مختلف")
# apl-source:29
تأكد_يساوي(متطابقتان([], []), True, "فارغتان")
# apl-source:30
