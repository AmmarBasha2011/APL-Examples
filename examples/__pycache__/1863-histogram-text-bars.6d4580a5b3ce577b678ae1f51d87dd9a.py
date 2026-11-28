
# apl-source:1
# مثال 1863 — مدرج نصي للأعداد
# apl-source:2
# Text histogram bars
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1863-histogram-text-bars.apl
# apl-source:6

# apl-source:7
# نكرر النجمة بقدر العدد
# apl-source:8
# نجمع الأسطر
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
def مدرج(ق):
  # apl-source:19
  أسطر = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    أسطر.append("*" * ع)
  # apl-source:22
  return "\n".join(أسطر)
# apl-source:23

# apl-source:24
تأكد_يساوي(مدرج([1, 3, 2]), "*\n***\n**", "ثلاثة")
# apl-source:25
تأكد_يساوي(مدرج([0]), "", "صفر")
# apl-source:26
تأكد_يساوي(مدرج([2]), "**", "واحد")
# apl-source:27
