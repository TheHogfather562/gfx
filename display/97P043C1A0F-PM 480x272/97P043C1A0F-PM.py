# coding: utf-8
##############################################################################
# Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################

def instantiateComponent(comp):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/display/97P043C1A0F-PM 480x272"
	comp.setHelpFile("../../docs/help_harmony_gfx_html_alias.h")
	#comp.setHelp("IDH_HTML_GFX_CMP__2__Display_Component")
	
	Name = comp.createStringSymbol("Name", None)
	Name.setLabel("Name")
	Name.setDescription("The display name.")
	Name.setDefaultValue("97P043C1A0F-PM")
	Name.setReadOnly(True)
	
	# System level 
	SYS_DEFINITIONS_H = comp.createFileSymbol("SYS_DEFINITIONS_H", None)
	SYS_DEFINITIONS_H.setType("STRING")
	SYS_DEFINITIONS_H.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	SYS_DEFINITIONS_H.setSourcePath("definitions.h.ftl")
	SYS_DEFINITIONS_H.setMarkup(True)

	SYS_INIT_C = comp.createFileSymbol("SYS_INIT_C", None)
	SYS_INIT_C.setType("STRING")
	SYS_INIT_C.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")
	SYS_INIT_C.setSourcePath("init.c.ftl")
	SYS_INIT_C.setMarkup(True)

	DISP_DRIVER_C = comp.createFileSymbol("DISP_DRIVER_C", None)
	DISP_DRIVER_C.setDestPath("gfx/display/")
	DISP_DRIVER_C.setSourcePath("disp_gfx_97P043C1A0F_PM.c.ftl")
	DISP_DRIVER_C.setOutputName("disp_gfx_97P043C1A0F_PM.c")
	DISP_DRIVER_C.setProjectPath(projectPath)
	DISP_DRIVER_C.setType("SOURCE")
	DISP_DRIVER_C.setMarkup(True)
	
	DISP_DRIVER_H = comp.createFileSymbol("DISP_DRIVER_H", None)
	DISP_DRIVER_H.setSourcePath("disp_gfx_97P043C1A0F_PM.h.ftl")
	DISP_DRIVER_H.setDestPath("gfx/display/")
	DISP_DRIVER_H.setOutputName("disp_gfx_97P043C1A0F_PM.h")
	DISP_DRIVER_H.setProjectPath(projectPath)
	DISP_DRIVER_H.setType("HEADER")
	DISP_DRIVER_H.setMarkup(True)

	DisplayWidth = comp.createIntegerSymbol("DisplayWidth", None)
	DisplayWidth.setLabel("Graphics Display Width")
	DisplayWidth.setDescription("The width of the graphics display in pixels.")
	DisplayWidth.setDefaultValue(480)
	DisplayWidth.setReadOnly(True)
	
	Height = comp.createIntegerSymbol("DisplayHeight", None)
	Height.setLabel("Graphics Display Height")
	Height.setDescription("The height of the graphics display in pixels.")
	Height.setDefaultValue(272)
	Height.setReadOnly(True)
	
	TouchWidth = comp.createIntegerSymbol("TouchWidth", None)
	TouchWidth.setLabel("Touch Panel Width")
	TouchWidth.setDescription("The width of the touch panel in pixels.")
	TouchWidth.setDefaultValue(272)
	TouchWidth.setReadOnly(True)
	
	TouchHeight = comp.createIntegerSymbol("TouchHeight", None)
	TouchHeight.setLabel("Touch Panel Height")
	TouchHeight.setDescription("The height of the touch panel in pixels.")
	TouchHeight.setDefaultValue(480)
	TouchHeight.setReadOnly(True)
	
	DataWidth = comp.createIntegerSymbol("DataWidth", None)
	DataWidth.setLabel("Data Width")
	DataWidth.setDescription("The width of the display data bus in bits.")
	DataWidth.setDefaultValue(16)
	DataWidth.setReadOnly(True)
	
	HorzMenu = comp.createMenuSymbol("HorzMenu", None)
	HorzMenu.setLabel("Horizontal Attributes")
	HorzMenu.setDescription("Contains the display horizontal refresh values.")
	
	HorzPulseWidth = comp.createIntegerSymbol("HorzPulseWidth", HorzMenu)
	HorzPulseWidth.setLabel("Horizontal Pulse Width")
	HorzPulseWidth.setDescription("The horizontal pulse width.")
	HorzPulseWidth.setDefaultValue(41)
	HorzPulseWidth.setReadOnly(True)
	
	HorzBackPorch = comp.createIntegerSymbol("HorzBackPorch", HorzMenu)
	HorzBackPorch.setLabel("Horizontal Back Porch")
	HorzBackPorch.setDescription("The horizontal back porch size in pixels.")
	HorzBackPorch.setDefaultValue(2)
	HorzBackPorch.setReadOnly(True)
	
	HorzFrontPorch = comp.createIntegerSymbol("HorzFrontPorch", HorzMenu)
	HorzFrontPorch.setLabel("Horizontal Front Porch")
	HorzFrontPorch.setDescription("The horizontal front porch size in pixels.")
	HorzFrontPorch.setDefaultValue(2)
	HorzFrontPorch.setReadOnly(True)
	
	VertMenu = comp.createMenuSymbol("VertMenu", None)
	VertMenu.setLabel("Vertical Attributes")
	VertMenu.setDescription("Contains the display vertical refresh values.")
	
	VertPulseWidth = comp.createIntegerSymbol("VertPulseWidth", VertMenu)
	VertPulseWidth.setLabel("Vertical Pulse Width")
	VertPulseWidth.setDescription("The vertical pulse width.")
	VertPulseWidth.setDefaultValue(10)
	VertPulseWidth.setReadOnly(True)
	
	VertBackPorch = comp.createIntegerSymbol("VertBackPorch", VertMenu)
	VertBackPorch.setLabel("Vertical Back Porch")
	VertBackPorch.setDescription("The vertical back porch size in pixels.")
	VertBackPorch.setDefaultValue(2)
	VertBackPorch.setReadOnly(True)
	
	VertFrontPorch = comp.createIntegerSymbol("VertFrontPorch", VertMenu)
	VertFrontPorch.setLabel("Vertical Front Porch")
	VertFrontPorch.setDescription("The vertical front porch size in pixels.")
	VertFrontPorch.setDefaultValue(2)
	VertFrontPorch.setReadOnly(True)
	
	InvLeftShift = comp.createBooleanSymbol("InvLeftShift", None)
	InvLeftShift.setLabel("Inverted Left Shift")
	InvLeftShift.setDescription("Indicates if this display requries inverted left shift.")
	InvLeftShift.setDefaultValue(False)
	InvLeftShift.setReadOnly(True)
	
	BackLightMenu = comp.createMenuSymbol("BackLightMenu", None)
	BackLightMenu.setLabel("Back Light Settings")
	BackLightMenu.setDescription("Contains values for controlling the back light.")
	
	BacklightDisable = comp.createIntegerSymbol("BacklightDisable", BackLightMenu)
	BacklightDisable.setLabel("Back Light Disable Value")
	BacklightDisable.setDescription("The value used to disable the display back light.")
	BacklightDisable.setDefaultValue(0)
	BacklightDisable.setReadOnly(True)
	
	BacklightEnable = comp.createIntegerSymbol("BacklightEnable", BackLightMenu)
	BacklightEnable.setLabel("Back Light Enable Value")
	BacklightEnable.setDescription("The value used to enable the display back light.")
	BacklightEnable.setDefaultValue(1)
	BacklightEnable.setReadOnly(True)
	
	PolarityMenu = comp.createMenuSymbol("PolarityMenu", None)
	PolarityMenu.setLabel("Polarity Settings")
	PolarityMenu.setDescription("Contains the display polarity values.")
	
	HSYNCNegative = comp.createBooleanSymbol("HSYNCNegative", PolarityMenu)
	HSYNCNegative.setLabel("HSYNC Negative?")
	HSYNCNegative.setDescription("Indicates if this display requries negative HSYNC polarity.")
	HSYNCNegative.setDefaultValue(False)
	HSYNCNegative.setReadOnly(True)
	
	VSYNCNegative = comp.createBooleanSymbol("VSYNCNegative", PolarityMenu)
	VSYNCNegative.setLabel("VSYNC Negative?")
	VSYNCNegative.setDescription("Indicates if this display requries negative VSYNC polarity.")
	VSYNCNegative.setDefaultValue(False)
	VSYNCNegative.setReadOnly(True)
	
	DataEnable = comp.createBooleanSymbol("DataEnable", None)
	DataEnable.setLabel("Use Data Enable?")
	DataEnable.setDescription("Indicates if this display requries the use of the Data Enable line.")
	DataEnable.setDefaultValue(True)
	DataEnable.setReadOnly(True)
	
	DataEnablePolarity = comp.createBooleanSymbol("DataEnablePolarity", None)
	DataEnablePolarity.setLabel("Data Enable Polarity Positive?")
	DataEnablePolarity.setDescription("Indicates if this display Data Enable polarity is positive.")
	DataEnablePolarity.setDefaultValue(True)
	DataEnablePolarity.setReadOnly(True)
	
	UseReset = comp.createBooleanSymbol("UseReset", None)
	UseReset.setLabel("Use Reset?")
	UseReset.setDescription("Indicates if this display reset line should be used.")
	UseReset.setDefaultValue(True)
	UseReset.setReadOnly(True)
	
	ResetPolarity = comp.createBooleanSymbol("ResetPolarity", None)
	ResetPolarity.setLabel("Reset Polarity Positive?")
	ResetPolarity.setDescription("Indicates if this display reset line should be reset positive.")
	ResetPolarity.setDefaultValue(True)
	ResetPolarity.setReadOnly(True)
	
	UseChipSelect = comp.createBooleanSymbol("UseChipSelect", None)
	UseChipSelect.setLabel("Use Chip Select?")
	UseChipSelect.setDescription("Indicates if this display uses the chip select line.")
	UseChipSelect.setDefaultValue(False)
	UseChipSelect.setReadOnly(True)
	
	ChipSelectPolarity = comp.createBooleanSymbol("ChipSelectPolarity", None)
	ChipSelectPolarity.setLabel("Chip Select Polarity Positive?")
	ChipSelectPolarity.setDescription("Indicates if this display chip select line should be positive.")
	ChipSelectPolarity.setDefaultValue(True)
	ChipSelectPolarity.setReadOnly(True)
