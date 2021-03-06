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

"""Location Record tests."""

from __future__ import absolute_import, print_function

from utils import get_mapping

from rero_ils.modules.locations.api import Location, LocationsSearch
from rero_ils.modules.locations.api import location_id_fetcher as fetcher


def test_location_create(db, location_data):
    """Test locanisation creation."""
    loc = Location.create(location_data, delete_pid=True)
    assert loc == location_data
    assert loc.get('pid') == '1'

    loc = Location.get_record_by_pid('1')
    assert loc == location_data

    fetched_pid = fetcher(loc.id, loc)
    assert fetched_pid.pid_value == '1'
    assert fetched_pid.pid_type == 'loc'


def test_location_es_mapping(es, db, library, location_data):
    """."""
    search = LocationsSearch()
    mapping = get_mapping(search.Meta.index)
    assert mapping
    Location.create(
        location_data,
        dbcommit=True,
        reindex=True,
        delete_pid=True
    )
    assert mapping == get_mapping(search.Meta.index)


def test_location_get_all_pickup_locations(es, db, library, location):
    """."""
    locations = Location.get_pickup_location_pids()
    assert list(locations)[0] == location.pid


def test_location_can_delete(location):
    """Test can delete"""
    assert location.get_links_to_me() == {}
    assert location.can_delete
