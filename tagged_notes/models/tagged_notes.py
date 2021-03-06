# -*- coding: utf-8 -*-
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import _, fields, models


class NotesTags(models.Model):
    _name = 'notes.tag'
    _description = 'Tags for notes'

    # fields
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True, required=True)

    _sql_constraints = [
        ('notes_tags_uniq', 'unique(name)', 'You cannot have duplicate tags for notes'),
    ]


class NotesTagged(models.Model):
    _name = 'notes.tagged'
    _description = 'Tagged notes'

    # fields
    note = fields.Char('Note', required=True)
    tag_id = fields.Many2one('notes.tag', string='Note Tag', required=True, ondelete='restrict', delegate=True)
    original_note_id = fields.Many2one('notes.tagged', string='Replaces', ondelete='restrict')
    active = fields.Boolean('Active', default=True, required=True)
