
# apl-source:1
# مثال 1987 — جمع الاسم الإنجليزي حسب العدد
# apl-source:2
# Pluralize noun by count
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1987-pluralize-count-with-noun-rules.apl
# apl-source:6

# apl-source:7
# # العدد 1 يبقى مفردا
# apl-source:8
# # وغير ذلك نطبق القاعدة
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
def جمع(ن, اسم):
  # apl-source:19
  if ن == 1:
    # apl-source:20
    return "1 " + اسم
  # apl-source:21
  if اسم.endswith("y"):
    # apl-source:22
    ج = اسم[:-1] + "ies"
  # apl-source:23
  elif اسم.endswith("s"):
    # apl-source:24
    ج = اسم + "es"
  # apl-source:25
  else:
    # apl-source:26
    ج = اسم + "s"
  # apl-source:27
  return str(ن) + " " + ج
# apl-source:28

# apl-source:29
تأكد_يساوي(جمع(1, "city"), "1 city", "مفرد")
# apl-source:30
تأكد_يساوي(جمع(2, "city"), "2 cities", "y")
# apl-source:31
تأكد_يساوي(جمع(2, "bus"), "2 buses", "s")
# apl-source:32
تأكد_يساوي(جمع(0, "file"), "0 files", "صفر")
# apl-source:33
