"""
TORRESVISUALS TEMPLATES
"""
import os
from functools import cached_property

import proxyshop.text_layers as text_classes
from proxyshop.__console__ import console
from proxyshop import templates as temp
from proxyshop import format_text as ft
from proxyshop.constants import con
from proxyshop.settings import cfg
from typing import Optional
import proxyshop.helpers as psd

from photoshop.api._layerSet import LayerSet
from photoshop.api._artlayer import ArtLayer
import photoshop.api as ps
app = ps.Application()


    class TorresNinjaFullartTemplate (temp.NormalTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresNinjaFullart"
    template_suffix = "Ninja Fullart"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return
    

class TorresNeonTemplate (temp.NormalTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresNeon"
    template_suffix = "Neon"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return
    
    class TorresCrystallTemplate (temp.NormalTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresCrystall"
    template_suffix = "Crystall"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return