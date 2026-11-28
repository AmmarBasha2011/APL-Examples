
# apl-source:1
# مثال 2299 — المحدد حتى 3×3
# apl-source:2
# Determinant up to 3x3
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2299-matrix-determinant-two-by-two-or-three.apl
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
  if len(م) == 1:
    # apl-source:20
    return م[0][0]
  # apl-source:21
  if len(م) == 2:
    # apl-source:22
    return م[0][0] * م[1][1] - م[0][1] * م[1][0]
  # apl-source:23
  أ = م[0][0] * (م[1][1] * م[2][2] - م[1][2] * م[2][1])
  # apl-source:24
  ب = م[0][1] * (م[1][0] * م[2][2] - م[1][2] * م[2][0])
  # apl-source:25
  ج = م[0][2] * (م[1][0] * م[2][1] - م[1][1] * م[2][0])
  # apl-source:26
  return أ - ب + ج
# apl-source:27

# apl-source:28
تأكد_يساوي(ف([[1, 2], [3, 4]]), -2, "حالة 1")
# apl-source:29
تأكد_يساوي(ف([[5]]), 5, "حالة 2")
# apl-source:30
تأكد_يساوي(ف([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0, "حالة 3")
# apl-source:31
تأكد_يساوي(ف([[0, 1], [1, 0]]), -1, "حالة 4")
# apl-source:32
تأكد_يساوي(ف([[2, -1, 0], [0, 3, 1], [1, 1, 1]]), 3, "حالة 5")
# apl-source:33
