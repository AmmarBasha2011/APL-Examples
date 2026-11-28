# مثال 6484 — العدد: كل الكلمات ثم (أول حرف كبير)
# count of cap over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6484-words-all-cap-count.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: العدد

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
    لو 1 == 1:
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع len(ر)

تأكد_يساوي(ف("the cat sat on the mat"), 6, "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), 6, "حالة 2")
تأكد_يساوي(ف("one two three four five six"), 6, "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), 5, "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), 10, "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), 6, "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), 7, "حالة 7")
تأكد_يساوي(ف("hello"), 1, "حالة 8")
