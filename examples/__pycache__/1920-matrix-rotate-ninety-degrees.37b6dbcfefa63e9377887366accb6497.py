
# apl-source:1
# مثال 1920 — تدوير مصفوفة ٩٠ درجة
# apl-source:2
# Rotate matrix by ninety degrees
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1920-matrix-rotate-ninety-degrees.apl
# apl-source:6

# apl-source:7
# ننشئ مصفوفة جديدة
# apl-source:8
# العنصر (ص،ج) ينتقل إلى (ج،ن-1-ص)
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
def دور(م):
  # apl-source:19
  ن = len(م)
  # apl-source:20
  خرج = []
  # apl-source:21
  for ص in range(ن):
    # apl-source:22
    صف = []
    # apl-source:23
    for ج in range(ن):
      # apl-source:24
      صف = صف + [0]
    # apl-source:25
    خرج = خرج + [صف]
  # apl-source:26
  for ص in range(ن):
    # apl-source:27
    for ج in range(ن):
      # apl-source:28
      خرج[ج][ن - 1 - ص] = م[ص][ج]
  # apl-source:29
  return خرج
# apl-source:30

# apl-source:31
تأكد_يساوي(دور([[1, 2], [3, 4]]), [[3, 1], [4, 2]], "٢ في ٢")
# apl-source:32
تأكد_يساوي(دور([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "٣ في ٣")
# apl-source:33
تأكد_يساوي(دور([[5]]), [[5]], "عنصر")
# apl-source:34
