
# apl-source:1
# مثال 1154 — مجموع ثلاثة
# apl-source:2
# Three sum
# apl-source:3
# Demonstrates: ترتيب ومؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1154-three-sum.apl
# apl-source:6

# apl-source:7
# نرتب القائمة ونثبت عنصراً
# apl-source:8
# ثم نبحث عن الزوج المكمل بمؤشرين
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
def ثلاثيات(أ):
  # apl-source:19
  ق = sorted(أ)
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ع in range(len(ق) - 2):
    # apl-source:22
    مكرر = False
    # apl-source:23
    if ع > 0:
      # apl-source:24
      مكرر = ق[ع] == ق[ع - 1]
    # apl-source:25
    ي = ع + 1
    # apl-source:26
    ن = len(ق) - 1
    # apl-source:27
    if مكرر:
      # apl-source:28
      ي = ن
    # apl-source:29
    while ي < ن:
      # apl-source:30
      مج = ق[ع] + ق[ي] + ق[ن]
      # apl-source:31
      if مج == 0:
        # apl-source:32
        ناتج = ناتج + [[ق[ع], ق[ي], ق[ن]]]
        # apl-source:33
        ي = ي + 1
        # apl-source:34
        while (ي < ن) and (ق[ي] == ق[ي - 1]):
          # apl-source:35
          ي = ي + 1
      # apl-source:36
      elif مج < 0:
        # apl-source:37
        ي = ي + 1
      # apl-source:38
      else:
        # apl-source:39
        ن = ن - 1
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
تأكد_يساوي(ثلاثيات([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]], "مثال أول")
# apl-source:43
تأكد_يساوي(ثلاثيات([0,1,1]), [], "لا حل")
# apl-source:44
تأكد_يساوي(ثلاثيات([0,0,0,0]), [[0,0,0]], "أصفار")
# apl-source:45
