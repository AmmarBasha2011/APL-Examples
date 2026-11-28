
# apl-source:1
# مثال 1695 — طابور بمكدسين
# apl-source:2
# Queue built from two stacks
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1695-queue-via-two-stacks.apl
# apl-source:6

# apl-source:7
# الدخول في مكدس والخروج من آخر
# apl-source:8
# ننقل عند فراغ مكدس الخروج
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
def أدخل(ط, قيمة):
  # apl-source:19
  ط[0].append(قيمة)
# apl-source:20

# apl-source:21
def أخرج(ط):
  # apl-source:22
  if len(ط[1]) == 0:
    # apl-source:23
    while len(ط[0]) > 0:
      # apl-source:24
      ط[1].append(ط[0].pop())
  # apl-source:25
  return ط[1].pop()
# apl-source:26

# apl-source:27
ط = [[], []]
# apl-source:28
أدخل(ط, 1)
# apl-source:29
أدخل(ط, 2)
# apl-source:30
أدخل(ط, 3)
# apl-source:31
تأكد_يساوي(أخرج(ط), 1, "الأول")
# apl-source:32
أدخل(ط, 4)
# apl-source:33
تأكد_يساوي(أخرج(ط), 2, "الثاني")
# apl-source:34
تأكد_يساوي(أخرج(ط), 3, "الثالث")
# apl-source:35
تأكد_يساوي(أخرج(ط), 4, "الرابع")
# apl-source:36
