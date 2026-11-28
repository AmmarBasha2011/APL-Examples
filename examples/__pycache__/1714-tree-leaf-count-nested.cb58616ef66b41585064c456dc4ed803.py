
# apl-source:1
# مثال 1714 — عدد أوراق الشجرة المتداخلة
# apl-source:2
# Leaf count of nested list tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1714-tree-leaf-count-nested.apl
# apl-source:6

# apl-source:7
# نتعمق في كل قائمة
# apl-source:8
# الرقم يعد ورقة
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
def عد_الأوراق(ش):
  # apl-source:19
  if type(ش) != type([]):
    # apl-source:20
    return 1
  # apl-source:21
  مجموع = 0
  # apl-source:22
  for ع in ش:
    # apl-source:23
    مجموع = مجموع + عد_الأوراق(ع)
  # apl-source:24
  return مجموع
# apl-source:25

# apl-source:26
تأكد_يساوي(عد_الأوراق([1, [2, 3], [[4], 5]]), 5, "خمس")
# apl-source:27
تأكد_يساوي(عد_الأوراق([]), 0, "فارغة")
# apl-source:28
تأكد_يساوي(عد_الأوراق(7), 1, "ورقة")
# apl-source:29
