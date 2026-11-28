
# apl-source:1
# مثال 944 — مرشح كالمان الأحادي
# apl-source:2
# 1D Kalman filter
# apl-source:3
# Demonstrates: كسب متكيف للقياس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/944-kalman.apl
# apl-source:6

# apl-source:7
# مرشح كالمان الأحادي: دمج قياسات مضججة في تقدير سلس
# apl-source:8
# يوازن بين ثقة النموذج وثقة القياس بكسب متكيف
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
# ضجيج العملية وضجيج القياس ثابتان
# apl-source:19
ضجيج_عملية = 0.01
# apl-source:20
ضجيج_قياس = 0.5
# apl-source:21

# apl-source:22
def رشح(قياسات):
  # apl-source:23
  تقدير = قياسات[0]
  # apl-source:24
  تباين = 1
  # apl-source:25
  خرج = []
  # apl-source:26
  for قياس in قياسات:
    # apl-source:27
    # تنبؤ
    # apl-source:28
    تباين = تباين + ضجيج_عملية
    # apl-source:29
    # تحديث
    # apl-source:30
    كسب = تباين / (تباين + ضجيج_قياس)
    # apl-source:31
    تقدير = تقدير + كسب * (قياس - تقدير)
    # apl-source:32
    تباين = (1 - كسب) * تباين
    # apl-source:33
    خرج = خرج + [تقدير]
  # apl-source:34
  return خرج
# apl-source:35

# apl-source:36
قياسات = [1, 1.3, 0.8, 1.1, 1]
# apl-source:37
تقديرات = رشح(قياسات)
# apl-source:38
print("التقديرات:", تقديرات)
# apl-source:39

# apl-source:40
متوقع = [1, 1.1224, 1.0258, 1.0437, 1.0347]
# apl-source:41
تأكد_يساوي(len(تقديرات), 5, "الطول")
# apl-source:42
for i in range(5):
  # apl-source:43
  تأكد_يساوي(round(تقديرات[i], 4), متوقع[i], "تقدير " + str(i))
# apl-source:44

# apl-source:45
# التقدير أكثر سلاسة من القياسات: قفزاته أصغر
# apl-source:46
قفزة_قياس = 0.5
# apl-source:47
قفزة_تقدير = تقديرات[3] - تقديرات[2]
# apl-source:48
if قفزة_تقدير < 0:
  # apl-source:49
  قفزة_تقدير = -قفزة_تقدير
# apl-source:50
if قفزة_تقدير >= قفزة_قياس:
  # apl-source:51
  print("فشل: المرشح لا ينعّم")
  # apl-source:52
  قياسي_نظام_اخرج(1)
# apl-source:53
print("ناجح: المرشح ينعّم")
# apl-source:54
