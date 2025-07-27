---
title: Windows环境配置
date: 2025-06-13 16:28:48
tags:
    - Windows
categories:
    - 技术
---

## 系统

Windows 与 Office 激活：`irm https://get.activated.win | iex`
Windows 与 Office 下载： `https://massgrave.dev/genuine-installation-media`
安全防护：[火绒](https://www.huorong.cn/)
驱动安装: [360 驱动大师](https://dm.weishi.360.cn/home.html)
软件卸载：[Geek Uninstaller](https://geekuninstaller.com/download)

## 浏览器

[Firefox Dev](https://www.mozilla.org/zh-CN/firefox/developer/)
[Chrome](https://www.google.com/chrome/index.html)
[Edge](https://www.microsoft.com/zh-cn/edge/download?form=MA13FJ)
[Clash Nyanpasu](https://nyanpasu.elaina.moe/)-可以本地保存一份

## 开发工具

[VSCode](https://code.visualstudio.com/Download)
[Charls](https://www.charlesproxy.com/download/)-[激活](https://www.zzzmode.com/mytools/charles/)

## 代码管理

代码管理：[Git](https://git-scm.com/downloads)

```powershell
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890
```

Node 管理：[NVM](https://nvm.uihtm.com/doc/download-nvm.html)`管理员安装`

打开管理员`powershell`
nvm 代理配置 `nvm proxy 127.0.0.1:7890`
查看 node 版本 `nvm list available`
安装 node `nvm install 20.19.4`
开启版本管理 `nvm on`
使用 node `nvm use 20.19.4`
npm 换源 `npm config set registry https://registry.npmmirror.com`
安装 pnpm `npm install -g pnpm`
开启 powerShell 本地脚本运行许可 `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Python 管理：[Anaconda](https://www.anaconda.com/download/success)

## 工具

便签：[flomo](https://help.flomoapp.com/basic/app.html)
清单：[嘀嗒清单](https://dida365.com/download)
笔记整理：[obsidian](https://obsidian.md/download)
快捷搜索：[uTools](https://www.u-tools.cn/download/)
显示亮度：[Twinkle](https://github.com/xanderfrangos/twinkle-tray/releases)
蓝光过滤：[f.lux](https://justgetflux.com/) `Alt + PgUp/PgDn` 切换亮度
定时休息: [Stretchly](https://github.com/hovancik/stretchly/releases)
解压工具：[Bandizip](https://github.com/shuhongfan/Bandizip)
截图工具：[Snipaste](https://zh.snipaste.com/)
翻译工具：[有道词典](https://fanyi.youdao.com/download-Windows)
文件搜索：[Everying](https://www.voidtools.com/zh-cn/downloads/)
输入法：[微信输入法](https://z.weixin.qq.com/)
托盘隐藏：[PSTrayFactory](https://www.pssoftlab.com/)
Windows 快捷增强:[PowerToys](https://github.com/microsoft/PowerToys/releases/tag/v0.91.1)
快捷按键：[AutoHotkey](https://github.com/AutoHotkey/AutoHotkey/releases)[MyKeymap](https://github.com/xianyukang/MyKeymap/releases)
鼠标工具：[WGestures](https://www.yingdev.com/projects/wgestures),[Strokesplus.net](https://www.strokesplus.net/)

## 美化

字体：[JetBrainsMonoNL Nerd Font](https://www.nerdfonts.com/font-downloads)
任务栏 [Nexus](https://winstep.net/nexus.asp)
透明任务栏 [TranslucentTB](微软商店)
桌面 [Rainmeter](https://www.rainmeter.net/) [Rainmeter 皮肤](https://zhutix.com/tag/rainmeter/)
美化包 [MToolBox](https://winmoes.com/tools/12948.html)

## VS 插件

conventional commits ---- git 规范提交插件
powershell ---- 命令行自动补充
gitignore ---- git 上传忽略文件
markdown preview ---- markdown 预览 Ctrl+Shift+V

## 娱乐

[steam](https://store.steampowered.com/about/)
[QQ](https://im.qq.com/pcqq/index.shtml)
