#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.utils.translation import ugettext_lazy as _
from common.utils import Choice


class SUBSCRIBER_STATUS(Choice):
    PENDING = 1, _('PENDING')
    PAUSE = 2, _('PAUSE')
    ABORT = 3, _('ABORT')
    FAIL = 4, _('FAIL')
    SENT = 5, _('SENT')
    IN_PROCESS = 6, _('IN PROCESS')
    NOT_AUTHORIZED = 7, _('NOT AUTHORIZED')
    COMPLETED = 8, _('COMPLETED')


class CAMPAIGN_STATUS(Choice):
    START = 1, _('START')
    PAUSE = 2, _('PAUSE')
    ABORT = 3, _('ABORT')
    END = 4, _('END')

CAMPAIGN_STATUS_COLOR = {1: "green", 2: "blue", 3: "orange", 4: "red"}


class CAMPAIGN_COLUMN_NAME(Choice):
    key = _('key')
    name = _('name')
    start_date = _('start date')
    type = _('type')
    app = _('app')
    contacts = _('contacts')
    status = _('status')


class AMD_BEHAVIOR(Choice):
    ALWAYS = 1, _('ALWAYS PLAY MESSAGE')
    HUMAN_ONLY = 2, _('PLAY MESSAGE TO HUMAN ONLY')
    VOICEMAIL_ONLY = 3, _('LEAVE MESSAGE TO VOICEMAIL ONLY')
