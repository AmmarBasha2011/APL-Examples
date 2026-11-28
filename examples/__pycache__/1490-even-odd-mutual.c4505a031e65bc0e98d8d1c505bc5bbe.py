
# apl-source:1
# مثال 1490 — زوجي وفردي بتراجع متبادل
# apl-source:2
# Even odd by mutual recursion
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1490-even-odd-mutual.apl
# apl-source:6

# apl-source:7
# الصفر زوجي
# apl-source:8
# العدد زوجي إذا كان سابقه فردياً
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
def زوجي_ت(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return True
  # apl-source:21
  return فردي_ت(ن - 1)
# apl-source:22

# apl-source:23
def فردي_ت(ن):
  # apl-source:24
  if ن == 0:
    # apl-source:25
    return False
  # apl-source:26
  return زوجي_ت(ن - 1)
# apl-source:27

# apl-source:28
تأكد_يساوي(زوجي_ت(10), True, "عشرة")
# apl-source:29
تأكد_يساوي(فردي_ت(7), True, "سبعة")
# apl-source:30
تأكد_يساوي(زوجي_ت(7), False, "سبعة ليست زوجية")
# apl-source:31
