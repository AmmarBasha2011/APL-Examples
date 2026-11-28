
# apl-source:1
# مثال 2298 — المرور الحلزوني
# apl-source:2
# Spiral order
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2298-matrix-spiral-order-walk.apl
# apl-source:6

# apl-source:7
# # مصفوفة من قوائم
# apl-source:8
# # ونتحقق من الناتج
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
def ف(م):
  # apl-source:19
  ر = []
  # apl-source:20
  ع = [ص[:] for ص in م] if False else م
  # apl-source:21
  أ = 0
  # apl-source:22
  ب = len(م) - 1
  # apl-source:23
  ي = 0
  # apl-source:24
  ك = len(م[0]) - 1
  # apl-source:25
  while أ <= ب and ي <= ك:
    # apl-source:26
    for ج in range(ي, ك + 1):
      # apl-source:27
      ر = ر + [م[أ][ج]]
    # apl-source:28
    أ = أ + 1
    # apl-source:29
    for ج in range(أ, ب + 1):
      # apl-source:30
      ر = ر + [م[ج][ك]]
    # apl-source:31
    ك = ك - 1
    # apl-source:32
    if أ <= ب:
      # apl-source:33
      for ج in range(ك, ي - 1, -1):
        # apl-source:34
        ر = ر + [م[ب][ج]]
      # apl-source:35
      ب = ب - 1
    # apl-source:36
    if ي <= ك:
      # apl-source:37
      for ج in range(ب, أ - 1, -1):
        # apl-source:38
        ر = ر + [م[ج][ي]]
      # apl-source:39
      ي = ي + 1
  # apl-source:40
  return ر
# apl-source:41

# apl-source:42
تأكد_يساوي(ف([[1, 2], [3, 4]]), [1, 2, 4, 3], "حالة 1")
# apl-source:43
تأكد_يساوي(ف([[5]]), [5], "حالة 2")
# apl-source:44
تأكد_يساوي(ف([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5], "حالة 3")
# apl-source:45
تأكد_يساوي(ف([[0, 1], [1, 0]]), [0, 1, 0, 1], "حالة 4")
# apl-source:46
تأكد_يساوي(ف([[2, -1, 0], [0, 3, 1], [1, 1, 1]]), [2, -1, 0, 1, 1, 1, 1, 0, 3], "حالة 5")
# apl-source:47
