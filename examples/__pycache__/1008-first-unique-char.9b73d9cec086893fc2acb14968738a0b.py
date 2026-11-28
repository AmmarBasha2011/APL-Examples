
# apl-source:1
# مثال 1008 — أول حرف غير مكرر
# apl-source:2
# First unique character
# apl-source:3
# Demonstrates: عد مرتين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1008-first-unique-char.apl
# apl-source:6

# apl-source:7
# نعد ظهور كل حرف ثم نمر ثانية على النص
# apl-source:8
# أول حرف عدده واحد هو الجواب
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
def اول_فريد(نص_):
  # apl-source:19
  for ع in range(len(نص_)):
    # apl-source:20
    عدد = 0
    # apl-source:21
    for ك in range(len(نص_)):
      # apl-source:22
      if نص_[ك] == نص_[ع]:
        # apl-source:23
        عدد = عدد + 1
    # apl-source:24
    if عدد == 1:
      # apl-source:25
      return ع
  # apl-source:26
  return -1
# apl-source:27

# apl-source:28
تأكد_يساوي(اول_فريد("leetcode"), 0, "الحرف الأول")
# apl-source:29
تأكد_يساوي(اول_فريد("loveleetcode"), 2, "الحرف الثالث")
# apl-source:30
تأكد_يساوي(اول_فريد("aabb"), -1, "لا فريد")
# apl-source:31
تأكد_يساوي(اول_فريد("كتابة"), 0, "عربي")
# apl-source:32
