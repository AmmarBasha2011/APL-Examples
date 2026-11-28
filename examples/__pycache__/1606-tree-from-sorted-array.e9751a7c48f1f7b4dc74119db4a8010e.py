
# apl-source:1
# مثال 1606 — شجرة متوازنة من قائمة مرتبة
# apl-source:2
# Balanced BST from sorted array
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1606-tree-from-sorted-array.apl
# apl-source:6

# apl-source:7
# نختار العنصر الأوسط جذراً
# apl-source:8
# نبني الفرعين من النصفين
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
def ابنِ_الشجرة(أ):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return []
  # apl-source:21
  وسط = len(أ) // 2
  # apl-source:22
  return [أ[وسط], ابنِ_الشجرة(أ[0:وسط]), ابنِ_الشجرة(أ[وسط + 1:len(أ)])]
# apl-source:23

# apl-source:24
تأكد_يساوي(ابنِ_الشجرة([]), [], "فارغة")
# apl-source:25
تأكد_يساوي(ابنِ_الشجرة([1, 2, 3]), [2, [1, [], []], [3, [], []]], "ثلاثة")
# apl-source:26
تأكد_يساوي(ابنِ_الشجرة([1, 2]), [2, [1, [], []], []], "اثنان")
# apl-source:27
