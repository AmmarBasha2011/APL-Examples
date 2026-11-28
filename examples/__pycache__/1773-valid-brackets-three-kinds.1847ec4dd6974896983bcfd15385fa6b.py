
# apl-source:1
# مثال 1773 — أقواس صحيحة بثلاثة أنواع
# apl-source:2
# Valid brackets of three kinds
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1773-valid-brackets-three-kinds.apl
# apl-source:6

# apl-source:7
# نكدس الفاتح
# apl-source:8
# ونقارن عند الإغلاق
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
def صحيحة(س):
  # apl-source:19
  أزواج = {")": "(", "]": "[", "}": "{"}
  # apl-source:20
  مكدس = []
  # apl-source:21
  for ح in س:
    # apl-source:22
    if ح in "([{":
      # apl-source:23
      مكدس.append(ح)
    # apl-source:24
    elif ح in ")]}":
      # apl-source:25
      if len(مكدس) == 0:
        # apl-source:26
        return False
      # apl-source:27
      if مكدس.pop() != أزواج[ح]:
        # apl-source:28
        return False
  # apl-source:29
  return len(مكدس) == 0
# apl-source:30

# apl-source:31
تأكد_يساوي(صحيحة("([]{})"), True, "متداخلة")
# apl-source:32
تأكد_يساوي(صحيحة("(]"), False, "متعارضة")
# apl-source:33
تأكد_يساوي(صحيحة("(("), False, "ناقصة")
# apl-source:34
تأكد_يساوي(صحيحة(""), True, "فارغة")
# apl-source:35
