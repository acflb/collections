; 1.发送弹窗
; MsgBox("Hello world!")

; `^`----`Ctrl`
; `#`----`Win`
; `!`----`Alt`
; `+`----`Shift`

; `HotIf` 如果符合条件才注册
; `WinExist` 是否存在目标程序

; #HotIf !WinExist("Notepad")
; ^q:: {
;     if (WinExist("Notepad")) {
;         return
;     }
;     Run("Notepad")
; }

; 检测按键状态 "1"为按下
; state := GetKeyState("RButton")
; MsgBox(state)

; #Include ./ImagePut.ahk
; ^q:: {
; 	pic := ImagePutBuffer('卡拉彼丘')

; 	; 显示截图
; 	; pic.Show()

; 	point := pic.PixelSearch(0xFFe24e55)
; 	MsgBox('X坐标' point[1] 'y坐标' point[2])
; }

#Include ./ImagePut.ahk

; BrownDust() {
; pic := ImagePutBuffer('BrownDust II')
; point := pic.ImageSearch('1.png')
; MsgBox('X坐标' point[1] 'y坐标' point[2])
; }

; Calculate() {
; 	pic := ImagePutBuffer('计算器')
; 	; pic.Show()
; 	point := pic.ImageSearch('2.png')
; 	MsgBox(point)
; }

ClickFunction() {

    Click 2210, 91
    Sleep 200
    Click 1399, 1050

}

^q:: {

    ClickFunction()

}
