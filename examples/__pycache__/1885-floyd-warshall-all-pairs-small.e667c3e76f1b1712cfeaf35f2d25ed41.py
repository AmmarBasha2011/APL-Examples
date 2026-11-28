
# apl-source:1
# مثال 1885 — أقصر المسافات بين كل الأزواج
# apl-source:2
# Floyd Warshall all pairs
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1885-floyd-warshall-all-pairs-small.apl
# apl-source:6

# apl-source:7
# مصفوفة المسافات المبدئية
# apl-source:8
# نحدثها بكل وسيط
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
def فلويد(م):
  # apl-source:19
  ن = len(م)
  # apl-source:20
  د = []
  # apl-source:21
  for ص in م:
    # apl-source:22
    د.append(ص + [])
  # apl-source:23
  for و_ك in range(ن):
    # apl-source:24
    for ي in range(ن):
      # apl-source:25
      for ج in range(ن):
        # apl-source:26
        if د[ي][و_ك] + د[و_ك][ج] < د[ي][ج]:
          # apl-source:27
          د[ي][ج] = د[ي][و_ك] + د[و_ك][ج]
  # apl-source:28
  return د
# apl-source:29

# apl-source:30
ك = 1000
# apl-source:31
م = [[0, 3, ك], [ك, 0, 1], [2, ك, 0]]
# apl-source:32
ن = فلويد(م)
# apl-source:33
تأكد_يساوي(ن[0][2], 4, "عبر عقدة")
# apl-source:34
تأكد_يساوي(ن[1][0], 3, "دورة")
# apl-source:35
تأكد_يساوي(ن[2][1], 5, "طويل")
# apl-source:36
