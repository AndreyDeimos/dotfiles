-- This file needs to have same structure as nvconfig.lua
-- https://github.com/NvChad/ui/blob/v3.0/lua/nvconfig.lua
-- Please read that file to know all available options :(

---@type ChadrcConfig
local M = {}
local colors = dofile(vim.g.base46_cache .. "colors")
M.base46 = {
  theme = "catppuccin",

  hl_override = {
    Comment = { italic = true, fg = colors.green },
    ["@comment"] = { italic = true, fg = colors.green },
  },
  hl_add = {
    Tabline = { fg = "NONE", bg = "NONE" },
  },

  transparency = true,
}

return M
