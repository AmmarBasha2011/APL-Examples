
# apl-source:1
# مثال 893 — أعداد أويلريان
# apl-source:2
# Eulerian numbers
# apl-source:3
# Demonstrates: تبديلات بعدد صعود ثابت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/893-eulerian-numbers.apl
# apl-source:6

# apl-source:7
# أعداد أويلريان A(n,k): تبديلات n عنصراً لها بالضبط k صعوداً
# apl-source:8
# A(n,k) = (n-k)*A(n-1,k-1) + (k+1)*A(n-1,k)
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
def أويلريان(ن, ك):
  # apl-source:19
  if ك >= ن:
    # apl-source:20
    return 0
  # apl-source:21
  if ك == 0:
    # apl-source:22
    return 1
  # apl-source:23
  return (ن - ك) * أويلريان(ن - 1, ك - 1) + (ك + 1) * أويلريان(ن - 1, ك)
# apl-source:24

# apl-source:25
print("A(4,1) =", أويلريان(4, 1))
# apl-source:26
print("A(5,2) =", أويلريان(5, 2))
# apl-source:27

# apl-source:28
تأكد_يساوي(أويلريان(4, 1), 11, "A(4,1) = 11")
# apl-source:29
تأكد_يساوي(أويلريان(5, 2), 66, "A(5,2) = 66")
# apl-source:30
تأكد_يساوي(أويلريان(6, 0), 1, "A(n,0) = 1")
# apl-source:31

# apl-source:32
# مجموع الصف n هو مضروب n
# apl-source:33
مجموع = 0
# apl-source:34
for ك in range(5):
  # apl-source:35
  مجموع = مجموع + أويلريان(5, ك)
# apl-source:36
تأكد_يساوي(مجموع, 120, "مجموع الصف 5 هو 5! = 120")
# apl-source:37

# apl-source:38
# تماثل الصف: A(n,k) = A(n,n-1-k)
# apl-source:39
تأكد_يساوي(أويلريان(5, 1), أويلريان(5, 3), "تماثل الصف")
# apl-source:40
