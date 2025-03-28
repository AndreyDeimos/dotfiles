-- ~/.config/nvim/lua/custom/options.lua

require "nvchad.options"
require("lspconfig.ui.windows").default_options.border = "solid"

-- Basic options
vim.opt.wrap = false
vim.opt.relativenumber = true
vim.opt.foldlevel = 99
-- vim.g.markdown_folding = 1

-- Add other customizations below

-- add yours here!

-- local o = vim.o
-- o.cursorlineopt ='both' -- to enable cursorline!
