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
    

class TorresBorderlessIkoriaTemplate (temp.NormalTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresBorderlessIkoria"
    template_suffix = "Borderless Ikoria"

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


class TorresStainedGlassTemplate (temp.NormalTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresStainedGlass"
    template_suffix = "Stained Glass"

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


class TorresSignatureBasicLandTemplate (temp.BasicLandTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresSignatureBasic"
    template_suffix = "Signature Basic"

    def __init__(self, layout):
        cfg.save_artist_name = True
        cfg.real_collector = False
        super().__init__(layout)

    @property
    def art_reference(self) -> str:
        return con.layers.BASIC_ART_FRAME

    @cached_property
    def text_layers(self) -> Optional[LayerSet]:
        return self.app.activeDocument

    def enable_frame_layers(self):
        psd.getLayer(self.layout.name).visible = True


class TorresJapaneseBasicLandTemplate (temp.BasicLandTemplate):
    """
     * Created by TorresVisuals
    """
    template_file_name = "TorresVisuals/TorresJapaneseBasic"
    template_suffix = "Japanese Basic"

    def __init__(self, layout):
        cfg.save_artist_name = True
        cfg.real_collector = False
        super().__init__(layout)

    @property
    def art_reference(self) -> str:
        return con.layers.BASIC_ART_FRAME

    @cached_property
    def text_layers(self) -> Optional[LayerSet]:
        return self.app.activeDocument

    def enable_frame_layers(self):
        psd.getLayer(self.layout.name).visible = True