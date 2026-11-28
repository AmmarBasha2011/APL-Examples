
# apl-source:1
# مثال 1195 — برتقال عفن
# apl-source:2
# Rotting oranges
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1195-rotting-oranges.apl
# apl-source:6

# apl-source:7
# كل دقيقة يعفن جيران العفن الأربعة
# apl-source:8
# نمشي بالعرض من كل برتقالة فاسدة
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
def دقائق(ش):
  # apl-source:19
  ص_ = len(ش)
  # apl-source:20
  ج_ = len(ش[0])
  # apl-source:21
  طابور = []
  # apl-source:22
  طازج = 0
  # apl-source:23
  for ص in range(ص_):
    # apl-source:24
    for ج in range(ج_):
      # apl-source:25
      if ش[ص][ج] == 2:
        # apl-source:26
        طابور = طابور + [[ص, ج, 0]]
      # apl-source:27
      elif ش[ص][ج] == 1:
        # apl-source:28
        طازج = طازج + 1
  # apl-source:29
  ع = 0
  # apl-source:30
  وقت = 0
  # apl-source:31
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:32
  while ع < len(طابور):
    # apl-source:33
    ص = طابور[ع][0]
    # apl-source:34
    ج = طابور[ع][1]
    # apl-source:35
    وقت = طابور[ع][2]
    # apl-source:36
    ع = ع + 1
    # apl-source:37
    for د in اتجاهات:
      # apl-source:38
      ر = ص + د[0]
      # apl-source:39
      ك = ج + د[1]
      # apl-source:40
      if (ر >= 0) and (ر < ص_) and (ك >= 0) and (ك < ج_):
        # apl-source:41
        if ش[ر][ك] == 1:
          # apl-source:42
          ش[ر][ك] = 2
          # apl-source:43
          طازج = طازج - 1
          # apl-source:44
          طابور = طابور + [[ر, ك, وقت + 1]]
  # apl-source:45
  if طازج > 0:
    # apl-source:46
    return -1
  # apl-source:47
  return وقت
# apl-source:48

# apl-source:49
تأكد_يساوي(دقائق([[2,1,1],[1,1,0],[0,1,1]]), 4, "مثال أول")
# apl-source:50
تأكد_يساوي(دقائق([[2,1,1],[0,1,1],[1,0,1]]), -1, "معزولة")
# apl-source:51
تأكد_يساوي(دقائق([[0,2]]), 0, "لا طازج")
# apl-source:52
تأكد_يساوي(دقائق([[1]]), -1, "طازجة فقط")
# apl-source:53
