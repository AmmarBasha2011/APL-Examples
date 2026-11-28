
# apl-source:1
# مثال 1527 — التطبيع بين صفر وواحد
# apl-source:2
# Min max normalization
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1527-min-max-normalize.apl
# apl-source:6

# apl-source:7
# نطرح الأصغر من كل قيمة
# apl-source:8
# نقسم على المدى
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
def طبّع(أ):
  # apl-source:19
  صغرى = أ[0]
  # apl-source:20
  كبرى = أ[0]
  # apl-source:21
  for ع in أ:
    # apl-source:22
    if ع < صغرى:
      # apl-source:23
      صغرى = ع
    # apl-source:24
    if ع > كبرى:
      # apl-source:25
      كبرى = ع
  # apl-source:26
  مدى = كبرى - صغرى
  # apl-source:27
  ناتج = []
  # apl-source:28
  for ع in أ:
    # apl-source:29
    if مدى == 0:
      # apl-source:30
      ناتج.append(0.0)
    # apl-source:31
    else:
      # apl-source:32
      ناتج.append((ع - صغرى) / مدى)
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(طبّع([10, 20, 30]), [0.0, 0.5, 1.0], "ثلاث قيم")
# apl-source:36
تأكد_يساوي(طبّع([4, 4]), [0.0, 0.0], "متساوية")
# apl-source:37
