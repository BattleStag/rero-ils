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

"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

import pytest
from utils import flush_index

from rero_ils.modules.libraries.api import LibrariesSearch, Library
from rero_ils.modules.locations.api import Location, LocationsSearch


@pytest.fixture(scope="module")
def create_app():
    """Create test app."""
    from invenio_app.factory import create_api

    return create_api


@pytest.fixture(scope="module")
def library(app, organisation, library_data):
    """."""
    lib = Library.create(
        data=library_data,
        delete_pid=False,
        dbcommit=True,
        reindex=True)
    flush_index(LibrariesSearch.Meta.index)
    return lib


@pytest.fixture(scope="module")
def location(library, location_data):
    """."""
    loc = Location.create(
        data=location_data,
        delete_pid=False,
        dbcommit=True,
        reindex=True)
    flush_index(LocationsSearch.Meta.index)
    return loc
