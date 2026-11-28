
# apl-source:1
# مثال 1196 — جدران وبوابات
# apl-source:2
# Walls and gates distance fill
# apl-source:3
# Demonstrates: بحث بالعرض من عدة مصادر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1196-walls-and-gates.apl
# apl-source:6

# apl-source:7
# نبدأ بالعرض من كل البوابات معاً
# apl-source:8
# فتصل كل غرفة بأقصر مسافة
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
def املأ(ش):
  # apl-source:19
  ر_ = len(ش)
  # apl-source:20
  ك_ = len(ش[0])
  # apl-source:21
  كبير = 2147483647
  # apl-source:22
  طابور = []
  # apl-source:23
  for ص in range(ر_):
    # apl-source:24
    for ج in range(ك_):
      # apl-source:25
      if ش[ص][ج] == 0:
        # apl-source:26
        طابور = طابور + [[ص, ج]]
  # apl-source:27
  ع = 0
  # apl-source:28
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:29
  while ع < len(طابور):
    # apl-source:30
    ص = طابور[ع][0]
    # apl-source:31
    ج = طابور[ع][1]
    # apl-source:32
    ع = ع + 1
    # apl-source:33
    for د in اتجاهات:
      # apl-source:34
      ر = ص + د[0]
      # apl-source:35
      ك = ج + د[1]
      # apl-source:36
      if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
        # apl-source:37
        if ش[ر][ك] == كبير:
          # apl-source:38
          ش[ر][ك] = ش[ص][ج] + 1
          # apl-source:39
          طابور = طابور + [[ر, ك]]
  # apl-source:40
  return ش
# apl-source:41

# apl-source:42
ك = 2147483647
# apl-source:43
م = [[ك,-1,0,ك],[ك,ك,ك,-1],[ك,-1,ك,-1],[0,-1,ك,ك]]
# apl-source:44
تأكد_يساوي(املأ(م), [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]], "مثال أول")
# apl-source:45
تأكد_يساوي(املأ([[0]]), [[0]], "بوابة فقط")
# apl-source:46
