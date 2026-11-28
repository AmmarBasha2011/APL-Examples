
# apl-source:1
# مثال 1377 — مكدس بأقصى قيمة
# apl-source:2
# Max stack operations
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1377-max-stack-ops.apl
# apl-source:6

# apl-source:7
# حذف الأقصى يزيل أقرب موضع من القمة فيه الأقصى
# apl-source:8
# نبحث من النهاية
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
def نفذ_العمليات(عمليات):
  # apl-source:19
  مكدس = []
  # apl-source:20
  ناتج = []
  # apl-source:21
  for عملية in عمليات:
    # apl-source:22
    اسم = عملية[0]
    # apl-source:23
    if اسم == "push":
      # apl-source:24
      مكدس = مكدس + [عملية[1]]
    # apl-source:25
    elif اسم == "top":
      # apl-source:26
      ناتج = ناتج + [مكدس[len(مكدس) - 1]]
    # apl-source:27
    elif اسم == "pop":
      # apl-source:28
      ناتج = ناتج + [مكدس.pop()]
    # apl-source:29
    elif اسم == "peekMax":
      # apl-source:30
      ناتج = ناتج + [max(مكدس)]
    # apl-source:31
    elif اسم == "popMax":
      # apl-source:32
      اكبر_قيمة = max(مكدس)
      # apl-source:33
      موضع = len(مكدس) - 1
      # apl-source:34
      while مكدس[موضع] != اكبر_قيمة:
        # apl-source:35
        موضع = موضع - 1
      # apl-source:36
      ناتج = ناتج + [مكدس.pop(موضع)]
  # apl-source:37
  return ناتج
# apl-source:38

# apl-source:39
ع = [["push",5],["push",1],["push",5],["top"],["popMax"],["top"],["peekMax"],["pop"],["top"]]
# apl-source:40
تأكد_يساوي(نفذ_العمليات(ع), [5,5,1,5,1,5], "مثال أول")
# apl-source:41
تأكد_يساوي(نفذ_العمليات([["push",2],["push",9],["popMax"],["top"]]), [9,2], "حذف الأقصى")
# apl-source:42
تأكد_يساوي(نفذ_العمليات([["push",4],["peekMax"]]), [4], "قمة واحدة")
# apl-source:43
