
# apl-source:1
# مثال 2071 — أثر المصفوفة وبناء مصفوفة الوحدة
# apl-source:2
# Matrix trace and identity
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2071-matrix-trace-and-identity-build.apl
# apl-source:6

# apl-source:7
# # مصفوفة الوحدة آحاد على القطر
# apl-source:8
# # والأثر لمصفوفة مربعة
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
def وحدة(ن):
  # apl-source:19
  م = []
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    صف = [0] * ن
    # apl-source:22
    صف[ي] = 1
    # apl-source:23
    م = م + [صف]
  # apl-source:24
  return م
# apl-source:25

# apl-source:26
def اثر(م):
  # apl-source:27
  مج = 0
  # apl-source:28
  for ي in range(len(م)):
    # apl-source:29
    مج = مج + م[ي][ي]
  # apl-source:30
  return مج
# apl-source:31

# apl-source:32
تأكد_يساوي(وحدة(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "وحدة")
# apl-source:33
تأكد_يساوي(اثر([[1, 2], [3, 4]]), 5, "أثر")
# apl-source:34
تأكد_يساوي(اثر(وحدة(5)), 5, "أثر الوحدة")
# apl-source:35
