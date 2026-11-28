
# apl-source:1
# مثال 1065 — أقل مسار في المثلث
# apl-source:2
# Triangle minimum path sum
# apl-source:3
# Demonstrates: برمجة من الأسفل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1065-triangle-min-path.apl
# apl-source:6

# apl-source:7
# نبدأ من الصف الأخير صعوداً
# apl-source:8
# كل خلية تضيف أصغر خليتين تحتها
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
def اقل_مثلث(م):
  # apl-source:19
  د = list(م[len(م) - 1])
  # apl-source:20
  for ر in range(len(م) - 2, -1, -1):
    # apl-source:21
    for ك in range(len(م[ر])):
      # apl-source:22
      افضل = د[ك]
      # apl-source:23
      if د[ك + 1] < افضل:
        # apl-source:24
        افضل = د[ك + 1]
      # apl-source:25
      د[ك] = م[ر][ك] + افضل
  # apl-source:26
  return د[0]
# apl-source:27

# apl-source:28
تأكد_يساوي(اقل_مثلث([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11, "أربعة صفوف")
# apl-source:29
تأكد_يساوي(اقل_مثلث([[-10]]), -10, "خلية")
# apl-source:30
تأكد_يساوي(اقل_مثلث([[1], [2, 3]]), 3, "صفان")
# apl-source:31
