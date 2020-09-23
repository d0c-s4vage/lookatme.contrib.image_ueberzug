"""
An image renderer that uses ueberzug
"""

import urwid
import ueberzug.lib.v0 as ueberzug
import urwid_ueberzogen as uw_uz
import time


from lookatme.exceptions import IgnoredByContrib

CANVAS = None

def root_urwid_widget(to_wrap):
    global CANVAS
    CANVAS = ueberzug.Canvas().__enter__()
    return uw_uz.Container(CANVAS, urwid.Pile([to_wrap]), visibility=ueberzug.Visibility.VISIBLE)


def image(link_uri, title, text):
    placement = CANVAS.create_placement(time.time(), path="/home/saitama/Downloads/gitlab_logo.png")
    blank_box = urwid.Pile([urwid.Text("") for x in range(15)])
    img = uw_uz.Image(placement, blank_box)
    return [img]
