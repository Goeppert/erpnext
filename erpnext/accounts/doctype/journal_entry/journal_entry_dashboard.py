from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'journal_entry',
		'internal_ref_type_links': {
			'Journal Entry': ['journal_entry_ref', 'ref_name'],
			'Payment Entry': ['journal_entry_ref', 'ref_name'],
			'Purchase Invoice': ['journal_entry_ref', 'ref_name'],
			'Stock Entry': ['journal_entry_ref', 'ref_name'],
		},
		'transactions': [
			{
				'label': _('References'),
				'items': ['Journal Entry', 'Payment Entry', 'Purchase Invoice', 'Stock Entry']
			}
		]
	}
