
# apl-source:1
# مثال 1069 — أطول نص متناظر ممكن
# apl-source:2
# Longest palindrome that can be built
# apl-source:3
# Demonstrates: عد الأزواج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1069-longest-palindrome-build.apl
# apl-source:6

# apl-source:7
# كل حرف يساهم بأزواجه في الطرفين
# apl-source:8
# ولو بقي حرف فرد واحد وضع في الوسط
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
def اطول_بناء(نص_):
  # apl-source:19
  فريدة = []
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح not in فريدة:
      # apl-source:22
      فريدة = فريدة + [ح]
  # apl-source:23
  طول_ = 0
  # apl-source:24
  فرد = False
  # apl-source:25
  for ح in فريدة:
    # apl-source:26
    عد_ح = 0
    # apl-source:27
    for خ in نص_:
      # apl-source:28
      if خ == ح:
        # apl-source:29
        عد_ح = عد_ح + 1
    # apl-source:30
    طول_ = طول_ + ((عد_ح // 2) * 2)
    # apl-source:31
    if (عد_ح % 2) == 1:
      # apl-source:32
      فرد = True
  # apl-source:33
  if فرد:
    # apl-source:34
    طول_ = طول_ + 1
  # apl-source:35
  return طول_
# apl-source:36

# apl-source:37
تأكد_يساوي(اطول_بناء("abccccdd"), 7, "dccaccd")
# apl-source:38
تأكد_يساوي(اطول_بناء("a"), 1, "حرف")
# apl-source:39
تأكد_يساوي(اطول_بناء("aaaaaa"), 6, "كله أزواج")
# apl-source:40
تأكد_يساوي(اطول_بناء("ab"), 1, "حرفان")
# apl-source:41
