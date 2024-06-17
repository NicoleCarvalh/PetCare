import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
import matplotlib.pyplot as plt
from backend.endpoints.clients import get_clients_list
from backend.endpoints.products import get_products_list
from backend.endpoints.sales import get_sales_list
from backend.endpoints.employees import get_employees_list

def fetch_report_data():
    sales_data = get_sales_list()
    products_data = get_products_list()
    
    # Calculate total sales
    total_sales = sum(sale['total'] for sale in sales_data)
    
    # Calculate total products sold and most sold product
    product_sales = {}
    for sale in sales_data:
        for product in sale['products']:
            product_id = product['product_id']
            quantity = product['quantity']
            if product_id in product_sales:
                product_sales[product_id] += quantity
            else:
                product_sales[product_id] = quantity

    most_sold_product = max(product_sales, key=product_sales.get)
    most_sold_product_name = next(p['name'] for p in products_data if p['id'] == most_sold_product)
    total_products_sold = sum(product_sales.values())

    # Calculate average ticket
    average_ticket = total_sales / len(sales_data) if sales_data else 0

    # Daily sales analysis
    daily_sales = {}
    for sale in sales_data:
        sale_date = sale['date_time'].split("T")[0]
        total = sale['total']
        if sale_date in daily_sales:
            daily_sales[sale_date] += total
        else:
            daily_sales[sale_date] = total

    daily_sales_list = []
    sorted_dates = sorted(daily_sales.keys())
    for i, date in enumerate(sorted_dates):
        total = daily_sales[date]
        if i == 0:
            variation = 0
        else:
            previous_total = daily_sales[sorted_dates[i - 1]]
            variation = ((total - previous_total) / previous_total) * 100 if previous_total != 0 else 0
        daily_sales_list.append({'data': date, 'total': total, 'variacao': round(variation, 2)})

    # Payment methods analysis
    payment_methods = {}
    for sale in sales_data:
        payment_method = sale['payment_method']
        if payment_method in payment_methods:
            payment_methods[payment_method] += sale['total']
        else:
            payment_methods[payment_method] = sale['total']

    payment_methods_list = [{'method': method, 'total': total} for method, total in payment_methods.items()]

    return {
        'total_vendas': total_sales,
        'produtos_vendidos': [{'nome': next(p['name'] for p in products_data if p['id'] == k), 'quantidade': v} for k, v in product_sales.items()],
        'ticket_medio': average_ticket,
        'produto_mais_vendido': most_sold_product_name,
        'vendas_diarias': daily_sales_list,
        'metodos_pagamento': payment_methods_list,
    }

def generate_pdf(report_data, filename="report.pdf"):
    # Configurar o documento PDF
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph("Relatório de Vendas", styles['Title']))

    # Introdução
    elements.append(Paragraph("Este relatório apresenta uma análise detalhada das vendas e desempenho dos produtos para o período selecionado.", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Resumo Executivo
    elements.append(Paragraph("Resumo Executivo", styles['Heading2']))
    elements.append(Paragraph(f"Total de Vendas: R$ {report_data['total_vendas']:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Produtos Vendidos: {sum(produto['quantidade'] for produto in report_data['produtos_vendidos'])}", styles['Normal']))
    elements.append(Paragraph(f"Ticket Médio: R$ {report_data['ticket_medio']:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Produto Mais Vendido: {report_data['produto_mais_vendido']}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Análise de Vendas Diárias
    elements.append(Paragraph("Análise de Vendas Diárias", styles['Heading2']))
    sales_data = [["Data", "Total de Vendas", "Variação %"]]
    for data in report_data['vendas_diarias']:
        sales_data.append([data['data'], f"R$ {data['total']:.2f}", f"{data['variacao']}%"])
    t = Table(sales_data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Análise de Produtos Vendidos
    elements.append(Paragraph("Análise de Produtos Vendidos", styles['Heading2']))
    products_data = [["Produto", "Quantidade Vendida"]]
    for produto in report_data['produtos_vendidos']:
        products_data.append([produto['nome'], produto['quantidade']])
    t = Table(products_data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Análise de Métodos de Pagamento
    elements.append(Paragraph("Análise de Métodos de Pagamento", styles['Heading2']))
    payment_data = [["Método de Pagamento", "Total Vendido"]]
    for metodo in report_data['metodos_pagamento']:
        payment_data.append([metodo['method'], f"R$ {metodo['total']:.2f}"])
    t = Table(payment_data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Gráfico de Exemplo
    elements.append(Paragraph("Gráfico de Vendas", styles['Heading2']))

    # Gerar um gráfico com matplotlib
    buffer = io.BytesIO()
    plt.figure(figsize=(6, 4))
    dates = [data['data'] for data in report_data['vendas_diarias']]
    sales = [data['total'] for data in report_data['vendas_diarias']]
    plt.plot(dates, sales, marker='o')
    plt.title('Total de Vendas Diárias')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas')
    plt.grid(True)
    plt.savefig(buffer, format='PNG')
    buffer.seek(0)

    # Adicionar gráfico ao PDF
    img = Image(buffer)
    elements.append(img)
    plt.close()

    # Conclusões e Recomendações
    elements.append(Paragraph("Conclusões e Recomendações", styles['Heading2']))
    elements.append(Paragraph("Baseado nos dados apresentados, recomenda-se focar nos produtos mais vendidos e analisar a performance dos métodos de pagamento para otimizar as estratégias de vendas.", styles['Normal']))

    # Construir o PDF
    doc.build(elements)
    buffer.close()
