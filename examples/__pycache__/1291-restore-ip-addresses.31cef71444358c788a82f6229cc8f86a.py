
# apl-source:1
# مثال 1291 — استعادة عناوين
# apl-source:2
# Restore IP addresses
# apl-source:3
# Demonstrates: حلقات متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1291-restore-ip-addresses.apl
# apl-source:6

# apl-source:7
# نجرب أربعة أجزاء كل منها بين صفر و255
# apl-source:8
# ولا يبدأ جزء متعدد الأرقام بصفر
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
def صالح_جزء(ج):
  # apl-source:19
  if (len(ج) == 0) or (len(ج) > 3):
    # apl-source:20
    return False
  # apl-source:21
  if (len(ج) > 1) and (ج[0] == "0"):
    # apl-source:22
    return False
  # apl-source:23
  return int(ج) <= 255
# apl-source:24

# apl-source:25
def عناوين(س):
  # apl-source:26
  ناتج = []
  # apl-source:27
  ن = len(س)
  # apl-source:28
  for ا in range(1, 4):
    # apl-source:29
    for ب in range(1, 4):
      # apl-source:30
      for ج in range(1, 4):
        # apl-source:31
        د = ن - ا - ب - ج
        # apl-source:32
        if (د >= 1) and (د <= 3):
          # apl-source:33
          ج1 = س[:ا]
          # apl-source:34
          ج2 = س[ا:ا + ب]
          # apl-source:35
          ج3 = س[ا + ب:ا + ب + ج]
          # apl-source:36
          ج4 = س[ا + ب + ج:]
          # apl-source:37
          ك1 = صالح_جزء(ج1)
          # apl-source:38
          ك2 = صالح_جزء(ج2)
          # apl-source:39
          ك3 = صالح_جزء(ج3)
          # apl-source:40
          ك4 = صالح_جزء(ج4)
          # apl-source:41
          if ك1 and ك2 and ك3 and ك4:
            # apl-source:42
            ناتج = ناتج + [ج1 + "." + ج2 + "." + ج3 + "." + ج4]
  # apl-source:43
  return ناتج
# apl-source:44

# apl-source:45
تأكد_يساوي(عناوين("25525511135"), ["255.255.11.135", "255.255.111.35"], "مثال أول")
# apl-source:46
تأكد_يساوي(عناوين("0000"), ["0.0.0.0"], "أصفار")
# apl-source:47
تأكد_يساوي(عناوين("101023"), ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"], "ست خانات")
# apl-source:48
تأكد_يساوي(عناوين("1111"), ["1.1.1.1"], "واحدات")
# apl-source:49
