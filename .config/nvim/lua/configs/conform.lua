local options = {
  formatters_by_ft = {
    -- css = { "prettier" },
    -- html = { "prettier" },
    python = { "ruff_format" },
    cpp = { "clang-format" },
  },

  format_on_save = {
    -- These options will be passed to conform.format()
    timeout_ms = 500,
    lsp_fallback = false,
  },
}

return options
