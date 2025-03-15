-- load defaults i.e lua_lsp

local handlers = {
  ["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, { border = "solid" }),
  ["textDocument/signatureHelp"] = vim.lsp.with(vim.lsp.handlers.signature_help, { border = "solid" }),
}

require("nvchad.configs.lspconfig").defaults()
require("lspconfig.ui.windows").default_options.border = "double"

local lspconfig = require "lspconfig"

-- EXAMPLE
local servers = { "html", "cssls", "pyright", "clangd", "nil_ls", "arduino_language_server" }
local nvlsp = require "nvchad.configs.lspconfig"

-- lsps with default config
for _, lsp in ipairs(servers) do
  lspconfig[lsp].setup {
    on_attach = nvlsp.on_attach,
    on_init = nvlsp.on_init,
    capabilities = nvlsp.capabilities,
    handlers = handlers,
  }
end

lspconfig["clangd"].setup {
  -- ...
  init_options = {
    -- ...
    completion = {
      placeholder = false,
    },
  },
}
lspconfig["pyright"].setup {
  settings = {
    python = {
      analysis = {
        typeCheckingMode = "off",
        docstringFormat = "numpy",
      },
    },
  },
}

-- configuring single server, example: typescript
-- lspconfig.ts_ls.setup {
--   on_attach = nvlsp.on_attach,
--   on_init = nvlsp.on_init,
--   capabilities = nvlsp.capabilities,
-- }
