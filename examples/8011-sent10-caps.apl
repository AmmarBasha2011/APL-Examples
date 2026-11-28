# مثال 8011 — أول حرف كبير لكل كلمة في الجملة رقم 11
# caps for sentence 11
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8011-sent10-caps.apl

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

تأكد_يساوي(ف("red blue green red blue red"), "Red Blue Green Red Blue Red", "حالة 1")
تأكد_يساوي(ف("nile river nile delta river"), "Nile River Nile Delta River", "حالة 2")
تأكد_يساوي(ف("bread milk bread eggs milk bread"), "Bread Milk Bread Eggs Milk Bread", "حالة 3")
