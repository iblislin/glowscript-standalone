Glowscript Standalone Example
===============================================================================

This repo show the glowscript standalone example. We do not need the ide from
`glowscript.org <http://www.glowscript.org>`_.

e.g.::

    $ cd sphere-vpy
    $ python -m http.server

Then go on your browser http://localhost:8000 and enjoy!

The file ``sphere-vpy/js/app.js`` is a good start point.
Note that there is a var named ``code`` at the top of the js file.
Just change it to your real vpython code. The ``code`` should be a big string
contain all your vpython program. Just including ``\n`` in the string do the
mulit-line trick.
