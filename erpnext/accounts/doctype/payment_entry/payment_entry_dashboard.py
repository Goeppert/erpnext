from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'payment_entry',
		'non_standard_fieldnames': {
			'Journal Entry': 'ref_name',
		},
		'transactions': [
			{
				'label': _('Payment'),
				'items': ['Journal Entry']
			}
		]
	}
