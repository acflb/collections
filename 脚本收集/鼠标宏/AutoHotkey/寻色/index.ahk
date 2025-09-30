; 发送弹窗
; MsgBox("Hello world!")

; `^`----`Ctrl`
; `#`----`Win`
; `!`----`Alt`
; `+`----`Shift`

; `HotIf` 如果符合条件才注册
; `WinExist` 是否存在目标程序

; #HotIf !WinExist("Notepad")
; ^q:: {
; 	if (WinExist("Notepad")) {
; 		return
; 	}
; 	Run("Notepad")
; }


; #Include ./ImagePut.ahk
; ^q:: {
; 	pic := ImagePutBuffer('卡拉彼丘')

; 	; 显示截图
; 	; pic.Show()

; 	point := pic.PixelSearch(0xFFe24e55)
; 	MsgBox('X坐标' point[1] 'y坐标' point[2])
; }
