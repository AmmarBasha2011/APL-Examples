
# apl-source:1
# مثال 710 — بحث A* على شبكة
# apl-source:2
# A* grid search
# apl-source:3
# Demonstrates: استدلال مانهاتن، طابور أولوية، جدران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/710-astar-grid.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# بحث A* على شبكة بجدران
# apl-source:25
# Demonstrates: كلفة + استدلال مانهاتن, طابور أولوية مصغر, إعادة بناء المسار
# apl-source:26
# شبكة 5×5 بجدار عمودي يفتح عند الأسفل
# apl-source:27

# apl-source:28
def مانهاتن(أ, ب):
  # apl-source:29
  فرق1 = أ[0] - ب[0]
  # apl-source:30
  if فرق1 < 0:
    # apl-source:31
    فرق1 = -فرق1
  # apl-source:32
  فرق2 = أ[1] - ب[1]
  # apl-source:33
  if فرق2 < 0:
    # apl-source:34
    فرق2 = -فرق2
  # apl-source:35
  return فرق1 + فرق2
# apl-source:36

# apl-source:37
def نجمة(شبكة, صفوف, أعمدة, بدء, هدف):
  # apl-source:38
  مفتوح = [[مانهاتن(بدء, هدف), 0, بدء, []]]
  # apl-source:39
  مغلق = []
  # apl-source:40
  while len(مفتوح) > 0:
    # apl-source:41
    أفضل = 0
    # apl-source:42
    for ي in range(1, len(مفتوح)):
      # apl-source:43
      if مفتوح[ي][0] < مفتوح[أفضل][0]:
        # apl-source:44
        أفضل = ي
    # apl-source:45
    عنصر = مفتوح[أفضل]
    # apl-source:46
    مفتوح = مفتوح[:أفضل] + مفتوح[أفضل + 1:]
    # apl-source:47
    موضع = عنصر[2]
    # apl-source:48
    كلفة = عنصر[1]
    # apl-source:49
    مسار = عنصر[3] + [موضع]
    # apl-source:50
    if موضع == هدف:
      # apl-source:51
      return مسار
    # apl-source:52
    if موضع in مغلق:
      # apl-source:53
      موضع = موضع
    # apl-source:54
    else:
      # apl-source:55
      مغلق.append(موضع)
      # apl-source:56
      حركات = [[-1, 0], [1, 0], [0, -1], [0, 1]]
      # apl-source:57
      for ح in حركات:
        # apl-source:58
        ص = موضع[0] + ح[0]
        # apl-source:59
        ع = موضع[1] + ح[1]
        # apl-source:60
        if ص >= 0 and ص < صفوف and ع >= 0 and ع < أعمدة and شبكة[ص][ع] == 0:
          # apl-source:61
          if ([ص, ع] in مغلق) == False:
            # apl-source:62
            ك2 = كلفة + 1
            # apl-source:63
            مفتوح.append([ك2 + مانهاتن([ص, ع], هدف), ك2, [ص, ع], مسار])
  # apl-source:64
  return []
# apl-source:65

# apl-source:66
شبكة = [
  # apl-source:67
  [0, 0, 1, 0, 0],
  # apl-source:68
  [0, 0, 1, 0, 0],
  # apl-source:69
  [0, 0, 1, 0, 0],
  # apl-source:70
  [0, 0, 1, 0, 0],
  # apl-source:71
  [0, 0, 0, 0, 0]
# apl-source:72
]
# apl-source:73
مسار = نجمة(شبكة, 5, 5, [0, 0], [0, 4])
# apl-source:74
تأكد_يساوي(len(مسار), 13, "المسار يلتف حول الجدار في 13 خانة")
# apl-source:75
تأكد_يساوي(مسار[0], [0, 0], "البداية")
# apl-source:76
تأكد_يساوي(مسار[12], [0, 4], "النهاية")
# apl-source:77
تأكد_يساوي([4, 2] in مسار, True, "يمر بفتحة الجدار")
# apl-source:78
مستقيم = نجمة([[0, 0, 0]], 1, 3, [0, 0], [0, 2])
# apl-source:79
تأكد_يساوي(len(مستقيم), 3, "مسار مستقيم")
# apl-source:80
مسدود = نجمة([[0, 1, 0]], 1, 3, [0, 0], [0, 2])
# apl-source:81
تأكد_يساوي(مسدود, [], "لا مسار")
# apl-source:82
print("طول المسار:", len(مسار))
# apl-source:83
