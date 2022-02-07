'''

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''
while True:
    try:
        tamanho_arquivo = float(input('Digite o tamanho do arquivo a ser baixado em MB: '))
        velocidade_internet = float(input('Digite a velocidade da sua internet em Mbps: '))

        conversao = tamanho_arquivo / (velocidade_internet / 8)
        minuto = conversao / 60


        print(f'O aquivo tem {tamanho_arquivo} e demorará cerca de {conversao} segundos, mais especificamnet, em cerca de {minuto:.1f} minutos.')
    except ValueError:
        print('Somente números')