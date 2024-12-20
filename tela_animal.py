class TelaAnimal():
    def tela_inicial(self):
        print('----------ANIMAIS----------')
        print('1 - Incluir Cachorro')
        print('2 - Incluir Gato')
        print('3 - Alterar Animal')
        print('4 - Excluir Animal')
        print('5 - Mostrar Animal')
        print('6 - Listar Animais')
        print('7 - Listar Cachorros')
        print('8 - Listar Gatos')
        print('0 - Retornar')
        
        self.solicitar_input()
    
    
    def solicitar_input():
        opcao = input
        return opcao

    def dados_cachorro(self):
        print('----- DADOS ANIMAIS -----')
        nome = input('Nome: ')
        chip = input('Chip: ')
        raca = 'cachorro'
        porte = None
        hepatite = None
        leptospirose = None
        raiva = None
        data_aplicacao_H = None
        data_aplicacao_L = None
        data_aplicacao_R = None
        
        while porte != 'pequeno' and porte != 'médio' and porte != 'grande':
            porte = input('O animal é pequeno, médio ou grande?\n')


        while hepatite != bool:
            hepatite = input('Vacinado contra hepatite?\n')
            if hepatite == 'sim':
                hepatite = True
                data_aplicacao_H = input('Qual a data da aplicação?\n')
                resposta_H = 'sim'
            elif hepatite == 'não':
                hepatite = False
                resposta_H = 'não'
            else:
                print('Responda com *sim* ou *não*')
                
        
            
            


        while leptospirose != bool:
            leptospirose = input('Vacinado contra leptospirose?\n')
            if leptospirose == 'sim':
                leptospirose = True
                data_aplicacao_L = input('Qual a data da aplicação?\n')
                resposta_L = 'sim'
            elif leptospirose == 'não':
                leptospirose = False
                resposta_L = 'não'
            else:
                print('Responda com *sim* ou *não*')
            
        


        while raiva != bool:   
            raiva = input('Vacinado contra raiva?\n')
            if raiva == 'sim':
                raiva = True
                data_aplicacao_R = input('Qual a data da aplicação?\n')
                resposta_R = 'sim'
            elif raiva == 'não':
                raiva = False
                resposta_R = 'não'
            else:
                print('Responda com *sim* ou *não*')
        
        
        


        return{'Nome: ':nome, 'Chip: ':chip, 'Raca: ':raca, 'Porte ':porte, 'Vacinado contra leptospirose: ':resposta_H, 'Vacinado contra hepatete: ':resposta_L, 'Vacinado contra raiva: ': resposta_R}
        
    def dados_gato(self):
        print('----- DADOS ANIMAIS -----')
        nome = input('Nome: ')
        chip = input('Chip: ')
        raca = 'gato'
        porte = None
        hepatite = None
        leptospirose = None
        raiva = None
        data_aplicacao_H = None
        data_aplicacao_L = None
        data_aplicacao_R = None

        hepatite = None
        while hepatite != bool:
            hepatite = input('Vacinado contra hepatite?\n')
            if hepatite == 'sim':
                hepatite = True
                data_aplicacao_H = input('Qual a data da aplicação?\n')
                resposta_H = 'sim'
            elif hepatite == 'não':
                hepatite = False
                resposta_H = 'não'
            else:
                print('Responda com *sim* ou *não*')

        leptospirose = None
        while leptospirose != bool:
            leptospirose = input('Vacinado contra leptospirose?\n')
            if leptospirose == 'sim':
                leptospirose = True
                data_aplicacao_L = input('Qual a data da aplicação?\n')
                resposta_L = 'sim'
            elif leptospirose == 'não':
                leptospirose = False
                resposta_L = 'não'
            else:
                print('Responda com *sim* ou *não*')

        raiva = None
        while raiva != bool:   
            raiva = input('Vacinado contra raiva?\n')
            if raiva == 'sim':
                raiva = True
                data_aplicacao_R = input('Qual a data da aplicação?\n')
                resposta_R = 'sim'
            elif raiva == 'não':
                raiva = False
                resposta_R = 'não'
            else:
                print('Responda com *sim* ou *não*')

        return{'Nome: ':nome, 'Chip: ':chip, 'Raca: ':raca, 'Vacinado contra leptospirose: ':resposta_H, 'Vacinado contra hepatete: ':resposta_L, 'Vacinado contra raiva: ': resposta_R}
