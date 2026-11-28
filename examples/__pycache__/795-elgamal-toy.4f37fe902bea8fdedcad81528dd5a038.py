
# apl-source:1
# مثال 795 — تشفير الجمال
# apl-source:2
# ElGamal toy
# apl-source:3
# Demonstrates: أس معياري، مفتاح عابر، معكوس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/795-elgamal-toy.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# تشفير الجمال التعليمي: مفتاح عام من أس معياري ومفتاح عابر لكل رسالة
# apl-source:25
# Demonstrates: أس معياري بالتربيع, مشاركة سر مشترك, معكوس ضربي للفك
# apl-source:26

# apl-source:27
def أس_معياري(أساس, أس, م):
  # apl-source:28
  ناتج = 1
  # apl-source:29
  ب = أساس % م
  # apl-source:30
  ه = أس
  # apl-source:31
  while ه > 0:
    # apl-source:32
    if ه % 2 == 1:
      # apl-source:33
      ناتج = (ناتج * ب) % م
    # apl-source:34
    ب = (ب * ب) % م
    # apl-source:35
    ه = ه // 2
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
def معكوس(أ, م):
  # apl-source:39
  # م أولي: المعكوس هو أ^(م-2) حسب فيرما
  # apl-source:40
  return أس_معياري(أ, م - 2, م)
# apl-source:41

# apl-source:42
أولي = 23
# apl-source:43
منشئ = 5
# apl-source:44
سري = 6
# apl-source:45
عام = أس_معياري(منشئ, سري, أولي)
# apl-source:46
تأكد_يساوي(عام, 8, "المفتاح العام")
# apl-source:47

# apl-source:48
رسالة = 10
# apl-source:49
عابر = 7
# apl-source:50
ج1 = أس_معياري(منشئ, عابر, أولي)
# apl-source:51
مشترك = أس_معياري(عام, عابر, أولي)
# apl-source:52
ج2 = (رسالة * مشترك) % أولي
# apl-source:53
تأكد_يساوي(ج1, 17, "الجزء الأول من الشيفرة")
# apl-source:54
تأكد_يساوي(ج2, 5, "الجزء الثاني من الشيفرة")
# apl-source:55

# apl-source:56
مشترك2 = أس_معياري(ج1, سري, أولي)
# apl-source:57
مفكوك = (ج2 * معكوس(مشترك2, أولي)) % أولي
# apl-source:58
تأكد_يساوي(مفكوك, رسالة, "فك التشفير يعيد الرسالة")
# apl-source:59
تأكد_يساوي((أس_معياري(2, 10, 23)), 12, "أس معياري معروف")
# apl-source:60
