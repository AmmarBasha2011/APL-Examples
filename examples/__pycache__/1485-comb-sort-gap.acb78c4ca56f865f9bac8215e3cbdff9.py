
# apl-source:1
# مثال 1485 — فرز المشط
# apl-source:2
# Comb sort
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1485-comb-sort-gap.apl
# apl-source:6

# apl-source:7
# نقارن عناصر تفصل بينها فجوة
# apl-source:8
# نقسم الفجوة على 1.3 حتى تصبح واحداً
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
def فرز_المشط(أ):
  # apl-source:19
  فجوة = len(أ)
  # apl-source:20
  مبدل = True
  # apl-source:21
  while فجوة > 1 or مبدل:
    # apl-source:22
    فجوة = int(فجوة / 1.3)
    # apl-source:23
    if فجوة < 1:
      # apl-source:24
      فجوة = 1
    # apl-source:25
    مبدل = False
    # apl-source:26
    for ع in range(len(أ) - فجوة):
      # apl-source:27
      if أ[ع] > أ[ع + فجوة]:
        # apl-source:28
        ت = أ[ع]
        # apl-source:29
        أ[ع] = أ[ع + فجوة]
        # apl-source:30
        أ[ع + فجوة] = ت
        # apl-source:31
        مبدل = True
  # apl-source:32
  return أ
# apl-source:33

# apl-source:34
تأكد_يساوي(فرز_المشط([8, 4, 1, 56, 3, -44, 23]), [-44, 1, 3, 4, 8, 23, 56], "سبعة")
# apl-source:35
تأكد_يساوي(فرز_المشط([2, 1]), [1, 2], "اثنان")
# apl-source:36
تأكد_يساوي(فرز_المشط([1]), [1], "واحد")
# apl-source:37
