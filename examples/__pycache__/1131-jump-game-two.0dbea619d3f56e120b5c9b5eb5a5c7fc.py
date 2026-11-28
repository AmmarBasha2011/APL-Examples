
# apl-source:1
# مثال 1131 — قفزات أقل
# apl-source:2
# Jump game II minimum jumps
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1131-jump-game-two.apl
# apl-source:6

# apl-source:7
# نتتبع أبعد نقطة نصلها في القفزة الحالية
# apl-source:8
# وعند بلوغ حد القفزة نزيد العداد
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
def اقل_قفزات(أ):
  # apl-source:19
  قفزات = 0
  # apl-source:20
  حد = 0
  # apl-source:21
  ابعد = 0
  # apl-source:22
  for ع in range(len(أ) - 1):
    # apl-source:23
    if ع + أ[ع] > ابعد:
      # apl-source:24
      ابعد = ع + أ[ع]
    # apl-source:25
    if ع == حد:
      # apl-source:26
      قفزات = قفزات + 1
      # apl-source:27
      حد = ابعد
  # apl-source:28
  return قفزات
# apl-source:29

# apl-source:30
تأكد_يساوي(اقل_قفزات([2,3,1,1,4]), 2, "مثال أول")
# apl-source:31
تأكد_يساوي(اقل_قفزات([2,3,0,1,4]), 2, "مع صفر")
# apl-source:32
تأكد_يساوي(اقل_قفزات([1]), 0, "عنصر واحد")
# apl-source:33
تأكد_يساوي(اقل_قفزات([1,1,1,1]), 3, "خطوات صغيرة")
# apl-source:34
تأكد_يساوي(اقل_قفزات([10,1,1,1]), 1, "قفزة كبيرة")
# apl-source:35
