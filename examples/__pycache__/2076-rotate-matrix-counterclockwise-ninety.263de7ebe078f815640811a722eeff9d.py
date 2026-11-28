
# apl-source:1
# مثال 2076 — تدوير المصفوفة عكس عقارب الساعة
# apl-source:2
# Rotate matrix counterclockwise
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2076-rotate-matrix-counterclockwise-ninety.apl
# apl-source:6

# apl-source:7
# # نبني الصف i من العمود n-1-i
# apl-source:8
# # من الأعلى للأسفل
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
  for ج in range(ن - 1, -1, -1):
    # apl-source:22
    صف = []
    # apl-source:23
    for ي in range(ن):
      # apl-source:24
      صف = صف + [م[ي][ج]]
    # apl-source:25
    خرج = خرج + [صف]
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(دور([[1, 2], [3, 4]]), [[2, 4], [1, 3]], "٢×٢")
# apl-source:29
تأكد_يساوي(دور([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[3, 6, 9], [2, 5, 8], [1, 4, 7]], "٣×٣")
# apl-source:30
