output = [
         'WA-01', 'WA-02',
         'WA-03', 'WA-04',
         'WA-05', 'WA-06',
         'WA-07', 'WA-08',
         'WA-09', 'WA-10', 'WV-01', 'WV-02', 'WV-03', 'WI-01', 'WI-02',
         'WI-03', 'WI-04',
         'WI-05', 'WI-06',
         'WI-07', 'WI-08', 'WY-01' ]

for value in output:
	print(" {\"value\":\"%s\",\"value2\":\"%s-1010\",\"office_code\":\"%s\",\"can_create_update_delete_orders\":\"N\",\"can_update_status_for\":\"%s\",\"can_update_values_for\":\"NONE\",\"is_admin\":\"N\"}," % (value, value, value, value))
