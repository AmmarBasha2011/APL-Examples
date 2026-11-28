
# apl-source:1
# مثال 1780 — أقصر نافذة بمجموع كاف
# apl-source:2
# Shortest subarray with sum at least target
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1780-min-window-sum-at-least.apl
# apl-source:6

# apl-source:7
# نمدد اليمين حتى يكفي المجموع
# apl-source:8
# ثم نقلص اليسار
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
def أقصر_نافذة(ق, هدف):
  # apl-source:19
  يسار = 0
  # apl-source:20
  مجموع = 0
  # apl-source:21
  أفضل = len(ق) + 1
  # apl-source:22
  for يمين in range(len(ق)):
    # apl-source:23
    مجموع = مجموع + ق[يمين]
    # apl-source:24
    while مجموع >= هدف:
      # apl-source:25
      أفضل = min(أفضل, يمين - يسار + 1)
      # apl-source:26
      مجموع = مجموع - ق[يسار]
      # apl-source:27
      يسار = يسار + 1
  # apl-source:28
  if أفضل > len(ق):
    # apl-source:29
    return 0
  # apl-source:30
  return أفضل
# apl-source:31

# apl-source:32
تأكد_يساوي(أقصر_نافذة([2, 3, 1, 2, 4, 3], 7), 2, "اثنان")
# apl-source:33
تأكد_يساوي(أقصر_نافذة([1, 1, 1], 10), 0, "لا تكفي")
# apl-source:34
تأكد_يساوي(أقصر_نافذة([5], 5), 1, "واحد")
# apl-source:35
