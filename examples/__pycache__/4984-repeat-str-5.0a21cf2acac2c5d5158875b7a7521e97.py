
# apl-source:1
# مثال 4984 — تكرار النص 5 مرات بفاصل
# apl-source:2
# Repeat text 5 times with separator
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4984-repeat-str-5.apl
# apl-source:6

# apl-source:7
# نبني النص بحلقة
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  ر = []
  # apl-source:19
  for ي in range(5):
    # apl-source:20
    ر = ر + [ن]
  # apl-source:21
  return "-".join(ر)
# apl-source:22

# apl-source:23
تأكد_يساوي(ف("a"), "a-a-a-a-a", "حالة 1")
# apl-source:24
تأكد_يساوي(ف("xy"), "xy-xy-xy-xy-xy", "حالة 2")
# apl-source:25
تأكد_يساوي(ف(""), "----", "حالة 3")
# apl-source:26
