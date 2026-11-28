
# apl-source:1
# مثال 1061 — أقل قطع للتناظر
# apl-source:2
# Palindrome partitioning minimum cuts
# apl-source:3
# Demonstrates: جدول تناظر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1061-min-cuts-palindrome.apl
# apl-source:6

# apl-source:7
# نبني أولاً جدولاً يقول هل كل جزء من النص متناظر
# apl-source:8
# ثم نحسب أقل قطع لكل بادئة
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
def اقل_قطع(نص_):
  # apl-source:19
  ن = len(نص_)
  # apl-source:20
  تناظر = []
  # apl-source:21
  for ر in range(ن):
    # apl-source:22
    تناظر = تناظر + [[False] * ن]
  # apl-source:23
  for نهاية in range(ن):
    # apl-source:24
    for بداية in range(نهاية + 1):
      # apl-source:25
      if نص_[بداية] == نص_[نهاية]:
        # apl-source:26
        if ((نهاية - بداية) < 2) or تناظر[بداية + 1][نهاية - 1]:
          # apl-source:27
          تناظر[بداية][نهاية] = True
  # apl-source:28
  قطع = [0] * ن
  # apl-source:29
  for نهاية in range(ن):
    # apl-source:30
    if تناظر[0][نهاية]:
      # apl-source:31
      قطع[نهاية] = 0
    # apl-source:32
    else:
      # apl-source:33
      قطع[نهاية] = نهاية
      # apl-source:34
      for بداية in range(1, نهاية + 1):
        # apl-source:35
        if تناظر[بداية][نهاية] and ((قطع[بداية - 1] + 1) < قطع[نهاية]):
          # apl-source:36
          قطع[نهاية] = قطع[بداية - 1] + 1
  # apl-source:37
  return قطع[ن - 1]
# apl-source:38

# apl-source:39
تأكد_يساوي(اقل_قطع("aab"), 1, "aab")
# apl-source:40
تأكد_يساوي(اقل_قطع("a"), 0, "حرف")
# apl-source:41
تأكد_يساوي(اقل_قطع("ab"), 1, "ab")
# apl-source:42
تأكد_يساوي(اقل_قطع("racecar"), 0, "متناظر كله")
# apl-source:43
تأكد_يساوي(اقل_قطع("abccbc"), 2, "abccbc")
# apl-source:44
