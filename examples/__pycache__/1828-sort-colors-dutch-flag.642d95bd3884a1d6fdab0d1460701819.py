
# apl-source:1
# مثال 1828 — فرز الألوان صفر واحد اثنان
# apl-source:2
# Sort colors Dutch flag
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1828-sort-colors-dutch-flag.apl
# apl-source:6

# apl-source:7
# الصفر إلى البداية والاثنان إلى النهاية
# apl-source:8
# الواحد يبقى في الوسط
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
def افرز_الألوان(ق):
  # apl-source:19
  ق = ق + []
  # apl-source:20
  بداية = 0
  # apl-source:21
  وسط = 0
  # apl-source:22
  نهاية = len(ق) - 1
  # apl-source:23
  while وسط <= نهاية:
    # apl-source:24
    if ق[وسط] == 0:
      # apl-source:25
      ت = ق[بداية]
      # apl-source:26
      ق[بداية] = ق[وسط]
      # apl-source:27
      ق[وسط] = ت
      # apl-source:28
      بداية = بداية + 1
      # apl-source:29
      وسط = وسط + 1
    # apl-source:30
    elif ق[وسط] == 1:
      # apl-source:31
      وسط = وسط + 1
    # apl-source:32
    else:
      # apl-source:33
      ت = ق[نهاية]
      # apl-source:34
      ق[نهاية] = ق[وسط]
      # apl-source:35
      ق[وسط] = ت
      # apl-source:36
      نهاية = نهاية - 1
  # apl-source:37
  return ق
# apl-source:38

# apl-source:39
تأكد_يساوي(افرز_الألوان([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2], "ستة")
# apl-source:40
تأكد_يساوي(افرز_الألوان([1, 0]), [0, 1], "اثنان")
# apl-source:41
تأكد_يساوي(افرز_الألوان([0]), [0], "واحد")
# apl-source:42
