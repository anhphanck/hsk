@echo off
echo =========================================
echo  HSK Pinyin Trainer - Local Server
echo  Mo trinh duyet tren dien thoai:
echo  Vao cung mang WiFi, truy cap:
echo  http://[IP_may_tinh]:8000
echo =========================================
echo.
python -m http.server 8000
pause
