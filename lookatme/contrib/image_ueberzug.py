"""
An image renderer that uses ueberzug
"""

import os
import time
import urwid
import ueberzug.lib.v0 as ueberzug
import urwid_ueberzogen as uw_uz


from lookatme.exceptions import IgnoredByContrib

CANVAS = None

def root_urwid_widget(to_wrap):
    global CANVAS
    CANVAS = ueberzug.Canvas().__enter__()
    return uw_uz.Container(CANVAS, urwid.Pile([to_wrap]), visibility=ueberzug.Visibility.VISIBLE)


def image(link_uri, title, text):
    link_uri = os.path.abspath(os.path.expanduser(link_uri))
    if not os.path.exists(link_uri):
        raise Exception("Local files only for images! (for now) {!r}".format(link_uri))
    placement = CANVAS.create_placement(
        time.time(),
        path=link_uri,
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
