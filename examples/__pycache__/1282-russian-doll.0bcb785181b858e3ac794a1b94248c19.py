
# apl-source:1
# مثال 1282 — دمى روسية
# apl-source:2
# Russian doll envelopes
# apl-source:3
# Demonstrates: أطول متتالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1282-russian-doll.apl
# apl-source:6

# apl-source:7
# نرتب بالعرض تصاعدياً وبالارتفاع تنازلياً
# apl-source:8
# ثم نحسب أطول متتالية متزايدة في الارتفاع
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
def اطول_متزايدة(أ):
  # apl-source:19
  ذيول = []
  # apl-source:20
  for س in أ:
    # apl-source:21
    ي = 0
    # apl-source:22
    ن = len(ذيول)
    # apl-source:23
    while ي < ن:
      # apl-source:24
      م = (ي + ن) // 2
      # apl-source:25
      if ذيول[م] < س:
        # apl-source:26
        ي = م + 1
      # apl-source:27
      else:
        # apl-source:28
        ن = م
    # apl-source:29
    if ي == len(ذيول):
      # apl-source:30
      ذيول = ذيول + [س]
    # apl-source:31
    else:
      # apl-source:32
      ذيول[ي] = س
  # apl-source:33
  return len(ذيول)
# apl-source:34

# apl-source:35
def مظاريف(م):
  # apl-source:36
  ازواج = []
  # apl-source:37
  for ز in م:
    # apl-source:38
    ازواج = ازواج + [[ز[0], -ز[1]]]
  # apl-source:39
  ازواج = sorted(ازواج)
  # apl-source:40
  ارتفاعات = []
  # apl-source:41
  for ز in ازواج:
    # apl-source:42
    ارتفاعات = ارتفاعات + [-ز[1]]
  # apl-source:43
  return اطول_متزايدة(ارتفاعات)
# apl-source:44

# apl-source:45
تأكد_يساوي(مظاريف([[5,4],[6,4],[6,7],[2,3]]), 3, "مثال أول")
# apl-source:46
تأكد_يساوي(مظاريف([[1,1],[1,1],[1,1]]), 1, "متطابقة")
# apl-source:47
تأكد_يساوي(مظاريف([]), 0, "فارغة")
# apl-source:48
