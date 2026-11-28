
# apl-source:1
# مثال 1062 — أطول تتابع متناظر
# apl-source:2
# Longest palindromic subsequence
# apl-source:3
# Demonstrates: جدول مجالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1062-longest-palindromic-subseq.apl
# apl-source:6

# apl-source:7
# أطول تتابع متناظر في نص بين موضعين
# apl-source:8
# إما يضيف الحرفين المتطابقين الطرفيين أو يتجاهل أحدهما
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
def اطول_تتابع(نص_):
  # apl-source:19
  ن = len(نص_)
  # apl-source:20
  د = []
  # apl-source:21
  for ر in range(ن):
    # apl-source:22
    د = د + [[0] * ن]
  # apl-source:23
  for ي in range(ن - 1, -1, -1):
    # apl-source:24
    د[ي][ي] = 1
    # apl-source:25
    for ل in range(ي + 1, ن):
      # apl-source:26
      if نص_[ي] == نص_[ل]:
        # apl-source:27
        د[ي][ل] = د[ي + 1][ل - 1] + 2
      # apl-source:28
      else:
        # apl-source:29
        د[ي][ل] = د[ي + 1][ل]
        # apl-source:30
        if د[ي][ل - 1] > د[ي][ل]:
          # apl-source:31
          د[ي][ل] = د[ي][ل - 1]
  # apl-source:32
  return د[0][ن - 1]
# apl-source:33

# apl-source:34
تأكد_يساوي(اطول_تتابع("bbbab"), 4, "bbbb")
# apl-source:35
تأكد_يساوي(اطول_تتابع("cbbd"), 2, "bb")
# apl-source:36
تأكد_يساوي(اطول_تتابع("a"), 1, "حرف")
# apl-source:37
تأكد_يساوي(اطول_تتابع("abcde"), 1, "بلا تكرار")
# apl-source:38
