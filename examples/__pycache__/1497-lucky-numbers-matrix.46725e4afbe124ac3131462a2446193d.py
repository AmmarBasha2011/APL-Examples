
# apl-source:1
# مثال 1497 — الأرقام المحظوظة في مصفوفة
# apl-source:2
# Lucky numbers in a matrix
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1497-lucky-numbers-matrix.apl
# apl-source:6

# apl-source:7
# نحسب أصغر كل صف وأكبر كل عمود
# apl-source:8
# العنصر المحظوظ يظهر في القائمتين
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
def محظوظة(م):
  # apl-source:19
  صغرى = []
  # apl-source:20
  for ص in م:
    # apl-source:21
    ص_صغرى = ص[0]
    # apl-source:22
    for ع in ص:
      # apl-source:23
      if ع < ص_صغرى:
        # apl-source:24
        ص_صغرى = ع
    # apl-source:25
    صغرى.append(ص_صغرى)
  # apl-source:26
  ناتج = []
  # apl-source:27
  for ع in range(len(م[0])):
    # apl-source:28
    عمود_كبرى = م[0][ع]
    # apl-source:29
    for ص in م:
      # apl-source:30
      if ص[ع] > عمود_كبرى:
        # apl-source:31
        عمود_كبرى = ص[ع]
    # apl-source:32
    if عمود_كبرى in صغرى:
      # apl-source:33
      ناتج.append(عمود_كبرى)
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
تأكد_يساوي(محظوظة([[3, 7, 8], [9, 11, 13], [15, 16, 17]]), [15], "واحد")
# apl-source:37
تأكد_يساوي(محظوظة([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]), [12], "اثنا عشر")
# apl-source:38
تأكد_يساوي(محظوظة([[7, 8], [1, 2]]), [7], "سبعة")
# apl-source:39
