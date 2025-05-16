require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("i", "jk", "<ESC>")
map({ "n", "i" }, "<C-k>", vim.lsp.buf.signature_help)
map({ "n" }, "<leader>ra", vim.lsp.buf.rename)

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")

-- mouse users + nvimtree users!
vim.keymap.set("n", "<RightMouse>", function()
  vim.cmd.exec '"normal! \\<RightMouse>"'

  local options = vim.bo.ft == "NvimTree" and "nvimtree" or "default"
  require("menu").open(options, { mouse = true })
end, {})
