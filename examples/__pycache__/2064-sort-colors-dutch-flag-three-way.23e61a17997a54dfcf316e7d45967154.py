
# apl-source:1
# مثال 2064 — فرز الألوان بعلم هولندا
# apl-source:2
# Dutch national flag sort
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2064-sort-colors-dutch-flag-three-way.apl
# apl-source:6

# apl-source:7
# # الصفر يذهب لليسار والاثنان لليمين
# apl-source:8
# # نمر مرة واحدة
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
def الوان(ق):
  # apl-source:19
  ق = ق[:]
  # apl-source:20
  ي = 0
  # apl-source:21
  ك = 0
  # apl-source:22
  ل = len(ق) - 1
  # apl-source:23
  while ك <= ل:
    # apl-source:24
    if ق[ك] == 0:
      # apl-source:25
      ت = ق[ي]
      # apl-source:26
      ق[ي] = ق[ك]
      # apl-source:27
      ق[ك] = ت
      # apl-source:28
      ي = ي + 1
      # apl-source:29
      ك = ك + 1
    # apl-source:30
    elif ق[ك] == 2:
      # apl-source:31
      ت = ق[ل]
      # apl-source:32
      ق[ل] = ق[ك]
      # apl-source:33
      ق[ك] = ت
      # apl-source:34
      ل = ل - 1
    # apl-source:35
    else:
      # apl-source:36
      ك = ك + 1
  # apl-source:37
  return ق
# apl-source:38

# apl-source:39
تأكد_يساوي(الوان([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2], "ستة")
# apl-source:40
تأكد_يساوي(الوان([2, 0, 1]), [0, 1, 2], "ثلاثة")
# apl-source:41
تأكد_يساوي(الوان([1]), [1], "واحد")
# apl-source:42
