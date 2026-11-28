# مثال 7961 — أول حرف كبير لكل كلمة في الجملة رقم 6
# caps for sentence 6
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7961-sent5-caps.apl

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

تأكد_يساوي(ف("we love data and data loves us"), "We Love Data And Data Loves Us", "حالة 1")
تأكد_يساوي(ف("a b c a b a"), "A B C A B A", "حالة 2")
تأكد_يساوي(ف("cairo is big and cairo is old"), "Cairo Is Big And Cairo Is Old", "حالة 3")
