
# apl-source:1
# مثال 1810 — أكثر حرف تكراراً
# apl-source:2
# Most common character
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1810-most-common-character-count.apl
# apl-source:6

# apl-source:7
# عند التعادل نأخذ الأول ظهوراً
# apl-source:8
# نمر بالنص مرتين
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
def أكثر_حرف(س):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ح in س:
    # apl-source:21
    عد[ح] = عد.get(ح, 0) + 1
  # apl-source:22
  أفضل = ""
  # apl-source:23
  أعلى = 0
  # apl-source:24
  for ح in س:
    # apl-source:25
    if عد[ح] > أعلى:
      # apl-source:26
      أعلى = عد[ح]
      # apl-source:27
      أفضل = ح
  # apl-source:28
  return أفضل
# apl-source:29

# apl-source:30
تأكد_يساوي(أكثر_حرف("abbcc"), "b", "تعادل")
# apl-source:31
تأكد_يساوي(أكثر_حرف("aaab"), "a", "الأكثر")
# apl-source:32
تأكد_يساوي(أكثر_حرف("z"), "z", "حرف")
# apl-source:33
