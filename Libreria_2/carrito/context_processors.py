def importe_total_carro(request):
    subtotal = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session["carro"].items():
                subtotal = subtotal + (float(value["precio"]))

    impuesto = subtotal*0.15
    total = subtotal + impuesto

    # Redondear los tres valores
    subtotal = round(subtotal, 2)
    impuesto = round(impuesto, 2)
    total = round(total, 2)

                             
    return {"importe_total_carro": total , "subtotal_compra": subtotal , "impuesto":impuesto}