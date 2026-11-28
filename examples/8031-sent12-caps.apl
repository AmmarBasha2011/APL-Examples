# مثال 8031 — أول حرف كبير لكل كلمة في الجملة رقم 13
# caps for sentence 13
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8031-sent12-caps.apl

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

تأكد_يساوي(ف("cairo is big and cairo is old"), "Cairo Is Big And Cairo Is Old", "حالة 1")
تأكد_يساوي(ف("stars and moon and stars again"), "Stars And Moon And Stars Again", "حالة 2")
تأكد_يساوي(ف("yes no yes yes no maybe"), "Yes No Yes Yes No Maybe", "حالة 3")
