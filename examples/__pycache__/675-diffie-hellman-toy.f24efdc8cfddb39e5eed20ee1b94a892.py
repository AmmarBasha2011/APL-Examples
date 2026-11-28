
# apl-source:1
# مثال 675 — تبادل ديفي-هيلمان التعليمي
# apl-source:2
# Toy Diffie-Hellman
# apl-source:3
# Demonstrates: سر مشترك، أس معياري، مولد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/675-diffie-hellman-toy.apl
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
# ديفي-هلمان مصغر: سر مشترك عبر قناة علنية
# apl-source:25
# Demonstrates: أس معياري, جذر بدائي, سرية بالمثل
# apl-source:26
# كل طرف يحسب السر نفسه دون إرساله
# apl-source:27

# apl-source:28
def أس_معياري(قاعدة, أس, معيار):
  # apl-source:29
  ناتج = 1
  # apl-source:30
  قاعدة = قاعدة % معيار
  # apl-source:31
  while أس > 0:
    # apl-source:32
    if أس % 2 == 1:
      # apl-source:33
      ناتج = (ناتج * قاعدة) % معيار
    # apl-source:34
    قاعدة = (قاعدة * قاعدة) % معيار
    # apl-source:35
    أس = أس // 2
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
أولي = 23
# apl-source:39
أساس = 5
# apl-source:40
سر_أ = 6
# apl-source:41
سر_ب = 15
# apl-source:42

# apl-source:43
عام_أ = أس_معياري(أساس, سر_أ, أولي)
# apl-source:44
عام_ب = أس_معياري(أساس, سر_ب, أولي)
# apl-source:45
تأكد_يساوي(عام_أ, 8, "عام أ")
# apl-source:46
تأكد_يساوي(عام_ب, 19, "عام ب")
# apl-source:47

# apl-source:48
مشترك_أ = أس_معياري(عام_ب, سر_أ, أولي)
# apl-source:49
مشترك_ب = أس_معياري(عام_أ, سر_ب, أولي)
# apl-source:50
تأكد_يساوي(مشترك_أ, مشترك_ب, "السران متطابقان")
# apl-source:51
تأكد_يساوي(مشترك_أ, 2, "السر المتوقع")
# apl-source:52
print("السر المشترك:", مشترك_أ)
# apl-source:53
