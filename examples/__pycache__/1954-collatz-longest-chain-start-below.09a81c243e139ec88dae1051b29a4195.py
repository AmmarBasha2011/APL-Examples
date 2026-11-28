
# apl-source:1
# مثال 1954 — أطول سلسلة كولاتز تحت حد
# apl-source:2
# Longest Collatz chain below limit
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1954-collatz-longest-chain-start-below.apl
# apl-source:6

# apl-source:7
# # نذكر طول السلسلة لكل عدد في قاموس
# apl-source:8
# # ونبحث عن أكبر طول بين 1 وحد
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
def طول_سلسلة(ن, ذاكرة):
  # apl-source:19
  مسار = []
  # apl-source:20
  while (ن in ذاكرة) == False:
    # apl-source:21
    مسار = مسار + [ن]
    # apl-source:22
    if ن % 2 == 0:
      # apl-source:23
      ن = ن // 2
    # apl-source:24
    else:
      # apl-source:25
      ن = 3 * ن + 1
  # apl-source:26
  عدد = ذاكرة[ن]
  # apl-source:27
  for ك in range(len(مسار)):
    # apl-source:28
    عدد = عدد + 1
    # apl-source:29
    ذاكرة[مسار[len(مسار) - 1 - ك]] = عدد
  # apl-source:30
  if len(مسار) > 0:
    # apl-source:31
    return ذاكرة[مسار[0]]
  # apl-source:32
  return ذاكرة[ن]
# apl-source:33

# apl-source:34
def افضل_بداية(حد):
  # apl-source:35
  ذاكرة = {}
  # apl-source:36
  ذاكرة[1] = 1
  # apl-source:37
  افضل = 1
  # apl-source:38
  اطول = 1
  # apl-source:39
  for ن in range(2, حد):
    # apl-source:40
    ط = طول_سلسلة(ن, ذاكرة)
    # apl-source:41
    if ط > اطول:
      # apl-source:42
      اطول = ط
      # apl-source:43
      افضل = ن
  # apl-source:44
  return [افضل, اطول]
# apl-source:45

# apl-source:46
تأكد_يساوي(افضل_بداية(10), [9, 20], "تحت عشرة")
# apl-source:47
تأكد_يساوي(افضل_بداية(100), [97, 119], "تحت مئة")
# apl-source:48
تأكد_يساوي(افضل_بداية(1000), [871, 179], "تحت ألف")
# apl-source:49
