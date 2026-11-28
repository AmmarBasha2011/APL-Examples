
# apl-source:1
# مثال 1708 — حجم المنطقة المتصلة
# apl-source:2
# Connected region size flood fill
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1708-flood-fill-region-size.apl
# apl-source:6

# apl-source:7
# نبدأ من خلية
# apl-source:8
# نتوسع في الاتجاهات الأربعة
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
def حجم_المنطقة(شبكة, ص0, س0):
  # apl-source:19
  قيمة = شبكة[ص0][س0]
  # apl-source:20
  رأينا = {}
  # apl-source:21
  مكدس = [[ص0, س0]]
  # apl-source:22
  رأينا[str(ص0) + "," + str(س0)] = 1
  # apl-source:23
  عد = 0
  # apl-source:24
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:25
  while len(مكدس) > 0:
    # apl-source:26
    ح = مكدس.pop()
    # apl-source:27
    عد = عد + 1
    # apl-source:28
    for ا in اتجاهات:
      # apl-source:29
      ي = ح[0] + ا[0]
      # apl-source:30
      ك = ح[1] + ا[1]
      # apl-source:31
      if ي >= 0 and ي < len(شبكة) and ك >= 0 and ك < len(شبكة[0]):
        # apl-source:32
        مفتاح = str(ي) + "," + str(ك)
        # apl-source:33
        if شبكة[ي][ك] == قيمة:
          # apl-source:34
          if (مفتاح in رأينا) == False:
            # apl-source:35
            رأينا[مفتاح] = 1
            # apl-source:36
            مكدس.append([ي, ك])
  # apl-source:37
  return عد
# apl-source:38

# apl-source:39
ش = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
# apl-source:40
تأكد_يساوي(حجم_المنطقة(ش, 0, 0), 3, "ثلاث")
# apl-source:41
تأكد_يساوي(حجم_المنطقة(ش, 2, 2), 1, "منفردة")
# apl-source:42
تأكد_يساوي(حجم_المنطقة(ش, 0, 2), 2, "أصفار")
# apl-source:43
