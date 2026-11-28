
# apl-source:1
# مثال 1336 — قفزات ثلاثة
# apl-source:2
# Jump game III reach zero
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1336-jump-game-three.apl
# apl-source:6

# apl-source:7
# من الموضع i نقفز إلى i زائد أو ناقص القيمة
# apl-source:8
# نستخدم البحث بالعرض مع الزيارات
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
def يصل_صفر(مصفوفة, بداية):
  # apl-source:19
  ن = len(مصفوفة)
  # apl-source:20
  مرئي = [False] * ن
  # apl-source:21
  طابور = [بداية]
  # apl-source:22
  مرئي[بداية] = True
  # apl-source:23
  ع = 0
  # apl-source:24
  while ع < len(طابور):
    # apl-source:25
    ق = طابور[ع]
    # apl-source:26
    ع = ع + 1
    # apl-source:27
    if مصفوفة[ق] == 0:
      # apl-source:28
      return True
    # apl-source:29
    for ن_ in [ق + مصفوفة[ق], ق - مصفوفة[ق]]:
      # apl-source:30
      if (ن_ >= 0) and (ن_ < ن):
        # apl-source:31
        if not مرئي[ن_]:
          # apl-source:32
          مرئي[ن_] = True
          # apl-source:33
          طابور = طابور + [ن_]
  # apl-source:34
  return False
# apl-source:35

# apl-source:36
تأكد_يساوي(يصل_صفر([4,2,3,0,3,1,2], 5), True, "ممكن")
# apl-source:37
تأكد_يساوي(يصل_صفر([3,0,2,1,2], 2), False, "غير ممكن")
# apl-source:38
تأكد_يساوي(يصل_صفر([0], 0), True, "في البداية")
# apl-source:39
