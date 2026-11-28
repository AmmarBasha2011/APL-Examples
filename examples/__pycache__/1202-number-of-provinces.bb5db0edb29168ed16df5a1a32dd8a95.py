
# apl-source:1
# مثال 1202 — عدد المقاطعات
# apl-source:2
# Number of provinces
# apl-source:3
# Demonstrates: اتحاد وبحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1202-number-of-provinces.apl
# apl-source:6

# apl-source:7
# نوحد كل مدينتين متصلتين
# apl-source:8
# وعدد الجذور المختلفة هو عدد المقاطعات
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
def جذر(اب, س):
  # apl-source:19
  while اب[س] != س:
    # apl-source:20
    اب[س] = اب[اب[س]]
    # apl-source:21
    س = اب[س]
  # apl-source:22
  return س
# apl-source:23

# apl-source:24
def مقاطعات(م):
  # apl-source:25
  ن = len(م)
  # apl-source:26
  اب = list(range(ن))
  # apl-source:27
  for ع in range(ن):
    # apl-source:28
    for ج in range(ع + 1, ن):
      # apl-source:29
      if م[ع][ج] == 1:
        # apl-source:30
        اب[جذر(اب, ع)] = جذر(اب, ج)
  # apl-source:31
  جذور = []
  # apl-source:32
  for ع in range(ن):
    # apl-source:33
    ر = جذر(اب, ع)
    # apl-source:34
    if ر not in جذور:
      # apl-source:35
      جذور = جذور + [ر]
  # apl-source:36
  return len(جذور)
# apl-source:37

# apl-source:38
تأكد_يساوي(مقاطعات([[1,1,0],[1,1,0],[0,0,1]]), 2, "اثنتان")
# apl-source:39
تأكد_يساوي(مقاطعات([[1,0,0],[0,1,0],[0,0,1]]), 3, "منفصلة")
# apl-source:40
تأكد_يساوي(مقاطعات([[1,1,1],[1,1,1],[1,1,1]]), 1, "كلها متصلة")
# apl-source:41
