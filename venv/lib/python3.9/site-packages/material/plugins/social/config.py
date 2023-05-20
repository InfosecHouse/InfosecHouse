# Copyright (c) 2016-2023 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import os

from mkdocs.config.base import Config
from mkdocs.config.config_options import Deprecated, Type

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Social plugin configuration scheme
class SocialConfig(Config):
    enabled = Type(bool, default = True)
    concurrency = Type(int, default = os.cpu_count())

    # Options for caching
    cache = Type(bool, default = True)
    cache_dir = Type(str, default = ".cache/plugin/social")

    # Options for cards
    cards = Type(bool, default = True)
    cards_dir = Type(str, default = "assets/images/social")
    cards_layout_dir = Type(str, default = "layouts")
    cards_layout = Type(str, default = "default")
    cards_layout_options = Type(dict, default = {})

    # Options for debugging
    debug = Type(bool, default = False)
    debug_grid = Type(bool, default = True)
    debug_grid_step = Type(int, default = 32)
    debug_color = Type(str, default = "grey")

    # Deprecated options
    cards_color = Deprecated(
        message =
            "Deprecated, use 'cards_layout_options.background_color' "
            "and 'cards_layout_options.color' with 'default' layout"
        )
    cards_font = Deprecated(
        message = "Deprecated, use 'cards_layout_options.font_family'"
    )
