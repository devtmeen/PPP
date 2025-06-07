cd "C:\Users\Administrator\Desktop\New_API\"

for /l %%x in (1, 1, 900000) do (
   cls
   title Update Baccarat %%x
   python Update_BonusTime_Baccarat.py
   timeout /t 10
)