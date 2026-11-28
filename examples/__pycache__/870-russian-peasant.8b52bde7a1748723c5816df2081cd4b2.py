
# apl-source:1
# مثال 870 — الضرب الفلاحي
# apl-source:2
# Russian peasant multiplication
# apl-source:3
# Demonstrates: تنصيف ومضاعفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/870-russian-peasant.apl
# apl-source:6

# apl-source:7
# الضرب الفلاحي الروسي: ضرب بالتنصيف والمضاعفة فقط
# apl-source:8
# كل خانة فردية من القاسم تضيف المضاعف للحصيلة (ضرب ثنائي صرف)
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
def ضرب_فلاحي(أ, ب):
  # apl-source:19
  حصيلة = 0
  # apl-source:20
  مضروب = أ
  # apl-source:21
  قاسم = ب
  # apl-source:22
  while قاسم > 0:
    # apl-source:23
    if قاسم % 2 == 1:
      # apl-source:24
      حصيلة = حصيلة + مضروب
    # apl-source:25
    مضروب = مضروب * 2
    # apl-source:26
    قاسم = قاسم // 2
  # apl-source:27
  return حصيلة
# apl-source:28

# apl-source:29
print("13 × 11 =", ضرب_فلاحي(13, 11))
# apl-source:30
print("37 × 25 =", ضرب_فلاحي(37, 25))
# apl-source:31

# apl-source:32
تأكد_يساوي(ضرب_فلاحي(13, 11), 143, "13 في 11")
# apl-source:33
تأكد_يساوي(ضرب_فلاحي(37, 25), 925, "37 في 25")
# apl-source:34
تأكد_يساوي(ضرب_فلاحي(7, 0), 0, "ضرب بصفر")
# apl-source:35
تأكد_يساوي(ضرب_فلاحي(1, 99), 99, "ضرب بواحد")
# apl-source:36

# apl-source:37
# يطابق الضرب العادي لنطاق صغير
# apl-source:38
for س in range(1, 12):
  # apl-source:39
  for ص in range(1, 12):
    # apl-source:40
    تأكد_يساوي(ضرب_فلاحي(س, ص), س * ص, "تطابق عند " + str(س) + "×" + str(ص))
# apl-source:41
