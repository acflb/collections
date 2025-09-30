-- 启用左键检测
EnablePrimaryMouseButtonEvents(true)

local Xjming = {1,2,1,2,1,2,1,2,1,2,1,0,0,0,0,0,-1,-2,-1,-2,-1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1}
local Yjming = {2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,8,8,8}

local capacity = 30

function OnEvent(event, arg)
	-- 监听左键事件
	--OutputLogMessage("event = %s, arg = %d\n", event, arg)

	if (event == "PROFILE_ACTIVATED") then
		OutputLogMessage("Event: "..event.." Arg: "..arg.."\n")
	end

	if (event == "MOUSE_BUTTON_PRESSED" and arg == 1) then
		OutputLogMessage("G1 pressed"..arg.."\n")

		-- for循环
		for i=1, capacity do
			MoveMouseRelative(Xjming[i],Yjming[i])
			Sleep(50)
		end
	end
end


-- 分隔符，中文会导致报错，上方不要 --


EnablePrimaryMouseButtonEvents(true)

local Xjming = {1,2,1,2,1,2,1,2,1,2,1,0,0,0,0,0,-1,-2,-1,-2,-1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1}
local Yjming = {2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,8,8,8}

local capacity = 30

function OnEvent(event, arg)
	--OutputLogMessage("event = %s, arg = %d\n", event, arg)

	if (event == "PROFILE_ACTIVATED") then
		OutputLogMessage("Event: "..event.." Arg: "..arg.."\n")
	end

	if (event == "MOUSE_BUTTON_PRESSED" and arg == 1) then
		OutputLogMessage("G1 pressed"..arg.."\n")
		for i=1, capacity do
			MoveMouseRelative(Xjming[i],Yjming[i])
			Sleep(50)
		end
	end
end