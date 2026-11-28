
# apl-source:1
# مثال 2133 — عناوين مع إبقاء الكلمات الصغيرة
# apl-source:2
# Title case with small words
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2133-title-case-keep-small-words-lower.apl
# apl-source:6

# apl-source:7
# # القائمة a وan وthe وof وand وin وon
# apl-source:8
# # أول كلمة تكبر دائما
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
def عنوان(س):
  # apl-source:19
  صغيرة = ["a", "an", "the", "of", "and", "in", "on"]
  # apl-source:20
  خرج = []
  # apl-source:21
  for ك in range(len(س.split())):
    # apl-source:22
    ك_ = س.split()[ك]
    # apl-source:23
    if ك > 0 and (ك_ in صغيرة):
      # apl-source:24
      خرج = خرج + [ك_]
    # apl-source:25
    else:
      # apl-source:26
      خرج = خرج + [ك_.capitalize()]
  # apl-source:27
  return " ".join(خرج)
# apl-source:28

# apl-source:29
تأكد_يساوي(عنوان("the lord of the rings"), "The Lord of the Rings", "ثلاثة")
# apl-source:30
تأكد_يساوي(عنوان("war and peace"), "War and Peace", "اثنان")
# apl-source:31
تأكد_يساوي(عنوان("a tale of two cities"), "A Tale of Two Cities", "أربعة")
# apl-source:32
