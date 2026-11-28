
# apl-source:1
# مثال 1713 — عمق الشجرة من أزواج الأب والابن
# apl-source:2
# Tree depth from parent array
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1713-tree-depth-from-pairs.apl
# apl-source:6

# apl-source:7
# الجذر أبوه سالب واحد
# apl-source:8
# نحسب أعمق عقدة
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
def عمق(آباء):
  # apl-source:19
  أعمق = 0
  # apl-source:20
  for ك in range(len(آباء)):
    # apl-source:21
    د = 0
    # apl-source:22
    ع = ك
    # apl-source:23
    while آباء[ع] != -1:
      # apl-source:24
      ع = آباء[ع]
      # apl-source:25
      د = د + 1
    # apl-source:26
    أعمق = max(أعمق, د)
  # apl-source:27
  return أعمق
# apl-source:28

# apl-source:29
تأكد_يساوي(عمق([-1, 0, 0, 1, 1, 3]), 3, "ثلاثة")
# apl-source:30
تأكد_يساوي(عمق([-1]), 0, "جذر")
# apl-source:31
تأكد_يساوي(عمق([-1, 0, 1, 2]), 3, "سلسلة")
# apl-source:32
