
# apl-source:1
# مثال 1140 — مكرر بفلويد
# apl-source:2
# Find duplicate with Floyd cycle
# apl-source:3
# Demonstrates: أرنب وسلحفاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1140-find-duplicate-floyd.apl
# apl-source:6

# apl-source:7
# نعامل القائمة كمؤشرات فتتكون حلقة
# apl-source:8
# ونجد بداية الحلقة بمؤشرين
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
def مكرر(أ):
  # apl-source:19
  بطيء = أ[0]
  # apl-source:20
  سريع = أ[0]
  # apl-source:21
  بطيء = أ[بطيء]
  # apl-source:22
  سريع = أ[أ[سريع]]
  # apl-source:23
  while بطيء != سريع:
    # apl-source:24
    بطيء = أ[بطيء]
    # apl-source:25
    سريع = أ[أ[سريع]]
  # apl-source:26
  بطيء = أ[0]
  # apl-source:27
  while بطيء != سريع:
    # apl-source:28
    بطيء = أ[بطيء]
    # apl-source:29
    سريع = أ[سريع]
  # apl-source:30
  return بطيء
# apl-source:31

# apl-source:32
تأكد_يساوي(مكرر([1,3,4,2,2]), 2, "مثال أول")
# apl-source:33
تأكد_يساوي(مكرر([3,1,3,4,2]), 3, "مثال ثان")
# apl-source:34
تأكد_يساوي(مكرر([1,1]), 1, "اثنان")
# apl-source:35
تأكد_يساوي(مكرر([2,5,9,6,9,3,8,7,1,4]), 9, "عشرة")
# apl-source:36
