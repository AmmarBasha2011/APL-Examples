
# apl-source:1
# مثال 1013 — محطة الوقود
# apl-source:2
# Gas station circuit
# apl-source:3
# Demonstrates: رصيد تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1013-gas-station.apl
# apl-source:6

# apl-source:7
# لو مجموع الوقود لا يقل عن مجموع الكلفة فالدورة ممكنة
# apl-source:8
# نبدأ من المحطة التالية كلما هبط الرصيد دون الصفر
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
def بداية_الدورة(وقود, كلفة):
  # apl-source:19
  كلي = 0
  # apl-source:20
  رصيد = 0
  # apl-source:21
  بداية = 0
  # apl-source:22
  for ع in range(len(وقود)):
    # apl-source:23
    فرق = وقود[ع] - كلفة[ع]
    # apl-source:24
    كلي = كلي + فرق
    # apl-source:25
    رصيد = رصيد + فرق
    # apl-source:26
    if رصيد < 0:
      # apl-source:27
      بداية = ع + 1
      # apl-source:28
      رصيد = 0
  # apl-source:29
  if كلي < 0:
    # apl-source:30
    return -1
  # apl-source:31
  return بداية
# apl-source:32

# apl-source:33
تأكد_يساوي(بداية_الدورة([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3, "تبدأ من الفهرس 3")
# apl-source:34
تأكد_يساوي(بداية_الدورة([2, 3, 4], [3, 4, 3]), -1, "مستحيلة")
# apl-source:35
تأكد_يساوي(بداية_الدورة([5], [4]), 0, "محطة واحدة")
# apl-source:36
