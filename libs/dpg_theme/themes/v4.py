# Author: Giuseppe
from __future__ import annotations

from typing import Optional, Sequence

import dearpygui.dearpygui as dpg

name = """V4"""
styles: dict[int, Sequence[float]] = {
    dpg.mvStyleVar_Alpha: [1.0],
    dpg.mvStyleVar_WindowPadding: [8.0, 8.0],
    dpg.mvStyleVar_WindowRounding: [3.0],
    dpg.mvStyleVar_WindowBorderSize: [0.0],
    dpg.mvStyleVar_WindowMinSize: [30.0, 30.0],
    dpg.mvStyleVar_WindowTitleAlign: [0.5, 0.5],
    dpg.mvStyleVar_ChildRounding: [3.0],
    dpg.mvStyleVar_ChildBorderSize: [1.0],
    dpg.mvStyleVar_PopupRounding: [3.0],
    dpg.mvStyleVar_PopupBorderSize: [0.0],
    dpg.mvStyleVar_FramePadding: [5.0, 3.5],
    dpg.mvStyleVar_FrameRounding: [3.0],
    dpg.mvStyleVar_FrameBorderSize: [0.0],
    dpg.mvStyleVar_ItemSpacing: [5.0, 4.0],
    dpg.mvStyleVar_ItemInnerSpacing: [5.0, 5.0],
    dpg.mvStyleVar_CellPadding: [4.0, 2.0],
    dpg.mvStyleVar_IndentSpacing: [5.0],
    dpg.mvStyleVar_ScrollbarSize: [15.0],
    dpg.mvStyleVar_ScrollbarRounding: [3.0],
    dpg.mvStyleVar_GrabMinSize: [15.0],
    dpg.mvStyleVar_GrabRounding: [3.0],
    dpg.mvStyleVar_TabRounding: [3.0],
    dpg.mvStyleVar_ButtonTextAlign: [0.5, 0.5],
    dpg.mvStyleVar_SelectableTextAlign: [0.0, 0.0],
}
colors: dict[int, Sequence[int, int, int, Optional[int]]] = {
    dpg.mvThemeCol_Text: [255, 255, 255, 255],
    dpg.mvThemeCol_TextDisabled: [255, 255, 255, 91],
    dpg.mvThemeCol_WindowBg: [25, 25, 25, 50],
    dpg.mvThemeCol_ChildBg: [25, 25, 25, 100],
    dpg.mvThemeCol_PopupBg: [25, 25, 25, 255],
    dpg.mvThemeCol_Border: [108, 97, 146, 140],
    dpg.mvThemeCol_BorderShadow: [0, 0, 0, 0],
    dpg.mvThemeCol_FrameBg: [25, 25, 25, 100],
    dpg.mvThemeCol_FrameBgHovered: [97, 108, 146, 140],
    dpg.mvThemeCol_FrameBgActive: [18, 18, 18, 255],
    dpg.mvThemeCol_TitleBg: [25, 25, 25, 255],
    dpg.mvThemeCol_TitleBgActive: [25, 25, 25, 255],
    dpg.mvThemeCol_TitleBgCollapsed: [66, 66, 66, 0],
    dpg.mvThemeCol_MenuBarBg: [0, 0, 0, 0],
    dpg.mvThemeCol_ScrollbarBg: [40, 40, 40, 0],
    dpg.mvThemeCol_ScrollbarGrab: [40, 40, 40, 255],
    dpg.mvThemeCol_ScrollbarGrabHovered: [60, 60, 60, 255],
    dpg.mvThemeCol_ScrollbarGrabActive: [75, 75, 75, 255],
    dpg.mvThemeCol_CheckMark: [75, 75, 75, 255],
    dpg.mvThemeCol_SliderGrab: [18, 18, 18, 255],
    dpg.mvThemeCol_SliderGrabActive: [208, 197, 246, 140],
    dpg.mvThemeCol_Button: [18, 18, 18, 140],
    dpg.mvThemeCol_ButtonHovered: [188, 177, 226, 140],
    dpg.mvThemeCol_ButtonActive: [208, 197, 246, 140],
    dpg.mvThemeCol_Header: [18, 18, 18, 255],
    dpg.mvThemeCol_HeaderHovered: [188, 177, 226, 140],
    dpg.mvThemeCol_HeaderActive: [208, 197, 246, 140],
    dpg.mvThemeCol_Separator: [64, 64, 67, 140],
    dpg.mvThemeCol_SeparatorHovered: [188, 177, 226, 140],
    dpg.mvThemeCol_SeparatorActive: [208, 197, 246, 140],
    dpg.mvThemeCol_ResizeGrip: [18, 18, 18, 255],
    dpg.mvThemeCol_ResizeGripHovered: [188, 177, 226, 140],
    dpg.mvThemeCol_ResizeGripActive: [208, 197, 246, 140],
    dpg.mvThemeCol_Tab: [18, 18, 18, 255],
    dpg.mvThemeCol_TabHovered: [188, 177, 226, 140],
    dpg.mvThemeCol_TabActive: [208, 197, 246, 140],
    dpg.mvThemeCol_TabUnfocused: [0, 115, 255, 0],
    dpg.mvThemeCol_TabUnfocusedActive: [34, 66, 108, 0],
    dpg.mvThemeCol_PlotLines: [108, 97, 146, 255],
    dpg.mvThemeCol_PlotLinesHovered: [108, 97, 146, 140],
    dpg.mvThemeCol_PlotHistogram: [108, 97, 146, 255],
    dpg.mvThemeCol_PlotHistogramHovered: [188, 177, 226, 140],
    dpg.mvThemeCol_TableHeaderBg: [48, 48, 51, 255],
    dpg.mvThemeCol_TableBorderStrong: [108, 97, 146, 140],
    dpg.mvThemeCol_TableBorderLight: [108, 97, 146, 74],
    dpg.mvThemeCol_TableRowBg: [0, 0, 0, 0],
    dpg.mvThemeCol_TableRowBgAlt: [255, 255, 255, 8],
    dpg.mvThemeCol_TextSelectedBg: [188, 177, 226, 140],
    dpg.mvThemeCol_DragDropTarget: [255, 255, 0, 229],
    dpg.mvThemeCol_NavHighlight: [0, 0, 0, 255],
    dpg.mvThemeCol_NavWindowingHighlight: [255, 255, 255, 178],
    dpg.mvThemeCol_NavWindowingDimBg: [204, 204, 204, 51],
    dpg.mvThemeCol_ModalWindowDimBg: [204, 204, 204, 89],
}
