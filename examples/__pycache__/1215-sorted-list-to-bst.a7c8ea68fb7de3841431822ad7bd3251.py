
# apl-source:1
# مثال 1215 — قائمة مرتبة إلى شجرة
# apl-source:2
# Sorted list to balanced BST
# apl-source:3
# Demonstrates: تقسيم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1215-sorted-list-to-bst.apl
# apl-source:6

# apl-source:7
# العنصر الأوسط هو الجذر
# apl-source:8
# والنصفان يصبحان الفرعين
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
def ابن_شجرة(أ):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return []
  # apl-source:21
  م = len(أ) // 2
  # apl-source:22
  return [أ[م], ابن_شجرة(أ[:م]), ابن_شجرة(أ[م + 1:])]
# apl-source:23

# apl-source:24
def متوسط_قراءة(ش):
  # apl-source:25
  if len(ش) == 0:
    # apl-source:26
    return []
  # apl-source:27
  return متوسط_قراءة(ش[1]) + [ش[0]] + متوسط_قراءة(ش[2])
# apl-source:28

# apl-source:29
def عمق(ش):
  # apl-source:30
  if len(ش) == 0:
    # apl-source:31
    return 0
  # apl-source:32
  return 1 + max(عمق(ش[1]), عمق(ش[2]))
# apl-source:33

# apl-source:34
ق = [-10, -3, 0, 5, 9]
# apl-source:35
ش = ابن_شجرة(ق)
# apl-source:36
تأكد_يساوي(ش[0], 0, "الجذر")
# apl-source:37
تأكد_يساوي(متوسط_قراءة(ش), ق, "مرتبة")
# apl-source:38
تأكد_يساوي(عمق(ش), 3, "متوازنة")
# apl-source:39
تأكد_يساوي(ابن_شجرة([]), [], "فارغة")
# apl-source:40
