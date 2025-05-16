print "Loading Telescope configuration..."

local telescope = require "telescope"
local telescopeConfig = require "telescope.config"

telescope.setup {
  extensions = {
    "fzf",
    "remote-sshfs"
  },
}
