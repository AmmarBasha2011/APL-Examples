
# apl-source:1
# مثال 1907 — دمج قائمتين مرتبتين
# apl-source:2
# Merge two sorted linked lists
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1907-merge-two-sorted-linked-lists.apl
# apl-source:6

# apl-source:7
# نقارن رأسي القائمتين
# apl-source:8
# نأخذ الأصغر ونتقدم
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
def دمج(قيم1, قيم2):
  # apl-source:19
  خرج = []
  # apl-source:20
  أ = 0
  # apl-source:21
  ب = 0
  # apl-source:22
  while أ < len(قيم1) and ب < len(قيم2):
    # apl-source:23
    if قيم1[أ] <= قيم2[ب]:
      # apl-source:24
      خرج = خرج + [قيم1[أ]]
      # apl-source:25
      أ = أ + 1
    # apl-source:26
    else:
      # apl-source:27
      خرج = خرج + [قيم2[ب]]
      # apl-source:28
      ب = ب + 1
  # apl-source:29
  for ك in range(أ, len(قيم1)):
    # apl-source:30
    خرج = خرج + [قيم1[ك]]
  # apl-source:31
  for ك in range(ب, len(قيم2)):
    # apl-source:32
    خرج = خرج + [قيم2[ك]]
  # apl-source:33
  return خرج
# apl-source:34

# apl-source:35
تأكد_يساوي(دمج([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6], "متداخلة")
# apl-source:36
تأكد_يساوي(دمج([], [1, 2]), [1, 2], "الأولى فارغة")
# apl-source:37
تأكد_يساوي(دمج([1, 1], [1]), [1, 1, 1], "مكررة")
# apl-source:38
