# مثال 7941 — أول حرف كبير لكل كلمة في الجملة رقم 4
# caps for sentence 4
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7941-sent3-caps.apl

# نقسم الجملة إلى كلمات
# ونعالجها حسب المطلوب

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = []
  لكل ك في ن.split(" "):
    ر = ر + [ك[0].upper() + ك[1:]]
  ارجع " ".join(ر)

تأكد_يساوي(ف("one fish two fish red fish blue fish"), "One Fish Two Fish Red Fish Blue Fish", "حالة 1")
تأكد_يساوي(ف("tea for two and two for tea"), "Tea For Two And Two For Tea", "حالة 2")
تأكد_يساوي(ف("red blue green red blue red"), "Red Blue Green Red Blue Red", "حالة 3")
