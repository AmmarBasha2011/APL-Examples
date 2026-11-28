
# apl-source:1
# مثال 1416 — اسم مضغوط طويلاً
# apl-source:2
# Long pressed name
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1416-long-pressed-name.apl
# apl-source:6

# apl-source:7
# مؤشران على الاسم والمكتوب
# apl-source:8
# الحرف المكرر يجب أن يطابق الحرف السابق
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
def ضغط_طويل(اسم, مكتوب):
  # apl-source:19
  ع = 0
  # apl-source:20
  for ج in range(len(مكتوب)):
    # apl-source:21
    if (ع < len(اسم)) and (اسم[ع] == مكتوب[ج]):
      # apl-source:22
      ع = ع + 1
    # apl-source:23
    elif (ج == 0) or (مكتوب[ج] != مكتوب[ج - 1]):
      # apl-source:24
      return False
  # apl-source:25
  return ع == len(اسم)
# apl-source:26

# apl-source:27
تأكد_يساوي(ضغط_طويل("alex", "aaleex"), True, "ضغط")
# apl-source:28
تأكد_يساوي(ضغط_طويل("saeed", "ssaaedd"), False, "ناقص")
# apl-source:29
تأكد_يساوي(ضغط_طويل("a", "a"), True, "حرف")
# apl-source:30
