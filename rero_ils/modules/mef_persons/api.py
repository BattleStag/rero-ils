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

"""API for manipulating documents."""

from functools import partial

from invenio_search.api import RecordsSearch

from .models import MefPersonIdentifier
from ..api import IlsRecord
from ..fetchers import id_fetcher
from ..minters import id_minter
from ..providers import Provider

# provider
MefPersonProvider = type(
    'MefPersonProvider',
    (Provider,),
    dict(identifier=MefPersonIdentifier, pid_type='pers')
)
# minter
mef_person_id_minter = partial(id_minter, provider=MefPersonProvider)
# fetcher
mef_person_id_fetcher = partial(id_fetcher, provider=MefPersonProvider)


class MefPersonsSearch(RecordsSearch):
    """Mef person search."""

    class Meta():
        """Meta class."""

        index = 'persons'


class MefPerson(IlsRecord):
    """MefPerson class."""

    minter = mef_person_id_minter
    fetcher = mef_person_id_fetcher
    provider = MefPersonProvider

    @classmethod
    def create_or_update(
        cls,
        data,
        id_=None,
        dbcommit=False,
        reindex=False,
        delete_pid=False,
        **kwargs
    ):
        """Create or update mef person record."""
        pid = data.get('pid')
        record = cls.get_record_by_pid(pid, with_deleted=False)
        if record:
            record.update(data, dbcommit=dbcommit, reindex=reindex)
            return record, 'updated'
        else:
            created_record = cls.create(
                data,
                delete_pid=delete_pid,
                dbcommit=dbcommit,
                reindex=reindex,
            )
            return created_record, 'created'
