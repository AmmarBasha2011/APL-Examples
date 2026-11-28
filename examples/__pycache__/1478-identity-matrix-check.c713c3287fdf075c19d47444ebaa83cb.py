
# apl-source:1
# مثال 1478 — هل المصفوفة وحدة
# apl-source:2
# Is it an identity matrix
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1478-identity-matrix-check.apl
# apl-source:6

# apl-source:7
# نفحص كل خانة
# apl-source:8
# نتوقف عند أول خانة مخالفة
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
def هي_وحدة(م):
  # apl-source:19
  for ص in range(len(م)):
    # apl-source:20
    for ع in range(len(م[ص])):
      # apl-source:21
      متوقع = 0
      # apl-source:22
      if ص == ع:
        # apl-source:23
        متوقع = 1
      # apl-source:24
      if م[ص][ع] != متوقع:
        # apl-source:25
        return False
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
تأكد_يساوي(هي_وحدة([[1, 0], [0, 1]]), True, "وحدة")
# apl-source:29
تأكد_يساوي(هي_وحدة([[1, 1], [0, 1]]), False, "عنصر زائد")
# apl-source:30
تأكد_يساوي(هي_وحدة([[2, 0], [0, 2]]), False, "ضعف الوحدة")
# apl-source:31
