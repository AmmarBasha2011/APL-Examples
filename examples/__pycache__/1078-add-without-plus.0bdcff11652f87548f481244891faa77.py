
# apl-source:1
# مثال 1078 — جمع بلا علامة الجمع
# apl-source:2
# Add two integers using bit operations
# apl-source:3
# Demonstrates: XOR وحمل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1078-add-without-plus.apl
# apl-source:6

# apl-source:7
# XOR يجمع البتات بلا حمل و AND مزاحاً بتاً واحداً يعطي الحمل
# apl-source:8
# نكرر حتى ينتهي الحمل
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
def اجمع_بتات(أ, ب):
  # apl-source:19
  while ب > 0:
    # apl-source:20
    حمل = (أ & ب) << 1
    # apl-source:21
    أ = أ ^ ب
    # apl-source:22
    ب = حمل
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
تأكد_يساوي(اجمع_بتات(5, 7), 12, "خمسة وسبعة")
# apl-source:26
تأكد_يساوي(اجمع_بتات(0, 9), 9, "صفر")
# apl-source:27
تأكد_يساوي(اجمع_بتات(123, 456), 579, "أكبر")
# apl-source:28
تأكد_يساوي(اجمع_بتات(1023, 1), 1024, "حمل ممتد")
# apl-source:29
