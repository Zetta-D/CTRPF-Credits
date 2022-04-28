#===================================================================
# * @file    CTRPFCredits.py
# * @brief   Small program in python to modify lib ctrpf credits
# * @author  ZettaD
# * @date    04.28.2022
#===================================================================

# pattern to search : \x62\x00\x00\x00\x79\x00\x00\x00\x80\x00\x00\x00\x38\x01\x00\x00\x61\x00\x00\x00\x6E\x00\x00\x00\xC4\x01\x00\x00\xD4\x01\x00\x00\x00\x69\x00\x00\x00\x74\x00\x00\x00\x84\x01\x00\x00\xCC\x01\x00\x43\x00\x00\x00\x54\x00\x00\x00\x48\x01\x00\x00\x40\x01\x00\x00\x6C\x00\x00\x00\x75\x00\x00\x00\x9C\x01\x00\x00\xA4\x01\x00\x00\x00\x6E\x00\x00\x00\x46\x00\x00\x00\xC8\x01\x00\x00\x84\x01\x00\x00\x6D\x00\x00\x00\x65\x00\x00\x00\xDC\x01\x00\x00\xBC\x01\x00\x72\x00\x00\x00\x6B\x00\x00\x00\x00
# if the lib receives an update 

# Little advice: Use spaces to center your credits

def CTRPFCredits(CTRPluginFramework, ByNanquitas):
		file = open('C:/devkitPro/libctrpf/lib/libctrpf.a', 'rb+')
		# Check the sizes
		if len(ByNanquitas) >= 12:
			ByNanquitas = ByNanquitas[:12]
		if len(CTRPluginFramework) >= 18:
			CTRPluginFramework = CTRPluginFramework[:18]
		# Edit the credits
		file.seek(0xBD650)
		for i, c in enumerate(list(ByNanquitas.rjust(12, " "))):
			file.write((ord(c) << (i & 0xA)).to_bytes(4, 'little'))
		file.seek(0xBD650 + 12*4)
		for i, c in enumerate(list(CTRPluginFramework.rjust(18, " "))):
			file.write((ord(c) << (i & 0xA)).to_bytes(4, 'little'))
		file.close()

# Example
CTRPFCredits("    Created By    ", "   ZettaD   ")
# https://imgur.com/gTdnBOA

# RIP Nanqutias x')