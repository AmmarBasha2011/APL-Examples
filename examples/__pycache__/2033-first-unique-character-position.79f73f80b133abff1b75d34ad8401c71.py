
# apl-source:1
# مثال 2033 — موضع أول حرف غير مكرر
# apl-source:2
# First unique character index
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2033-first-unique-character-position.apl
# apl-source:6

# apl-source:7
# # المرور الأول للعد
# apl-source:8
# # والثاني لإيجاد الموضع
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
def اول_فريد(س):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ح in س:
    # apl-source:21
    عد[ح] = عد.get(ح, 0) + 1
  # apl-source:22
  for ك in range(len(س)):
    # apl-source:23
    if عد[س[ك]] == 1:
      # apl-source:24
      return ك
  # apl-source:25
  return -1
# apl-source:26

# apl-source:27
تأكد_يساوي(اول_فريد("leetcode"), 0, "الأول")
# apl-source:28
تأكد_يساوي(اول_فريد("loveleetcode"), 2, "الثالث")
# apl-source:29
تأكد_يساوي(اول_فريد("aabb"), -1, "لا يوجد")
# apl-source:30
