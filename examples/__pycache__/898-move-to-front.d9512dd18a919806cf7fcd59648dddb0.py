
# apl-source:1
# مثال 898 — تحويلة انقل للأمام
# apl-source:2
# Move-to-front transform
# apl-source:3
# Demonstrates: جدول متكيف ذاتياً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/898-move-to-front.apl
# apl-source:6

# apl-source:7
# تحويلة انقل للأمام: ضغط يستغل التكرار الموضعي
# apl-source:8
# كل رمز يستبدل بموضعه في جدول ثم ينتقل لمقدمته
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
def انقل_للأمام(دخل, جدول):
  # apl-source:19
  خرج = []
  # apl-source:20
  ج = []
  # apl-source:21
  for x in جدول:
    # apl-source:22
    ج = ج + [x]
  # apl-source:23
  for رمز in دخل:
    # apl-source:24
    موضع = 0
    # apl-source:25
    for i in range(len(ج)):
      # apl-source:26
      if ج[i] == رمز:
        # apl-source:27
        موضع = i
    # apl-source:28
    خرج = خرج + [موضع]
    # apl-source:29
    ج = [رمز] + ج[:موضع] + ج[موضع + 1:]
  # apl-source:30
  return خرج
# apl-source:31

# apl-source:32
def فك_انقل(مشفر, جدول):
  # apl-source:33
  خرج = []
  # apl-source:34
  ج = []
  # apl-source:35
  for x in جدول:
    # apl-source:36
    ج = ج + [x]
  # apl-source:37
  for موضع in مشفر:
    # apl-source:38
    رمز = ج[موضع]
    # apl-source:39
    خرج = خرج + [رمز]
    # apl-source:40
    ج = [رمز] + ج[:موضع] + ج[موضع + 1:]
  # apl-source:41
  return خرج
# apl-source:42

# apl-source:43
جدول = [1, 2, 3, 4]
# apl-source:44
دخل = [3, 1, 4, 1]
# apl-source:45
مشفر = انقل_للأمام(دخل, جدول)
# apl-source:46
print("المشفر:", مشفر)
# apl-source:47
print("المفكوك:", فك_انقل(مشفر, جدول))
# apl-source:48

# apl-source:49
تأكد_يساوي(مشفر[0], 2, "أول موضع")
# apl-source:50
تأكد_يساوي(len(مشفر), 4, "طول المشفر")
# apl-source:51

# apl-source:52
# الفك يعيد الأصل
# apl-source:53
مفكوك = فك_انقل(مشفر, جدول)
# apl-source:54
تأكد_يساوي(len(مفكوك), 4, "طول المفكوك")
# apl-source:55
for i in range(4):
  # apl-source:56
  تأكد_يساوي(مفكوك[i], دخل[i], "رمز " + str(i))
# apl-source:57

# apl-source:58
# التكرار المتتالي يعطي أصفاراً: مفتاح كفاءة الضغط
# apl-source:59
دخل2 = [7, 7, 7, 7]
# apl-source:60
جدول2 = [7, 8, 9]
# apl-source:61
مشفر2 = انقل_للأمام(دخل2, جدول2)
# apl-source:62
تأكد_يساوي(مشفر2[1], 0, "تكرار أول")
# apl-source:63
تأكد_يساوي(مشفر2[2], 0, "تكرار ثانٍ")
# apl-source:64
تأكد_يساوي(مشفر2[3], 0, "تكرار ثالث")
# apl-source:65
