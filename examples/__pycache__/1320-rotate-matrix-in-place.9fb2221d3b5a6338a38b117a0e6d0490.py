
# apl-source:1
# مثال 1320 — تدوير في المكان
# apl-source:2
# Rotate matrix in place by transpose
# apl-source:3
# Demonstrates: نقل وعكس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1320-rotate-matrix-in-place.apl
# apl-source:6

# apl-source:7
# ننقل المصفوفة بتبديل العناصر حول القطر
# apl-source:8
# ثم نعكس كل صف
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
def دور_مكانه(م):
  # apl-source:19
  ن = len(م)
  # apl-source:20
  for ع in range(ن):
    # apl-source:21
    for ج in range(ع + 1, ن):
      # apl-source:22
      ت = م[ع][ج]
      # apl-source:23
      م[ع][ج] = م[ج][ع]
      # apl-source:24
      م[ج][ع] = ت
  # apl-source:25
  for صف in م:
    # apl-source:26
    صف.reverse()
  # apl-source:27
  return م
# apl-source:28

# apl-source:29
تأكد_يساوي(دور_مكانه([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]], "ثلاثة")
# apl-source:30
تأكد_يساوي(دور_مكانه([[1,2],[3,4]]), [[3,1],[4,2]], "اثنان")
# apl-source:31
تأكد_يساوي(دور_مكانه([[1]]), [[1]], "واحد")
# apl-source:32
