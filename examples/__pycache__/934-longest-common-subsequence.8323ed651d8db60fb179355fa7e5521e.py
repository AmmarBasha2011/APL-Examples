
# apl-source:1
# مثال 934 — أطول تتابع مشترك
# apl-source:2
# Longest common subsequence
# apl-source:3
# Demonstrates: جدول ثنائي متدرج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/934-longest-common-subsequence.apl
# apl-source:6

# apl-source:7
# أطول تتابع جزئي مشترك: برمجة ديناميكية ثنائية
# apl-source:8
# أساس diff ومواءمة التتابعات الحيوية
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
def أطول_مشترك(أ, ب):
  # apl-source:19
  ن = len(أ)
  # apl-source:20
  م = len(ب)
  # apl-source:21
  ع = []
  # apl-source:22
  for _ in range(ن + 1):
    # apl-source:23
    صف = []
    # apl-source:24
    for __ in range(م + 1):
      # apl-source:25
      صف = صف + [0]
    # apl-source:26
    ع = ع + [صف]
  # apl-source:27
  for i in range(1, ن + 1):
    # apl-source:28
    for ج in range(1, م + 1):
      # apl-source:29
      if أ[i - 1] == ب[ج - 1]:
        # apl-source:30
        ع[i][ج] = ع[i - 1][ج - 1] + 1
      # apl-source:31
      else:
        # apl-source:32
        أعلى = ع[i - 1][ج]
        # apl-source:33
        يسار = ع[i][ج - 1]
        # apl-source:34
        if أعلى >= يسار:
          # apl-source:35
          ع[i][ج] = أعلى
        # apl-source:36
        else:
          # apl-source:37
          ع[i][ج] = يسار
  # apl-source:38
  return ع[ن][م]
# apl-source:39

# apl-source:40
print("LCS(ABCBDAB, BDCABA) =", أطول_مشترك("ABCBDAB", "BDCABA"))
# apl-source:41

# apl-source:42
تأكد_يساوي(أطول_مشترك("ABCBDAB", "BDCABA"), 4, "المثال القياسي")
# apl-source:43
تأكد_يساوي(أطول_مشترك("abc", "abc"), 3, "تطابق تام")
# apl-source:44
تأكد_يساوي(أطول_مشترك("abc", "def"), 0, "لا مشترك")
# apl-source:45
تأكد_يساوي(أطول_مشترك("", "abc"), 0, "فارغ")
# apl-source:46
تأكد_يساوي(أطول_مشترك("AGGTAB", "GXTXAYB"), 4, "مثال ثانٍ")
# apl-source:47
