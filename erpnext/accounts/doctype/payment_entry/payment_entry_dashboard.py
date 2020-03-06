from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'payment_entry',
		'non_standard_fieldnames': {
			'Journal Entry': 'reference_name,reference_name_2',
		},
		'transactions': [
			{
				'label': _('Payment'),
				'items': ['Journal Entry']
			}
		]
	}
