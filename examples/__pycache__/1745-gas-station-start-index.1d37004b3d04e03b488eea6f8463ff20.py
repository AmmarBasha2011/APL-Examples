
# apl-source:1
# مثال 1745 — محطة البداية للدورة
# apl-source:2
# Gas station circuit start
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1745-gas-station-start-index.apl
# apl-source:6

# apl-source:7
# إذا انقطع الوقود نبدأ بعد المحطة
# apl-source:8
# المجموع الكلي يجب ألا ينقص
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
def بداية(وقود, كلفة):
  # apl-source:19
  كلي = 0
  # apl-source:20
  خزان = 0
  # apl-source:21
  بدء = 0
  # apl-source:22
  for ك in range(len(وقود)):
    # apl-source:23
    فرق = وقود[ك] - كلفة[ك]
    # apl-source:24
    كلي = كلي + فرق
    # apl-source:25
    خزان = خزان + فرق
    # apl-source:26
    if خزان < 0:
      # apl-source:27
      بدء = ك + 1
      # apl-source:28
      خزان = 0
  # apl-source:29
  if كلي < 0:
    # apl-source:30
    return -1
  # apl-source:31
  return بدء
# apl-source:32

# apl-source:33
تأكد_يساوي(بداية([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3, "ثلاثة")
# apl-source:34
تأكد_يساوي(بداية([2, 3, 4], [3, 4, 3]), -1, "مستحيل")
# apl-source:35
