
# apl-source:1
# مثال 1146 — سحق حلوى
# apl-source:2
# One-dimensional candy crush
# apl-source:3
# Demonstrates: مكدس مع عدّاد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1146-candy-crush-1d.apl
# apl-source:6

# apl-source:7
# نخزن الحرف وعدد تكراره المتتالي
# apl-source:8
# ونحذف الكتلة حين يبلغ العدد ثلاثة
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
def اسحق(س):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ح in س:
    # apl-source:21
    if (len(مكدس) > 0) and (مكدس[-1][0] == ح):
      # apl-source:22
      مكدس[-1][1] = مكدس[-1][1] + 1
    # apl-source:23
    else:
      # apl-source:24
      مكدس = مكدس + [[ح, 1]]
    # apl-source:25
    if مكدس[-1][1] == 3:
      # apl-source:26
      مكدس.pop()
  # apl-source:27
  ناتج = ""
  # apl-source:28
  for ز in مكدس:
    # apl-source:29
    ناتج = ناتج + ز[0] * ز[1]
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(اسحق("aaabbbc"), "c", "كتلتان")
# apl-source:33
تأكد_يساوي(اسحق("abbba"), "aa", "تسلسل")
# apl-source:34
تأكد_يساوي(اسحق("aabbccc"), "aabb", "نهاية")
# apl-source:35
تأكد_يساوي(اسحق("abc"), "abc", "بلا إزالة")
# apl-source:36
تأكد_يساوي(اسحق("aaaa"), "a", "أربعة")
# apl-source:37
