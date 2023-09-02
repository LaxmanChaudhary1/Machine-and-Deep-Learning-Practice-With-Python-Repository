@echo off
cls

echo Laptop Condition Report:
echo -----------------------
echo.

echo 1. System Information:
echo ---------------------
systeminfo | findstr /C:"OS Name" /C:"OS Version" /C:"System Type" /C:"Host Name"

echo.
echo 2. Memory (RAM) Information:
echo ---------------------------
wmic memorychip get capacity

echo.
echo 3. Storage Information:
echo ----------------------
wmic logicaldisk get caption,size,freespace

echo.
echo 4. Battery Information:
echo ----------------------
powercfg /batteryreport

echo.
echo 5. Temperature and Fan Speed:
echo -----------------------------
wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature
wmic /namespace:\\root\wmi PATH MSAcpi_Fan get DeviceID, Active

echo.
echo 6. Network Information:
echo ----------------------
ipconfig /all

echo.
echo 7. Display Information:
echo ----------------------
wmic desktopmonitor get screenheight, screenwidth

pause
