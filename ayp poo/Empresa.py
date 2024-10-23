import empleado
import tren

def calcular_totales_y_promedios(empleados):
    total_empleados = len(empleados)
    empleados_por_tren = {}
    empleados_con_aumento = 0
    promedio_pago_tren = {}

    for empleado in empleados:
        tipo_tren = empleado.tipo_tren
        if tipo_tren not in empleados_por_tren:
            empleados_por_tren[tipo_tren] = 1
            promedio_pago_tren[tipo_tren] = empleado.calcular_pago()
        else:
            empleados_por_tren[tipo_tren] += 1
            promedio_pago_tren[tipo_tren] = (promedio_pago_tren[tipo_tren] + empleado.calcular_pago()) / 2
        
        if empleado.horas_trabajadas > 8:
            empleados_con_aumento += 1
    
    return total_empleados, empleados_por_tren, empleados_con_aumento, promedio_pago_tren


def generar_reporte(totales_y_promedios):


    total_empleados, empleados_por_tren, empleados_con_aumento, promedio_pago_tren = totales_y_promedios

    print("Reporte de Nomina")
    print("-----------------")
    print(f"Cantidad total de empleados: {total_empleados}")
    print("Empleados por tipo de tren:")
    for tren, cantidad in empleados_por_tren.items():
        print(f"  {tren}: {cantidad} empleados")
    print(f"Empleados con aumento: {empleados_con_aumento}") 
    print("Promedio de pago por tipo de tren:")   
    for tren, promedio in promedio_pago_tren.items():
        print(f"   {tren}: {promedio}")
 
if __name__ == "__main__":
    resultados = calcular_totales_y_promedios(empleados)
    generar_reporte(resultados)
           