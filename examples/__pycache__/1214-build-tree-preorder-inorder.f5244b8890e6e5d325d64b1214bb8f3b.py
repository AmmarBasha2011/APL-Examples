
# apl-source:1
# مثال 1214 — بناء من مسارين
# apl-source:2
# Build tree from preorder and inorder
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1214-build-tree-preorder-inorder.apl
# apl-source:6

# apl-source:7
# أول عنصر في القراءة المسبقة هو الجذر
# apl-source:8
# وموضعه في المتوسطة يفصل الفرعين
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
def ابن(مسبق, متوسط):
  # apl-source:19
  if len(مسبق) == 0:
    # apl-source:20
    return []
  # apl-source:21
  جذر = مسبق[0]
  # apl-source:22
  م = متوسط.index(جذر)
  # apl-source:23
  return [جذر, ابن(مسبق[1:م + 1], متوسط[:م]), ابن(مسبق[م + 1:], متوسط[م + 1:])]
# apl-source:24

# apl-source:25
ش = ابن([3,9,20,15,7], [9,3,15,20,7])
# apl-source:26
تأكد_يساوي(ش, [3, [9, [], []], [20, [15, [], []], [7, [], []]]], "مثال أول")
# apl-source:27
تأكد_يساوي(ابن([1], [1]), [1, [], []], "عقدة")
# apl-source:28
تأكد_يساوي(ابن([], []), [], "فارغة")
# apl-source:29
