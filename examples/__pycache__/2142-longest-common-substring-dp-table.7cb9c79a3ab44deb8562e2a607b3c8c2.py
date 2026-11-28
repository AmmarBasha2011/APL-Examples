
# apl-source:1
# مثال 2142 — أطول نص فرعي مشترك
# apl-source:2
# Longest common substring DP
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2142-longest-common-substring-dp-table.apl
# apl-source:6

# apl-source:7
# # القيمة تعتمد على الخلية القطرية السابقة
# apl-source:8
# # نحتفظ بأكبر قيمة
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
def مشترك(ا, ب):
  # apl-source:19
  جدول = []
  # apl-source:20
  for ي in range(len(ا) + 1):
    # apl-source:21
    جدول = جدول + [[0] * (len(ب) + 1)]
  # apl-source:22
  افضل = 0
  # apl-source:23
  for ي in range(1, len(ا) + 1):
    # apl-source:24
    for ك in range(1, len(ب) + 1):
      # apl-source:25
      if ا[ي - 1] == ب[ك - 1]:
        # apl-source:26
        جدول[ي][ك] = جدول[ي - 1][ك - 1] + 1
        # apl-source:27
        افضل = max(افضل, جدول[ي][ك])
  # apl-source:28
  return افضل
# apl-source:29

# apl-source:30
تأكد_يساوي(مشترك("abcdxyz", "xyzabcd"), 4, "أربعة")
# apl-source:31
تأكد_يساوي(مشترك("abc", "def"), 0, "لا يوجد")
# apl-source:32
تأكد_يساوي(مشترك("zxabcdezy", "yzabcdezx"), 6, "ستة")
# apl-source:33
