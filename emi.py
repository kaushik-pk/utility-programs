from prettytable import PrettyTable

x = PrettyTable();
p = 4950000
r = 0.069
t = 360

is_prepayment = True
# Month must greater than 1 i.e no prepayment in first month
prepayment_month = 24
prepayment_amount = 40000

print('\n\nPrincipal amout - Rs.' + str(p) + '\nRate of interest - ' + str(round(r*100,2)), '%\nTenure - ' + str(round(t/12)) + ' years');

mr = float(1 + (r/12));
emi = round((p*r/12)*( mr**t  / ( mr**t - 1) ));
print("\nYour monthly emi is " + str(emi));

x.field_names = ["Month","Initial Principal", "EMI", "Interest paid", "Principal paid", "Remaining principal", "Prepayment"];
x.add_row([0,p,emi,round(p*r/12,2),round((emi - round(p*r/12,2))),round((p - ( emi - round(p*r/12,2)))),0])

total_interest = 0
monthlyCal = [{
    'mth': 0,
    'pr':p,
    'emi':emi,
    'intp': round(p*r/12,2),
    'prp': round(emi - round(p*r/12,2)),
    'remp': round(p - ( emi - round(p*r/12,2))),
    'prep':0
}];
total_interest = round(total_interest + monthlyCal[0]['intp'],2)

for m in range(1,t):
    init_principal = monthlyCal[m-1]['remp'];
    paying_emi = emi
    if is_prepayment and m >= prepayment_month:
        interest_paid = round(init_principal*r/12,2)
        principal_paid = round(emi - interest_paid) + prepayment_amount
        remaining_principal = init_principal - principal_paid
        paying_emi = paying_emi + prepayment_amount
        if( remaining_principal < 0 ):
            if( init_principal < paying_emi ):
                principal_paid = init_principal
                paying_emi = interest_paid + init_principal
                if( init_principal < emi ):
                    prepayment_amount = 0
                else:
                    prepayment_amount = principal_paid - emi
            else:
                principal_paid = remaining_principal
            remaining_principal = 0
            p = 0
        cal = {
            'mth': m,
            'pr': init_principal,
            'emi':paying_emi,
            'intp': interest_paid,
            'prp': principal_paid,
            'remp': remaining_principal,
            'prep': prepayment_amount
        }
    else:
        interest_paid = round(init_principal*r/12,2)
        principal_paid = round(emi - interest_paid)
        remaining_principal = init_principal - principal_paid
        if( remaining_principal < 0 ):
            principal_paid = init_principal
            if( init_principal < paying_emi ):
                paying_emi = interest_paid + init_principal
            remaining_principal = 0
            p = 0
        cal = {
            'mth': m,
            'pr': init_principal,
            'emi':paying_emi,
            'intp': interest_paid,
            'prp': principal_paid,
            'remp': remaining_principal,
            'prep': 0
        }
    monthlyCal.append(cal)
    total_interest = round(total_interest + cal['intp'],2)
    x.add_row([cal['mth'],cal['pr'],cal['emi'],cal['intp'],cal['prp'],cal['remp'],cal['prep']])
    if p == 0:
        break;
print(x);

print('Total interest paid - ' + str(total_interest))
print('\n\n')