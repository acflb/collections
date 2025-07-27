---
title: PowerShell美化与7.5.X版本在vscode配置
date: 2025-07-11 11:48:06
tags:
    - vscode
    - PowerShell
categories:
    - 技术
---

1. 下载并安装[PowerShell 7.5.X](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5#installing-the-msi-package)
   推荐下载 msi 版本,可以自动配置系统环境和通过`Update-Module` 或 **Microsoft Update** 接收安全补丁

2. 配置`vscode`

    安装`PowerShell`扩展

    ![image-20250711120704676](./assets/image-20250711120704676.png)

    打开设置文件`setting.json`

    ![image-20250711120135447](./assets/image-20250711120135447.png)

    ![image-20250711120213625](./assets/image-20250711120213625.png)

    再末尾`}`上一行添加配置文件

    ![image-20250711120605328](./assets/image-20250711120605328.png)

    ```json
    	// Windows终端配置文件
    	"terminal.integrated.profiles.windows": {
    		"PowerShell": {
    			"source": "PowerShell", // PowerShell终端来源
    			"icon": "terminal-powershell" // 设置PowerShell终端图标
    		},
    		"PowerShell 7": {
    			"path": "C:\\Program Files\\PowerShell\\7\\pwsh.exe" // PowerShell 7的执行路径
    		}
    	},
    	"terminal.integrated.defaultProfile.windows": "PowerShell 7" // 设置Windows默认终端为PowerShell 7
    ```

3. `` Ctrl + Shift + `  ``新建终端

    输入`$PSVersionTable.PSVersion`查看当前版本`7.5.2`

    ![image-20250711120924991](./assets/image-20250711120924991.png)

    配置 powershell，安装 powershell 插件

    ```powershell
    # 允许运行Install-Module脚本
    set-executionpolicy remotesigned

    # 更新最新版本的PSReadLine，为了自动补全
    Install-Module PSReadLine -Force

    # 创建powershell 的初始化脚本，点击确认创建即可
    notepad $profile

    # 安装几个插件
    Install-Module posh-git
    Install-Module Terminal-Icons

    ```

4. `oh-my-posh`配置

    安装并配置 oh-my-posh
    安装 oh-my-posh

    `winget install JanDeDobbeleer.OhMyPosh -s winget`

    如果该方法失效，移步[oh-my-posh windows set up](https://ohmyposh.dev/docs/installation/windows)查看最新安装方法

    下载 oh-my-posh 主题

    `git clone https://github.com/JanDeDobbeleer/oh-my-posh`

    将里面的 theme 文件夹保留即可。
    测试

    `oh-my-posh init pwsh | Invoke-Expression`
    打开 powershell 7 创建配置文件`New-Item -Path $PROFILE -ItemType File -Force`
    打开配置文件 `notepad $PROFILE`
    添加配置

    ```powershell
    # ====== 基础配置 ======
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

    # ====== 模块导入 ======
    Import-Module PSReadLine
    Import-Module posh-git
    Import-Module Terminal-Icons

    # ====== Oh My Posh 主题 ======推荐atomic, amro, catppuccin，velvet
    $env:Path += ";C:\Users\17667\AppData\Local\Programs\oh-my-posh\bin"
    $env:POSH_THEMES_PATH = "C:\Users\17667\AppData\Local\Programs\oh-my-posh\themes"
    oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\atomic.omp.json" | Invoke-Expression

    # ====== PSReadLine 增强 ======
    Set-PSReadLineOption -PredictionSource History
    Set-PSReadLineOption -PredictionViewStyle ListView
    Set-PSReadLineOption -EditMode Windows
    Set-PSReadLineKeyHandler -Chord "Ctrl+d" -Function DeleteChar
    Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

    # ====== 别名设置 ======
    Set-Alias ll Get-ChildItem
    Set-Alias g git
    Set-Alias find Select-String

    # ====== 实用函数 ======
    function which ($command) {
      Get-Command $command | Select-Object -ExpandProperty Source
    }
    function uptime {
      Get-WmiObject win32_operatingsystem |
      Select-Object @{Name='Uptime';Expression={(Get-Date) - $_.ConvertToDateTime($_.LastBootUpTime)}}
    }

    # ====== 中文问候语整合版 ======
    function Show-ChineseGreeting {
        # 基础信息
        $user = $env:USERNAME
        $date = Get-Date -Format "yyyy年MM月dd日 dddd"

        # 系统信息
        $osInfo = Get-CimInstance Win32_OperatingSystem
        $uptime = (Get-Date) - $osInfo.LastBootUpTime
        $uptimeStr = "系统已运行: {0}天{1}小时" -f $uptime.Days, $uptime.Hours

        # 随机语录
        $quotes = @(
            "代码改变世界！",
            "保持热爱，奔赴山海",
            "今天又是充满可能的一天",
            "学而不思则罔，思而不学则殆",
            "程序员：解决问题的艺术家",
            "每一次编译都是新的开始"
        )

        # 显示问候语
        Write-Host "欢迎您，Kaleus! " -NoNewline -ForegroundColor Green
        Write-Host "[$date]" -ForegroundColor Cyan
        Write-Host "$uptimeStr" -ForegroundColor Blue
        Write-Host "当前目录: $((Get-Location).Path)" -ForegroundColor Yellow
        Write-Host "$( $quotes | Get-Random )`n" -ForegroundColor Magenta
    }

    # 执行问候函数
    Show-ChineseGreeting
    ```

    PowerShell 5.x

    ```powerShell
    # ====== 基础配置 ======
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

    # ====== 模块导入 ======
    Import-Module PSReadLine
    Import-Module posh-git
    Import-Module Terminal-Icons

    # ====== Oh My Posh 主题 ======
    $env:Path += ";C:\Users\17667\AppData\Local\Programs\oh-my-posh\bin"
    $env:POSH_THEMES_PATH = "C:\Users\17667\AppData\Local\Programs\oh-my-posh\themes"
    oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\catppuccin.omp.json" | Invoke-Expression

    # ====== PSReadLine 增强 ======
    Set-PSReadLineOption -PredictionSource History
    Set-PSReadLineOption -PredictionViewStyle ListView
    Set-PSReadLineOption -EditMode Windows
    Set-PSReadLineKeyHandler -Chord "Ctrl+d" -Function DeleteChar
    Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

    # ====== 别名设置 ======
    Set-Alias ll Get-ChildItem
    Set-Alias g git
    Set-Alias find Select-String

    # ====== 实用函数 ======
    function which ($command) {
      Get-Command $command | Select-Object -ExpandProperty Source
    }
    function uptime {
      Get-WmiObject win32_operatingsystem |
      Select-Object @{Name='Uptime';Expression={(Get-Date) - $_.ConvertToDateTime($_.LastBootUpTime)}}
    }

    # ====== 启动问候语 ======
    # ====== English Greeting Function ======
    function Show-EnglishGreeting {
        # Basic info
        $user = $env:USERNAME
        $date = Get-Date -Format "dddd, MMMM dd, yyyy"
        $timeOfDay = switch ((Get-Date).Hour) {
            { $_ -lt 5 } { "late night" }
            { $_ -lt 12 } { "morning" }
            { $_ -lt 17 } { "afternoon" }
            { $_ -lt 21 } { "evening" }
            default { "night" }
        }

        # System info
        $osInfo = Get-CimInstance Win32_OperatingSystem
        $uptime = (Get-Date) - $osInfo.LastBootUpTime
        $uptimeStr = "System uptime: {0} days {1} hours" -f $uptime.Days, $uptime.Hours

        # Random quotes
        $quotes = @(
            "Code changes the world!",
            "Stay curious, keep learning",
            "Today is full of possibilities",
            "The best way to predict the future is to invent it",
            "Programmers: artists who solve problems with logic",
            "Every compile is a new beginning",
            "Make it work, make it right, make it fast"
        )

        # Display greeting
        Write-Host "Good $timeOfDay, Kaleus! " -NoNewline -ForegroundColor Green
        Write-Host "[$date]" -ForegroundColor Cyan
        Write-Host "$uptimeStr" -ForegroundColor Blue
        Write-Host "Current directory: $((Get-Location).Path)" -ForegroundColor Yellow
        Write-Host "$($quotes | Get-Random)`n" -ForegroundColor Magenta
    }

    # Execute greeting function
    Show-EnglishGreeting
    ```

    Windows Terminal 美化

    打开终端 ➡️`Ctrl + .` 打开设置 ➡️`JSON`文件

    ```json
    {
    	"profiles": {
    		"defaults": {
    			"colorScheme": "One Half Dark",
    			"font": {
    				"face": "JetBrainsMono Nerd Font"
    			},
    			"experimental.retroTerminalEffect": false,
    			"opacity": 60,
    			"padding": "15, 15, 15, 15",
    			"useAcrylic": true
    		},
    		"list": [
    			{
    				"commandline": "%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    				"guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
    				"hidden": false,
    				"name": "Windows PowerShell"
    			},
    			{
    				"commandline": "%SystemRoot%\\System32\\cmd.exe",
    				"guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
    				"hidden": false,
    				"name": "\u547d\u4ee4\u63d0\u793a\u7b26"
    			},
    			{
    				"guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
    				"hidden": false,
    				"name": "Azure Cloud Shell",
    				"source": "Windows.Terminal.Azure"
    			},
    			{
    				"guid": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
    				"hidden": false,
    				"name": "PowerShell",
    				"source": "Windows.Terminal.PowershellCore"
    			}
    		]
    	},
    	"schemes": [
    		{
    			"name": "One Half Dark",
    			"background": "#282C34",
    			"black": "#282C34",
    			"blue": "#61AFEF",
    			"cyan": "#56B6C2",
    			"green": "#98C379",
    			"purple": "#C678DD",
    			"red": "#E06C75",
    			"white": "#DCDFE4",
    			"yellow": "#E5C07B",
    			"brightBlack": "#5A6374"
    		}
    	]
    }
    ```

参考:
[汇尘轩](https://kirigaya.cn/blog/article?seq=28)
[Gemini](https://gemini.google.com/app)
[DeepSeek](https://chat.deepseek.com/)
