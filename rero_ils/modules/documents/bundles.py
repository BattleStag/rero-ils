# -*- coding: utf-8 -*-
#
# This file is part of RERO ILS.
# Copyright (C) 2017 RERO.
#
# RERO ILS is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# RERO ILS is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RERO ILS; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""JS/CSS bundles for theme."""

from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

from ...bundles import i18n

detailed_js = Bundle(
    i18n,
    NpmBundle(
        'js/rero_ils/translations.js',
        'js/rero_ils/thumbnail.js',
        'js/rero_ils/detailed_app.js',
        filters='requirejs',
        depends=('node_modules/d3/*'),
        npm={
            "almond": "~0.3.1",
            'angular': '~1.4.10',
            'angular-loading-bar': '~0.9.0',
            'd3': '^3.5.17'
        }
    ),
    filters='jsmin',
    output='gen/rero_ils.detailed.%(version)s.js',
)
