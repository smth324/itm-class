'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''

def savings(gross_pay, tax_rate, expenses):
    return int(gross_pay * (1-tax_rate)) - expenses

def material_waste(total_material, material_units, num_jobs, job_consumption):
    return str(total_material - (num_jobs*job_consumption)) + material_units


def interest(principal, rate, periods):
    return int(principal + principal*rate*periods)