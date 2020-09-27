# lookatme.contrib.image_ueberzug

This is a [lookatme](https://github.com/d0c-s4vage/lookatme) extension that
uses [ueberzug](https://github.com/seebye/ueberzug) and
[urwid-ueberzogen](https://github.com/seebye/urwid-ueberzogen/tree/master/urwid_ueberzogen)
to provide image rendering support.

## ⚠️  PROOF OF CONCEPT STATUS ⚠️

This extension is very much still a proof of concept and relies on lookatme
features that haven't been released.

To test it out:

* Checkout the lookatme branch `feature/101-allow_inline_render_fns_widget`
* Install lookatme into a virtual environment
* Install this extension
* Try to render an image!

```
git clone https://github.com/d0c-s4vage/lookatme.contrib.image_ueberzug
cd lookatme.contrib.image_ueberzug
virtualenv /tmp/venv
. /tmp/venv/bin/activate
pip install -r requirements.txt
lookatme example/galaxies.md
```

## Installation

If this project has been pushed up to pypi:

```bash
pip install lookatme.contrib.image_ueberzug
```

otherwise:

```bash
pip install ./path/to/lookatme.contrib.image_ueberzug
```

## Usage

Add the image_ueberzug into the extensions array in the
slide YAML header:

```markdown
---
title: A title
author: Me
date: 2019-12-04
extensions:
  - image_ueberzug
---
```

With the extension installed and declared in the YAML header, images in the
markdown will be rendered with ueberzug!
