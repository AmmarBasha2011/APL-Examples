
# apl-source:1
# مثال 1594 — ارتفاع شجرة ثنائية
# apl-source:2
# Binary tree height
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1594-binary-tree-height.apl
# apl-source:6

# apl-source:7
# العقدة قائمة [القيمة، اليسار، اليمين]
# apl-source:8
# الشجرة الفارغة قائمة فارغة
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
def الارتفاع(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return 0
  # apl-source:21
  ي = الارتفاع(ش[1])
  # apl-source:22
  م = الارتفاع(ش[2])
  # apl-source:23
  return 1 + max(ي, م)
# apl-source:24

# apl-source:25
تأكد_يساوي(الارتفاع([]), 0, "فارغة")
# apl-source:26
تأكد_يساوي(الارتفاع([1, [], []]), 1, "عقدة")
# apl-source:27
تأكد_يساوي(الارتفاع([1, [2, [4, [], []], []], [3, [], []]]), 3, "ثلاثة مستويات")
# apl-source:28
