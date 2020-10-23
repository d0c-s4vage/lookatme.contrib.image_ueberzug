"""
An image renderer that uses ueberzug
"""

import os
import time
import urwid
import ueberzug.lib.v0 as ueberzug
import urwid_ueberzogen as uw_uz


import lookatme.config
from lookatme.exceptions import IgnoredByContrib

CANVAS = None


def user_warnings():
    """No user warnings for this extension
    """
    return []


def root_urwid_widget(to_wrap):
    global CANVAS
    CANVAS = ueberzug.Canvas().__enter__()
    return uw_uz.Container(CANVAS, urwid.Pile([to_wrap]), visibility=ueberzug.Visibility.VISIBLE)


def image(link_uri, title, text):
    base_dir = lookatme.config.SLIDE_SOURCE_DIR
    full_path = os.path.join(base_dir, link_uri)

    if not os.path.exists(full_path):
        raise Exception("Local files only for images! (for now) {!r}".format(link_uri))
    placement = CANVAS.create_placement(
        time.time(),
        path=full_path,
        scaler=ueberzug.ScalerOption.FIT_CONTAIN.value,
    )
    try:
        height = int(text)
    except:
        height = 30
    blank_box = urwid.BoxAdapter(urwid.SolidFill(" "), height=height)
    img = uw_uz.Image(placement, blank_box)
    return [img]


def shutdown():
    if CANVAS is None:
        return
    CANVAS.__exit__()
