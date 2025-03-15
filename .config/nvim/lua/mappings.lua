require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("n", ";", ":", { desc = "CMD enter command mode" })
map("i", "jk", "<ESC>")
vim.keymap.set("n", "K", function()
  vim.lsp.buf.hover {
    border = "double",
  }
end)
map({ "n", "i" }, "<C-k>", vim.lsp.buf.signature_help)

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")

-- mouse users + nvimtree users!
vim.keymap.set("n", "<RightMouse>", function()
  vim.cmd.exec '"normal! \\<RightMouse>"'

  local options = vim.bo.ft == "NvimTree" and "nvimtree" or "default"
  require("menu").open(options, { mouse = true })
end, {})
