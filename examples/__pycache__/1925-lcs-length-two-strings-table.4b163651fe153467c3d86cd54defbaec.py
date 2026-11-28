
# apl-source:1
# مثال 1925 — طول أطول تتابع مشترك
# apl-source:2
# Longest common subsequence length
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1925-lcs-length-two-strings-table.apl
# apl-source:6

# apl-source:7
# الخلية (ي،ك) تخص أول ي حرفا وأول ك حرفا
# apl-source:8
# إن تطابق الحرفان نزيد القيمة القطرية
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
def تتابع(أ, ب):
  # apl-source:19
  ج = []
  # apl-source:20
  for ي in range(len(أ) + 1):
    # apl-source:21
    صف = []
    # apl-source:22
    for ك in range(len(ب) + 1):
      # apl-source:23
      صف = صف + [0]
    # apl-source:24
    ج = ج + [صف]
  # apl-source:25
  for ي in range(1, len(أ) + 1):
    # apl-source:26
    for ك in range(1, len(ب) + 1):
      # apl-source:27
      if أ[ي - 1] == ب[ك - 1]:
        # apl-source:28
        ج[ي][ك] = ج[ي - 1][ك - 1] + 1
      # apl-source:29
      else:
        # apl-source:30
        ج[ي][ك] = max(ج[ي - 1][ك], ج[ي][ك - 1])
  # apl-source:31
  return ج[len(أ)][len(ب)]
# apl-source:32

# apl-source:33
تأكد_يساوي(تتابع("abcde", "ace"), 3, "ace")
# apl-source:34
تأكد_يساوي(تتابع("abc", "def"), 0, "لا اشتراك")
# apl-source:35
تأكد_يساوي(تتابع("AGGTAB", "GXTXAYB"), 4, "GTAB")
# apl-source:36
