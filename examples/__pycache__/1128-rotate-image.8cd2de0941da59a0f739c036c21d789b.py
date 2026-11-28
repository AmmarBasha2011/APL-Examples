
# apl-source:1
# مثال 1128 — تدوير صورة
# apl-source:2
# Rotate image 90 degrees
# apl-source:3
# Demonstrates: نقل ثم عكس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1128-rotate-image.apl
# apl-source:6

# apl-source:7
# ننقل المصفوفة ثم نعكس كل صف
# apl-source:8
# والنتيجة تدوير مع عقارب الساعة
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
  ناتج = []
  # apl-source:21
  for ص in range(ن):
    # apl-source:22
    صف = []
    # apl-source:23
    for ج in range(ن):
      # apl-source:24
      صف = صف + [م[ن - 1 - ج][ص]]
    # apl-source:25
    ناتج = ناتج + [صف]
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(دور([[1,2],[3,4]]), [[3,1],[4,2]], "اثنان")
# apl-source:29
تأكد_يساوي(دور([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]], "ثلاثة")
# apl-source:30
تأكد_يساوي(دور(دور(دور(دور([[1,2],[3,4]])))), [[1,2],[3,4]], "أربع مرات")
# apl-source:31
تأكد_يساوي(دور([[5]]), [[5]], "عنصر")
# apl-source:32
