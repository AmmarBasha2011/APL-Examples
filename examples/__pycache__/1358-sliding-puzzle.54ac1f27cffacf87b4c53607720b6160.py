
# apl-source:1
# مثال 1358 — لغز الانزلاق
# apl-source:2
# Sliding puzzle 2x3
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1358-sliding-puzzle.apl
# apl-source:6

# apl-source:7
# الحالة نص من ستة أرقام
# apl-source:8
# نبدل الصفر مع جاره ونبحث بالعرض
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
def اقل_حركات(بداية):
  # apl-source:19
  هدف = "123450"
  # apl-source:20
  جيران = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
  # apl-source:21
  مرئي = {}
  # apl-source:22
  مرئي[بداية] = True
  # apl-source:23
  طابور = [[بداية, 0]]
  # apl-source:24
  ع = 0
  # apl-source:25
  while ع < len(طابور):
    # apl-source:26
    حالة = طابور[ع][0]
    # apl-source:27
    خطوات = طابور[ع][1]
    # apl-source:28
    ع = ع + 1
    # apl-source:29
    if حالة == هدف:
      # apl-source:30
      return خطوات
    # apl-source:31
    ص = حالة.find("0")
    # apl-source:32
    for ج in جيران[ص]:
      # apl-source:33
      حروف = list(حالة)
      # apl-source:34
      حروف[ص] = حروف[ج]
      # apl-source:35
      حروف[ج] = "0"
      # apl-source:36
      جديد = ""
      # apl-source:37
      for ح in حروف:
        # apl-source:38
        جديد = جديد + ح
      # apl-source:39
      if جديد not in مرئي:
        # apl-source:40
        مرئي[جديد] = True
        # apl-source:41
        طابور = طابور + [[جديد, خطوات + 1]]
  # apl-source:42
  return -1
# apl-source:43

# apl-source:44
تأكد_يساوي(اقل_حركات("123405"), 1, "حركة واحدة")
# apl-source:45
تأكد_يساوي(اقل_حركات("123540"), -1, "غير قابل للحل")
# apl-source:46
تأكد_يساوي(اقل_حركات("412503"), 5, "خمس حركات")
# apl-source:47
