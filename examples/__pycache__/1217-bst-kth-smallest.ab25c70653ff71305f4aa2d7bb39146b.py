
# apl-source:1
# مثال 1217 — الأصغر ترتيب k في شجرة
# apl-source:2
# Kth smallest element in BST
# apl-source:3
# Demonstrates: قراءة متوسطة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1217-bst-kth-smallest.apl
# apl-source:6

# apl-source:7
# القراءة المتوسطة تعطي القيم مرتبة
# apl-source:8
# فنأخذ العنصر ذا الفهرس k ناقص واحد
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
def قيم_مرتبة(ش):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return []
  # apl-source:21
  return قيم_مرتبة(ش[1]) + [ش[0]] + قيم_مرتبة(ش[2])
# apl-source:22

# apl-source:23
def الترتيب_ك(ش, ك):
  # apl-source:24
  return قيم_مرتبة(ش)[ك - 1]
# apl-source:25

# apl-source:26
شجرة = [5, [3, [2, [1, [], []], []], [4, [], []]], [6, [], []]]
# apl-source:27
تأكد_يساوي(الترتيب_ك(شجرة, 1), 1, "الأول")
# apl-source:28
تأكد_يساوي(الترتيب_ك(شجرة, 3), 3, "الثالث")
# apl-source:29
تأكد_يساوي(الترتيب_ك(شجرة, 6), 6, "الأخير")
# apl-source:30
