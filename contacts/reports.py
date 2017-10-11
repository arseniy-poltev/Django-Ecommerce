import datetime
from printing_tools.documents import SuzysDocument

def commission_report(agent):
    ''' return pdf with commission report '''
    report = SuzysDocument()

    order_list, commission_total = agent.comission_owed()
    agent_name = '{} {}'.format(agent.contact_first_name, agent.contact_name)

    ## title and instructions
    report.add_title('Commission report {} {}'.format(
        agent_name,
        datetime.date.today().strftime('%d/%m/%Y')))

    ## Commission details
    report.add_heading('Commission Detail')
    table_headers = ['Order #', 'Client Name', 'Date Ordered', 'Date Paid', 'Order Amount']
    col_widths = [0.12, 0.33, 0.18, 0.18, 0.19]
    table_data = []

    table_data.append(table_headers)
    for order in order_list:
        table_data.append([
            order[u'order #'],
            order[u'client name'],
            order[u'order data'],
            order[u'date paid'],
            order[u'sale total'],
            ])
    report.add_table(table_data, col_widths)

    report.add_body_text(u'Commission total: {}'.format(commission_total))
    report.add_body_text('Please send your commission-note to S-Company ltd with this document attached')

    return report.print_document()