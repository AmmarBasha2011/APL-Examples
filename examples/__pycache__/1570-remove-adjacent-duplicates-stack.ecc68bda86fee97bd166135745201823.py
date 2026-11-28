
# apl-source:1
# مثال 1570 — حذف المكرر المتجاور بمكدس
# apl-source:2
# Remove adjacent duplicates with a stack
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1570-remove-adjacent-duplicates-stack.apl
# apl-source:6

# apl-source:7
# نضيف الحرف إلى المكدس
# apl-source:8
# إن ساوى الحرف قمة المكدس نحذف القمة
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
def احذف_المتجاور(نص_):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if len(مكدس) > 0 and مكدس[len(مكدس) - 1] == ح:
      # apl-source:22
      مكدس.pop()
    # apl-source:23
    else:
      # apl-source:24
      مكدس.append(ح)
  # apl-source:25
  return "".join(مكدس)
# apl-source:26

# apl-source:27
تأكد_يساوي(احذف_المتجاور("abbaca"), "ca", "مثال")
# apl-source:28
تأكد_يساوي(احذف_المتجاور("azxxzy"), "ay", "متداخل")
# apl-source:29
تأكد_يساوي(احذف_المتجاور("aa"), "", "كله")
# apl-source:30
