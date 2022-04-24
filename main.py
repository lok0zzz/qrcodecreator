import qrcode

import randomwordsgenerator

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

if __name__ == '__main__':
    print('Olá, deseja executar esse programa?\n\n')
    print('====================================================')
    print(' Y. Criar QR code')
    print(' N. Fechar')
    print('====================================================')
    awnser = input(' • ')

    try:
        if awnser.lower() == 'y':
            print('====================================================')
            print('Qual o link que deve ser gerado seu QR code? (ex: https://google.com.br/)')
            print('====================================================')
            qr_code_link = input(' • ')
            if awnser:
                qr.add_data(qr_code_link)
                qr.make(fit=True)

                name = randomwordsgenerator.gerarValorRandomico()
                try:
                    img = qr.make_image()
                    img.save(f'{name}.jpg')
                    print('====================================================')
                    print(f'\n\n\n\n\n\nQR code criado com sucesso | NOME: {name}.jpg')
                except Exception as e:
                    print(e)

            else:
                print('====================================================')
                print('Coloque um link válido')
                print('====================================================')

        elif awnser.lower() == 'n':
            print('====================================================')
            print('Programa encerrado')
            print('====================================================')
            pass
        else:
            print('====================================================')
            print('Erro | Verifique se o número digitado está correto')
            print('====================================================')
    except Exception as e:
        print('====================================================')
        print('Algum erro no programa aconteceu, tente novamente')
        print(e)
        print('====================================================')
