
# apl-source:1
# مثال 1063 — نص متشابك
# apl-source:2
# Interleaving string
# apl-source:3
# Demonstrates: جدول ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1063-interleaving-string.apl
# apl-source:6

# apl-source:7
# جدول يقول هل أول ي حرفاً من الأول وأول ك من الثاني تصنع بادئة الثالث
# apl-source:8
# كل خلية تعتمد على الخلية العليا واليسرى
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
def متشابك(أ, ب, ج):
  # apl-source:19
  if (len(أ) + len(ب)) != len(ج):
    # apl-source:20
    return False
  # apl-source:21
  د = []
  # apl-source:22
  for ي in range(len(أ) + 1):
    # apl-source:23
    د = د + [[False] * (len(ب) + 1)]
  # apl-source:24
  د[0][0] = True
  # apl-source:25
  for ي in range(len(أ) + 1):
    # apl-source:26
    for ك in range(len(ب) + 1):
      # apl-source:27
      if (ي > 0) and د[ي - 1][ك] and (أ[ي - 1] == ج[(ي + ك) - 1]):
        # apl-source:28
        د[ي][ك] = True
      # apl-source:29
      if (ك > 0) and د[ي][ك - 1] and (ب[ك - 1] == ج[(ي + ك) - 1]):
        # apl-source:30
        د[ي][ك] = True
  # apl-source:31
  return د[len(أ)][len(ب)]
# apl-source:32

# apl-source:33
تأكد_يساوي(متشابك("aabcc", "dbbca", "aadbbcbcac"), True, "ممكن")
# apl-source:34
تأكد_يساوي(متشابك("aabcc", "dbbca", "aadbbbaccc"), False, "غير ممكن")
# apl-source:35
تأكد_يساوي(متشابك("", "", ""), True, "فارغة")
# apl-source:36
تأكد_يساوي(متشابك("a", "", "c"), False, "حرف مختلف")
# apl-source:37
