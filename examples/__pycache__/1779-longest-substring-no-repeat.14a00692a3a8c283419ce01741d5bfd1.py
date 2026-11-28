
# apl-source:1
# مثال 1779 — أطول جزء بلا تكرار
# apl-source:2
# Longest substring without repeats
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1779-longest-substring-no-repeat.apl
# apl-source:6

# apl-source:7
# قاموس لآخر موضع لكل حرف
# apl-source:8
# ننقل بداية النافذة عند التكرار
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
def أطول_فريد(س):
  # apl-source:19
  آخر = {}
  # apl-source:20
  بداية = 0
  # apl-source:21
  أفضل = 0
  # apl-source:22
  for ك in range(len(س)):
    # apl-source:23
    ح = س[ك]
    # apl-source:24
    if ح in آخر:
      # apl-source:25
      if آخر[ح] >= بداية:
        # apl-source:26
        بداية = آخر[ح] + 1
    # apl-source:27
    آخر[ح] = ك
    # apl-source:28
    أفضل = max(أفضل, ك - بداية + 1)
  # apl-source:29
  return أفضل
# apl-source:30

# apl-source:31
تأكد_يساوي(أطول_فريد("abcabcbb"), 3, "ثلاثة")
# apl-source:32
تأكد_يساوي(أطول_فريد("bbbb"), 1, "واحد")
# apl-source:33
تأكد_يساوي(أطول_فريد("pwwkew"), 3, "ثلاثة أخرى")
# apl-source:34
تأكد_يساوي(أطول_فريد(""), 0, "فارغ")
# apl-source:35
