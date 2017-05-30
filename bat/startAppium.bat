@echo off
echo "作需要两个模拟器要执行任务，所以需要启动两个appium server，你们要是没有自己删掉一行啊"
start "" "D:\Program Files\Appium\Appium\node.exe" "D:\Program Files\Appium\Appium\node_modules\appium\bin\appium.js" --port 4723
start "" "D:\Program Files\Appium\Appium\node.exe" "D:\Program Files\Appium\Appium\node_modules\appium\bin\appium.js" --port 5723