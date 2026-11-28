
# apl-source:1
# مثال 1368 — أقل حافلات
# apl-source:2
# Bus routes minimum buses
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1368-bus-routes-min.apl
# apl-source:6

# apl-source:7
# نربط كل محطة بخطوطها
# apl-source:8
# ونتوسع بالعرض خطاً خطاً
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
def اقل_حافلات(خطوط, مصدر, هدف):
  # apl-source:19
  if مصدر == هدف:
    # apl-source:20
    return 0
  # apl-source:21
  خطوط_المحطة = {}
  # apl-source:22
  for ر in range(len(خطوط)):
    # apl-source:23
    for م in خطوط[ر]:
      # apl-source:24
      if م not in خطوط_المحطة:
        # apl-source:25
        خطوط_المحطة[م] = []
      # apl-source:26
      خطوط_المحطة[م] = خطوط_المحطة[م] + [ر]
  # apl-source:27
  محطات_مرئية = {}
  # apl-source:28
  محطات_مرئية[مصدر] = True
  # apl-source:29
  خطوط_مرئية = {}
  # apl-source:30
  طابور = [[مصدر, 0]]
  # apl-source:31
  ع = 0
  # apl-source:32
  while ع < len(طابور):
    # apl-source:33
    محطة = طابور[ع][0]
    # apl-source:34
    حافلات = طابور[ع][1]
    # apl-source:35
    ع = ع + 1
    # apl-source:36
    for ر in خطوط_المحطة.get(محطة, []):
      # apl-source:37
      if not خطوط_مرئية.get(ر, False):
        # apl-source:38
        خطوط_مرئية[ر] = True
        # apl-source:39
        for م in خطوط[ر]:
          # apl-source:40
          if م == هدف:
            # apl-source:41
            return حافلات + 1
          # apl-source:42
          if not محطات_مرئية.get(م, False):
            # apl-source:43
            محطات_مرئية[م] = True
            # apl-source:44
            طابور = طابور + [[م, حافلات + 1]]
  # apl-source:45
  return -1
# apl-source:46

# apl-source:47
تأكد_يساوي(اقل_حافلات([[1,2,7],[3,6,7]], 1, 6), 2, "حافلتان")
# apl-source:48
تأكد_يساوي(اقل_حافلات([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12), -1, "لا وصول")
# apl-source:49
تأكد_يساوي(اقل_حافلات([[1,2]], 1, 1), 0, "نفس المحطة")
# apl-source:50
