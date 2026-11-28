
# apl-source:1
# مثال 1030 — أطول نص بلا تكرار
# apl-source:2
# Longest substring without repeating characters
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1030-longest-no-repeat.apl
# apl-source:6

# apl-source:7
# نافذة تتسع يميناً وتنكمش يساراً عند ظهور حرف مكرر
# apl-source:8
# نحفظ أكبر عرض مر بها
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
def اطول_بلا_تكرار(نص_):
  # apl-source:19
  بداية = 0
  # apl-source:20
  افضل = 0
  # apl-source:21
  for ع in range(len(نص_)):
    # apl-source:22
    for ك in range(بداية, ع):
      # apl-source:23
      if نص_[ك] == نص_[ع]:
        # apl-source:24
        بداية = ك + 1
    # apl-source:25
    if ((ع - بداية) + 1) > افضل:
      # apl-source:26
      افضل = (ع - بداية) + 1
  # apl-source:27
  return افضل
# apl-source:28

# apl-source:29
تأكد_يساوي(اطول_بلا_تكرار("abcabcbb"), 3, "abc")
# apl-source:30
تأكد_يساوي(اطول_بلا_تكرار("bbbbb"), 1, "حرف واحد")
# apl-source:31
تأكد_يساوي(اطول_بلا_تكرار("pwwkew"), 3, "wke")
# apl-source:32
تأكد_يساوي(اطول_بلا_تكرار(""), 0, "فارغ")
# apl-source:33
