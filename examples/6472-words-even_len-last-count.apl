# مثال 6472 — العدد: الكلمات ذات الطول الزوجي ثم (آخر حرف)
# count of last over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6472-words-even_len-last-count.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك[len(ك) - 1]]
  ارجع len(ر)

تأكد_يساوي(ف("the cat sat on the mat"), 1, "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), 2, "حالة 2")
تأكد_يساوي(ف("one two three four five six"), 2, "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), 2, "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), 8, "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), 5, "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), 5, "حالة 7")
تأكد_يساوي(ف("hello"), 0, "حالة 8")
