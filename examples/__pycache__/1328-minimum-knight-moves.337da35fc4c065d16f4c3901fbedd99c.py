
# apl-source:1
# مثال 1328 — حركات الحصان
# apl-source:2
# Minimum knight moves
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1328-minimum-knight-moves.apl
# apl-source:6

# apl-source:7
# الحصان يتحرك بثماني حركات ممكنة
# apl-source:8
# نستخدم البحث بالعرض على رقعة كبيرة بما يكفي
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
def حركات(هدف_س, هدف_ص):
  # apl-source:19
  ح = [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
  # apl-source:20
  مرئي = {}
  # apl-source:21
  مرئي["0,0"] = True
  # apl-source:22
  طابور = [[0, 0, 0]]
  # apl-source:23
  ع = 0
  # apl-source:24
  while ع < len(طابور):
    # apl-source:25
    س = طابور[ع][0]
    # apl-source:26
    ص = طابور[ع][1]
    # apl-source:27
    خ = طابور[ع][2]
    # apl-source:28
    ع = ع + 1
    # apl-source:29
    if (س == هدف_س) and (ص == هدف_ص):
      # apl-source:30
      return خ
    # apl-source:31
    for ز in ح:
      # apl-source:32
      ن1 = س + ز[0]
      # apl-source:33
      ن2 = ص + ز[1]
      # apl-source:34
      مفتاح = str(ن1) + "," + str(ن2)
      # apl-source:35
      if (مفتاح not in مرئي) and (ن1 >= -2) and (ن1 <= 12) and (ن2 >= -2) and (ن2 <= 12):
        # apl-source:36
        مرئي[مفتاح] = True
        # apl-source:37
        طابور = طابور + [[ن1, ن2, خ + 1]]
  # apl-source:38
  return -1
# apl-source:39

# apl-source:40
تأكد_يساوي(حركات(2, 1), 1, "حركة واحدة")
# apl-source:41
تأكد_يساوي(حركات(5, 5), 4, "أربع حركات")
# apl-source:42
تأكد_يساوي(حركات(0, 0), 0, "نفس الخانة")
# apl-source:43
تأكد_يساوي(حركات(1, 1), 2, "قطرية")
# apl-source:44
