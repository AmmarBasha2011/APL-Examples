
# apl-source:1
# مثال 1216 — التحقق من شجرة بحث
# apl-source:2
# Validate binary search tree
# apl-source:3
# Demonstrates: حدود
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1216-bst-validate.apl
# apl-source:6

# apl-source:7
# نمرر لكل عقدة حداً أدنى وأقصى
# apl-source:8
# والقيمة يجب أن تقع بينهما
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
def صحيحة(ش, ادنى, اقصى):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return True
  # apl-source:21
  if (ش[0] <= ادنى) or (ش[0] >= اقصى):
    # apl-source:22
    return False
  # apl-source:23
  ي = صحيحة(ش[1], ادنى, ش[0])
  # apl-source:24
  if not ي:
    # apl-source:25
    return False
  # apl-source:26
  return صحيحة(ش[2], ش[0], اقصى)
# apl-source:27

# apl-source:28
كبير = 1000000000
# apl-source:29
تأكد_يساوي(صحيحة([2, [1, [], []], [3, [], []]], -كبير, كبير), True, "صحيحة")
# apl-source:30
تأكد_يساوي(صحيحة([5, [1, [], []], [4, [3, [], []], [6, [], []]]], -كبير, كبير), False, "فرع خاطئ")
# apl-source:31
تأكد_يساوي(صحيحة([5, [4, [], [6, [], []]], []], -كبير, كبير), False, "حفيد خاطئ")
# apl-source:32
تأكد_يساوي(صحيحة([], -كبير, كبير), True, "فارغة")
# apl-source:33
