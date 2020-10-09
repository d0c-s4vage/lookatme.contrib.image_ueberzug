# lookatme.contrib.image_ueberzug

This is a [lookatme](https://github.com/d0c-s4vage/lookatme) extension that
uses [ueberzug](https://github.com/seebye/ueberzug) and
[urwid-ueberzogen](https://github.com/seebye/urwid-ueberzogen/tree/master/urwid_ueberzogen)
to provide image rendering support. This works on linux only (or wherever
ueberzug functions).


After successfully installing, you should see something like this:

![example](example/running.gif)

## Installation

```bash
pip install lookatme.contrib.image_ueberzug
```

## Usage

Use images! For now, only local images are supported. Remote image support
will be added later.

Enable this plugin by adding it to the metadata in the head of the markdown file.

```txt
---
title: <title>
author: <author>
extensions:
  - image_ueberzug
---
```

Use the text of the image to indicate the height (number of rows) that the
image should use when rendered. The example below will render
`path/to/image.png` with a height of `7` rows:

```
![7](path/to/image.png)
```
