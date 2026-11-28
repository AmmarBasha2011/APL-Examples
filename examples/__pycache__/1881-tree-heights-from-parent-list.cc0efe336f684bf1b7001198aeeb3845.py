
# apl-source:1
# مثال 1881 — ارتفاع الشجرة من مصفوفة الآباء
# apl-source:2
# Tree height from parent list
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1881-tree-heights-from-parent-list.apl
# apl-source:6

# apl-source:7
# نحسب عمق كل عقدة
# apl-source:8
# الارتفاع أكبر عمق
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
def ارتفاع(آباء):
  # apl-source:19
  عمق = []
  # apl-source:20
  for ك in آباء:
    # apl-source:21
    عمق.append(-1)
  # apl-source:22
  أعلى = 0
  # apl-source:23
  for ك in range(len(آباء)):
    # apl-source:24
    مسار = []
    # apl-source:25
    ع = ك
    # apl-source:26
    while ع != -1 and عمق[ع] == -1:
      # apl-source:27
      مسار.append(ع)
      # apl-source:28
      ع = آباء[ع]
    # apl-source:29
    د = 0
    # apl-source:30
    if ع != -1:
      # apl-source:31
      د = عمق[ع] + 1
    # apl-source:32
    مسار.reverse()
    # apl-source:33
    for ن in مسار:
      # apl-source:34
      عمق[ن] = د
      # apl-source:35
      د = د + 1
    # apl-source:36
    أعلى = max(أعلى, عمق[ك])
  # apl-source:37
  return أعلى
# apl-source:38

# apl-source:39
تأكد_يساوي(ارتفاع([-1, 0, 0, 1, 1, 3]), 3, "ثلاثة")
# apl-source:40
تأكد_يساوي(ارتفاع([-1]), 0, "جذر")
# apl-source:41
تأكد_يساوي(ارتفاع([-1, 0, 0, 0]), 1, "نجمة")
# apl-source:42
