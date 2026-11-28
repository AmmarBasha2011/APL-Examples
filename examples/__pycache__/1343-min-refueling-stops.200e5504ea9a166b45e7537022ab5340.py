
# apl-source:1
# مثال 1343 — أقل زيارات وقود
# apl-source:2
# Minimum refueling stops
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1343-min-refueling-stops.apl
# apl-source:6

# apl-source:7
# نسير بأبعد ما نستطيع
# apl-source:8
# وعند نفاد الوقود نأخذ أكبر خزان مررنا به
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
def اقل_محطات(هدف, وقود, محطات):
  # apl-source:19
  خزانات = []
  # apl-source:20
  ع = 0
  # apl-source:21
  زيارات = 0
  # apl-source:22
  مدى = وقود
  # apl-source:23
  while مدى < هدف:
    # apl-source:24
    while (ع < len(محطات)) and (محطات[ع][0] <= مدى):
      # apl-source:25
      خزانات = خزانات + [محطات[ع][1]]
      # apl-source:26
      ع = ع + 1
    # apl-source:27
    if len(خزانات) == 0:
      # apl-source:28
      return -1
    # apl-source:29
    خزانات = sorted(خزانات)
    # apl-source:30
    مدى = مدى + خزانات.pop()
    # apl-source:31
    زيارات = زيارات + 1
  # apl-source:32
  return زيارات
# apl-source:33

# apl-source:34
تأكد_يساوي(اقل_محطات(1, 1, []), 0, "لا حاجة")
# apl-source:35
تأكد_يساوي(اقل_محطات(100, 1, [[10,100]]), -1, "لا يصل")
# apl-source:36
تأكد_يساوي(اقل_محطات(100, 10, [[10,60],[20,30],[30,30],[60,40]]), 2, "توقفان")
# apl-source:37
