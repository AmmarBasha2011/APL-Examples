
# apl-source:1
# مثال 1602 — العنصر الأصغر رقم ك في شجرة بحث
# apl-source:2
# Kth smallest element in BST
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1602-kth-smallest-in-bst.apl
# apl-source:6

# apl-source:7
# نجمع القيم بالترتيب المتوسط
# apl-source:8
# العنصر ك هو الموضع ك ناقص واحد
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
def بالترتيب(ش, نتيجة):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return نتيجة
  # apl-source:21
  بالترتيب(ش[1], نتيجة)
  # apl-source:22
  نتيجة.append(ش[0])
  # apl-source:23
  بالترتيب(ش[2], نتيجة)
  # apl-source:24
  return نتيجة
# apl-source:25

# apl-source:26
def الأصغر_ك(ش, ك):
  # apl-source:27
  ق = بالترتيب(ش, [])
  # apl-source:28
  return ق[ك - 1]
# apl-source:29

# apl-source:30
شجرة = [5, [3, [2, [], []], [4, [], []]], [6, [], []]]
# apl-source:31
تأكد_يساوي(الأصغر_ك(شجرة, 1), 2, "الأول")
# apl-source:32
تأكد_يساوي(الأصغر_ك(شجرة, 3), 4, "الثالث")
# apl-source:33
تأكد_يساوي(الأصغر_ك(شجرة, 5), 6, "الأخير")
# apl-source:34
