
# apl-source:1
# مثال 1300 — عينة بالخزان
# apl-source:2
# Reservoir sampling with seeded generator
# apl-source:3
# Demonstrates: عينات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1300-reservoir-sampling-fixed.apl
# apl-source:6

# apl-source:7
# العنصر ذو الترتيب i يحل محل المختار باحتمال 1 على i
# apl-source:8
# نستخدم مولداً ثابت البذرة
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
class مولد_بسيط:
  # apl-source:19
  def __init__(ذات, بذرة):
    # apl-source:20
    ذات.ح = بذرة
# apl-source:21

  # apl-source:22
  def تالي(ذات):
    # apl-source:23
    ذات.ح = (ذات.ح * 1664525 + 1013904223) % 4294967296
    # apl-source:24
    return ذات.ح
# apl-source:25

# apl-source:26
def اختر_من_تدفق(تدفق, بذرة):
  # apl-source:27
  م = مولد_بسيط(بذرة)
  # apl-source:28
  مختار = 0
  # apl-source:29
  for ع in range(len(تدفق)):
    # apl-source:30
    if م.تالي() % (ع + 1) == 0:
      # apl-source:31
      مختار = تدفق[ع]
  # apl-source:32
  return مختار
# apl-source:33

# apl-source:34
ت = [10, 20, 30, 40, 50]
# apl-source:35
ن = اختر_من_تدفق(ت, 7)
# apl-source:36
تأكد_يساوي(ن in ت, True, "من التدفق")
# apl-source:37
تأكد_يساوي(اختر_من_تدفق(ت, 7), ن, "نفس البذرة")
# apl-source:38
تأكد_يساوي(اختر_من_تدفق([9], 1), 9, "عنصر واحد")
# apl-source:39
