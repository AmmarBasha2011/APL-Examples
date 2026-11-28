
# apl-source:1
# مثال 1218 — إدراج وحذف شجرة بحث
# apl-source:2
# BST insert and delete
# apl-source:3
# Demonstrates: شجرة بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1218-bst-insert-delete.apl
# apl-source:6

# apl-source:7
# الحذف لعقدة بابنين يستبدلها بأصغر قيمة في الفرع الأيمن
# apl-source:8
# ونعيد بناء الفروع بدوال ذاتية
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
def ادرج(ش, ق):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return [ق, [], []]
  # apl-source:21
  if ق < ش[0]:
    # apl-source:22
    return [ش[0], ادرج(ش[1], ق), ش[2]]
  # apl-source:23
  if ق > ش[0]:
    # apl-source:24
    return [ش[0], ش[1], ادرج(ش[2], ق)]
  # apl-source:25
  return ش
# apl-source:26

# apl-source:27
def اصغر_قيمة(ش):
  # apl-source:28
  while len(ش[1]) > 0:
    # apl-source:29
    ش = ش[1]
  # apl-source:30
  return ش[0]
# apl-source:31

# apl-source:32
def احذف_قيمة(ش, ق):
  # apl-source:33
  if len(ش) == 0:
    # apl-source:34
    return []
  # apl-source:35
  if ق < ش[0]:
    # apl-source:36
    return [ش[0], احذف_قيمة(ش[1], ق), ش[2]]
  # apl-source:37
  if ق > ش[0]:
    # apl-source:38
    return [ش[0], ش[1], احذف_قيمة(ش[2], ق)]
  # apl-source:39
  if len(ش[1]) == 0:
    # apl-source:40
    return ش[2]
  # apl-source:41
  if len(ش[2]) == 0:
    # apl-source:42
    return ش[1]
  # apl-source:43
  خلف = اصغر_قيمة(ش[2])
  # apl-source:44
  return [خلف, ش[1], احذف_قيمة(ش[2], خلف)]
# apl-source:45

# apl-source:46
def قراءة(ش):
  # apl-source:47
  if len(ش) == 0:
    # apl-source:48
    return []
  # apl-source:49
  return قراءة(ش[1]) + [ش[0]] + قراءة(ش[2])
# apl-source:50

# apl-source:51
ش = []
# apl-source:52
for ق in [5, 3, 7, 2, 4, 6, 8]:
  # apl-source:53
  ش = ادرج(ش, ق)
# apl-source:54
تأكد_يساوي(قراءة(ش), [2, 3, 4, 5, 6, 7, 8], "بعد الإدراج")
# apl-source:55
ش = احذف_قيمة(ش, 3)
# apl-source:56
تأكد_يساوي(قراءة(ش), [2, 4, 5, 6, 7, 8], "حذف ببن")
# apl-source:57
ش = احذف_قيمة(ش, 5)
# apl-source:58
تأكد_يساوي(قراءة(ش), [2, 4, 6, 7, 8], "حذف الجذر")
# apl-source:59
ش = احذف_قيمة(ش, 100)
# apl-source:60
تأكد_يساوي(قراءة(ش), [2, 4, 6, 7, 8], "غير موجود")
# apl-source:61
