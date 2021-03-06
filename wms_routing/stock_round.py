# -*- coding: utf-8 -*-
##############################################################################
#
#    wms_routing module for OpenERP, This module allows to assing rounds to orders to set default locations automatically on moves
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of wms_routing
#
#    wms_routing is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    wms_routing is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv
from osv import fields


class stock_round(osv.osv):
    _name = 'stock.round'
    _description = 'Stock round'

    _columns = {
        'name': fields.char('Name', size=64, required=True, help='Name of the round'),
        'location_id': fields.many2one('stock.location', 'Destination', help='Location for this round'),
        'company_id': fields.many2one('res.company', 'Company', help='The company of this round'),
    }

stock_round()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
