
# apl-source:1
# مثال 2039 — أطول نص فرعي بلا تكرار
# apl-source:2
# Longest substring without repeats
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2039-longest-unique-substring-last-seen.apl
# apl-source:6

# apl-source:7
# # إن تكرر حرف داخل النافذة ننقل البداية بعد موضعه السابق
# apl-source:8
# # ونحدث أكبر طول
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
def اطول(س):
  # apl-source:19
  اخر = {}
  # apl-source:20
  بداية = 0
  # apl-source:21
  افضل = 0
  # apl-source:22
  for ك in range(len(س)):
    # apl-source:23
    if س[ك] in اخر and اخر[س[ك]] >= بداية:
      # apl-source:24
      بداية = اخر[س[ك]] + 1
    # apl-source:25
    اخر[س[ك]] = ك
    # apl-source:26
    افضل = max(افضل, ك - بداية + 1)
  # apl-source:27
  return افضل
# apl-source:28

# apl-source:29
تأكد_يساوي(اطول("abcabcbb"), 3, "abc")
# apl-source:30
تأكد_يساوي(اطول("bbbbb"), 1, "b")
# apl-source:31
تأكد_يساوي(اطول("pwwkew"), 3, "wke")
# apl-source:32
تأكد_يساوي(اطول(""), 0, "فارغ")
# apl-source:33
