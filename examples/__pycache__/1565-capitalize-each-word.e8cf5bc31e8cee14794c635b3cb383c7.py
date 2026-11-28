
# apl-source:1
# مثال 1565 — حرف كبير لكل كلمة
# apl-source:2
# Capitalize each word
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1565-capitalize-each-word.apl
# apl-source:6

# apl-source:7
# نقسم النص إلى كلمات
# apl-source:8
# نعيد بناء كل كلمة ثم نجمعها
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
def كبّر_الكلمات(نص_):
  # apl-source:19
  كلمات = []
  # apl-source:20
  for ك in نص_.split():
    # apl-source:21
    كلمات.append(ك[0].upper() + ك[1:].lower())
  # apl-source:22
  return " ".join(كلمات)
# apl-source:23

# apl-source:24
تأكد_يساوي(كبّر_الكلمات("hello wORLD"), "Hello World", "إنجليزي")
# apl-source:25
تأكد_يساوي(كبّر_الكلمات("a bc def"), "A Bc Def", "أطوال مختلفة")
# apl-source:26
تأكد_يساوي(كبّر_الكلمات(""), "", "فارغ")
# apl-source:27
