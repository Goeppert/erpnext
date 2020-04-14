from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'journal_entry',
		'internal_non_standard_fieldnames': {
			'Journal Entry': 'reference_name,reference_name_2',
			'Payment Entry': 'reference_name,reference_name_2',
			'Purchase Invoice': 'reference_name,reference_name_2',
			'Stock Entry': 'reference_name,reference_name_2',
		},
		'transactions': [
			{
				'label': _('References'),
				'items': ['Journal Entry', 'Payment Entry', 'Purchase Invoice', 'Stock Entry']
			}
		]
	}
