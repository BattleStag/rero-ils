# -*- coding: utf-8 -*-
#
# This file is part of RERO ILS.
# Copyright (C) 2018 RERO.
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

"""Blueprint used for loading templates."""

from __future__ import absolute_import, print_function

from functools import wraps

from flask import Blueprint, jsonify

from ..patron_types.api import PatronType
from ..patrons.api import current_patron
from ...permissions import login_and_librarian

blueprint = Blueprint(
    'patron_types',
    __name__,
    template_folder='templates',
    static_folder='static',
)


def check_permission(fn):
    """."""
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        """."""
        login_and_librarian()
        return fn(*args, **kwargs)
    return decorated_view


@blueprint.route('/patron_types/name/validate/<name>', methods=["GET"])
@check_permission
def name_validate(name):
    """Patron type name Validate."""
    response = {
        'name': None
    }
    if current_patron:
        patron_type = PatronType.exist_name_and_organisation_pid(
            name,
            current_patron.organisation.pid
        )
        if patron_type:
            response = {
                'name': patron_type.name
            }
    return jsonify(response)
