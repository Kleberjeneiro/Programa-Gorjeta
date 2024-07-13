print('#####################################')
print('####       Programa Gorjeta       ###')                
print('#####################################')
print('')
valor_meta = 100
valor_meta1 = 150
valor_meta2 = 160

nome_garcon = input('Nome do Garçon: ')
valor_pedido = input('Valor do Pedido: R$ ')

if nome_garcon and valor_pedido:
    valor_pedido = float(valor_pedido)
    if valor_meta <= valor_pedido < valor_meta2:
        bonus = valor_pedido * 0.01
        print(f'{nome_garcon}, recebeu desse pedido R$ {bonus:.2f} de bônus')
    elif valor_pedido >= valor_meta2:
        bonus = valor_pedido * 0.02
        print(f'{nome_garcon}, recebeu desse pedido R$ {bonus:.2f} de bônus 0.02') 
    else:
        bonus = 0
        print(f'{nome_garcon}, recebeu desse pedido R$ {bonus:.2f} de bônus')
else:
    print('Preencha todas as informações')
print('')
print('#####################################')
print('####       Programa Gorjeta       ###')                
print('#####################################')    