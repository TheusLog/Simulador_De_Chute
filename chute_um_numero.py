import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        # Layout
        self.layout = [
            [sg.Text('Seu Chute',size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40,10))]
        ]
    
    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Chute o Numero',layout=self.layout)
        self.gerar_numero_aleatorio()
        
        try:
            while True:
                # receber os valores
                self.eventos, self.valores = self.janela.Read()
                # fazer alguma coisa com estes valores
                if self.eventos == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']

                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor menor!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('chute um valor maior!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABENS VOÇE ACERTOU')
                            break
        except:
            print('Favor Digitar apenas numeros!')
            self.Iniciar()

    def gerar_numero_aleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()