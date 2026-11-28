
# apl-source:1
# مثال 1564 — عد الكلمات في نص
# apl-source:2
# Count words in text
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1564-count-words-in-text.apl
# apl-source:6

# apl-source:7
# split بلا وسيط يتجاهل المسافات الزائدة
# apl-source:8
# طول القائمة هو العدد
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
def عدد_الكلمات(نص_):
  # apl-source:19
  return len(نص_.split())
# apl-source:20

# apl-source:21
تأكد_يساوي(عدد_الكلمات("مرحبا بالعالم"), 2, "كلمتان")
# apl-source:22
تأكد_يساوي(عدد_الكلمات("  كثير   من   المسافات  "), 3, "مسافات")
# apl-source:23
تأكد_يساوي(عدد_الكلمات(""), 0, "فارغ")
# apl-source:24
