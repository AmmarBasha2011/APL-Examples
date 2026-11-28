
# apl-source:1
# مثال 1349 — حالات آمنة
# apl-source:2
# Find eventual safe states
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1349-eventual-safe-states.apl
# apl-source:6

# apl-source:7
# نعكس الحواف ونطبق ترتيباً طوبولوجياً
# apl-source:8
# العقدة الآمنة لا تصل إلى دورة
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
def عقد_آمنة(رسم):
  # apl-source:19
  ن = len(رسم)
  # apl-source:20
  عكس = []
  # apl-source:21
  عدد_خارج = []
  # apl-source:22
  for ع in range(ن):
    # apl-source:23
    عكس = عكس + [[]]
    # apl-source:24
    عدد_خارج = عدد_خارج + [len(رسم[ع])]
  # apl-source:25
  for ع in range(ن):
    # apl-source:26
    for ج in رسم[ع]:
      # apl-source:27
      عكس[ج] = عكس[ج] + [ع]
  # apl-source:28
  طابور = []
  # apl-source:29
  for ع in range(ن):
    # apl-source:30
    if عدد_خارج[ع] == 0:
      # apl-source:31
      طابور = طابور + [ع]
  # apl-source:32
  آمنة = []
  # apl-source:33
  ك = 0
  # apl-source:34
  while ك < len(طابور):
    # apl-source:35
    ق = طابور[ك]
    # apl-source:36
    ك = ك + 1
    # apl-source:37
    آمنة = آمنة + [ق]
    # apl-source:38
    for س in عكس[ق]:
      # apl-source:39
      عدد_خارج[س] = عدد_خارج[س] - 1
      # apl-source:40
      if عدد_خارج[س] == 0:
        # apl-source:41
        طابور = طابور + [س]
  # apl-source:42
  return sorted(آمنة)
# apl-source:43

# apl-source:44
تأكد_يساوي(عقد_آمنة([[1,2],[2,3],[5],[0],[5],[],[]]), [2,4,5,6], "مثال أول")
# apl-source:45
تأكد_يساوي(عقد_آمنة([[1,2,3,4],[1,2],[3,4],[0,4],[]]), [4], "عقدة واحدة")
# apl-source:46
تأكد_يساوي(عقد_آمنة([[]]), [0], "طرفية")
# apl-source:47
