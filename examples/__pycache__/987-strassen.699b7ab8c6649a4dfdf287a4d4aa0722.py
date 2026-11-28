
# apl-source:1
# مثال 987 — ضرب ستراسن
# apl-source:2
# Strassen multiplication
# apl-source:3
# Demonstrates: سبع ضربات بدل ثماني
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/987-strassen.apl
# apl-source:6

# apl-source:7
# ضرب ستراسن: سبعة ضربات بدل ثمانية لمصفوفتين 2x2
# apl-source:8
# أساس الخوارزمية التكرارية الأسرع للمصفوفات الكبيرة
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
أ = [[1, 2], [3, 4]]
# apl-source:19
ب = [[5, 6], [7, 8]]
# apl-source:20

# apl-source:21
ض1 = أ[0][0] * (ب[0][1] - ب[1][1])
# apl-source:22
ض2 = (أ[0][0] + أ[0][1]) * ب[1][1]
# apl-source:23
ض3 = (أ[1][0] + أ[1][1]) * ب[0][0]
# apl-source:24
ض4 = أ[1][1] * (ب[1][0] - ب[0][0])
# apl-source:25
ض5 = (أ[0][0] + أ[1][1]) * (ب[0][0] + ب[1][1])
# apl-source:26
ض6 = (أ[0][1] - أ[1][1]) * (ب[1][0] + ب[1][1])
# apl-source:27
ض7 = (أ[0][0] - أ[1][0]) * (ب[0][0] + ب[0][1])
# apl-source:28

# apl-source:29
ناتج11 = ((ض5 + ض4) - ض2) + ض6
# apl-source:30
ناتج12 = ض1 + ض2
# apl-source:31
ناتج21 = ض3 + ض4
# apl-source:32
ناتج22 = ((ض1 + ض5) - ض3) - ض7
# apl-source:33

# apl-source:34
تأكد_يساوي(ناتج11, 19, "العنصر الأول")
# apl-source:35
تأكد_يساوي(ناتج12, 22, "العنصر الثاني")
# apl-source:36
تأكد_يساوي(ناتج21, 43, "العنصر الثالث")
# apl-source:37
تأكد_يساوي(ناتج22, 50, "العنصر الرابع")
# apl-source:38
تأكد_يساوي((5) + (14), ناتج11, "تحقق مباشر")
# apl-source:39
