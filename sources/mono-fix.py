import fontlab
import fontgate

font = fontlab.CurrentFont()

print font.info.postscriptIsFixedPitch
print font.info.openTypeOS2Panose

font.info.postscriptIsFixedPitch = True
font.info.openTypeOS2Panose = [2, 0, 0, 9, 0, 0, 0, 0, 0, 0]

print font.info.postscriptIsFixedPitch
print font.info.openTypeOS2Panose