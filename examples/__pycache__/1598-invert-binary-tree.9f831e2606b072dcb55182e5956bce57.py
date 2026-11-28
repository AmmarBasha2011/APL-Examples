
# apl-source:1
# مثال 1598 — قلب شجرة ثنائية
# apl-source:2
# Invert a binary tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1598-invert-binary-tree.apl
# apl-source:6

# apl-source:7
# نقلب الفرعين أولاً
# apl-source:8
# ثم نبدل موضعيهما
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
def اقلب_الشجرة(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return []
  # apl-source:21
  return [ش[0], اقلب_الشجرة(ش[2]), اقلب_الشجرة(ش[1])]
# apl-source:22

# apl-source:23
تأكد_يساوي(اقلب_الشجرة([]), [], "فارغة")
# apl-source:24
تأكد_يساوي(اقلب_الشجرة([1, [2, [], []], [3, [], []]]), [1, [3, [], []], [2, [], []]], "عقدتان")
# apl-source:25
تأكد_يساوي(اقلب_الشجرة(اقلب_الشجرة([1, [2, [], []], []])), [1, [2, [], []], []], "مرتان")
# apl-source:26
