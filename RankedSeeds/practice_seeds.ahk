#SingleInstance force

#If WinActive("Minecraft") && (WinActive("ahk_exe javaw.exe") || WinActive("ahk_exe java.exe"))
	^r:: ; hotkey
	FileRead, seeds, seeds.txt
	RegExMatch(seeds, ".+?\v", seed)
	If !RegExMatch(seed, "\d") {
		MsgBox The seed list is empty. The program will exit.
		ExitApp
	}
	Send {Tab}{Enter}{Tab 3}{Enter}
	Send {Tab 2}{Space 3}{Tab 4}{Space}
	Send {Tab 3}
	Send %seed%
	Send {Tab 6}{Space}
	seeds := RegExReplace(seeds, ".+?\v", "", "", 1)
	StringTrimLeft, seeds, seeds, 1
	FileDelete, seeds.txt
	FileAppend, %seeds%, seeds.txt
	return