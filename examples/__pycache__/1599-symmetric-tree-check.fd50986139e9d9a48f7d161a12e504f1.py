
# apl-source:1
# مثال 1599 — هل الشجرة متناظرة
# apl-source:2
# Symmetric tree check
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1599-symmetric-tree-check.apl
# apl-source:6

# apl-source:7
# نقارن الفرع الأيسر بمرآة الأيمن
# apl-source:8
# القيم متساوية والأبناء متقابلون
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
def متقابلان(أ, ب):
  # apl-source:19
  if أ == [] and ب == []:
    # apl-source:20
    return True
  # apl-source:21
  if أ == [] or ب == []:
    # apl-source:22
    return False
  # apl-source:23
  if أ[0] != ب[0]:
    # apl-source:24
    return False
  # apl-source:25
  return متقابلان(أ[1], ب[2]) and متقابلان(أ[2], ب[1])
# apl-source:26

# apl-source:27
def متناظرة(ش):
  # apl-source:28
  if ش == []:
    # apl-source:29
    return True
  # apl-source:30
  return متقابلان(ش[1], ش[2])
# apl-source:31

# apl-source:32
تأكد_يساوي(متناظرة([1, [2, [], []], [2, [], []]]), True, "متناظرة")
# apl-source:33
تأكد_يساوي(متناظرة([1, [2, [3, [], []], []], [2, [], []]]), False, "غير متناظرة")
# apl-source:34
تأكد_يساوي(متناظرة([]), True, "فارغة")
# apl-source:35
