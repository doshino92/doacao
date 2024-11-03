

class TelaAnimal():
    def opcoes(self):
        print('----------ANIMAIS----------')
        print('1 - Incluir Amigo')
        print('2 - Alterar Animal')
        print('3 - Excluir Animal')
        print('4 - Listar Animais')
        print('5 - Listar Cachorros')
        print('6 - Listar Gatos')
        print('0 - Retornar')
    
        opcao = int(input('Escolha a opcao: '))
        return opcao

    def dados_animais(self):
        print('----- DADOS ANIMAIS -----')
        nome = input('Nome: ')
        chip = input('Chip: ')
        cpf_daodor = input('CPF do doador: ')
        raca = None
        while raca != 'cachorro' and raca != 'gato':
            raca = input('Raca: ')
            if raca == 'cachorro':
                porte = input('Porte: ')
            elif raca =='gato':
                pass
            else:
                print('Responda com *cachorro* ou *gato*')
        
        hepatite = None
        while hepatite != bool:
            hepatite = input('Vacinado contra hepatite? \n')
            if hepatite == 'sim':
                hepatite = True
                resposta_H = 'sim'
            elif hepatite == 'não':
                hepatite = False
                resposta_H = 'não'
            else:
                print('Responda com *sim* ou *não*')
        
        leptospirose = None
        while leptospirose != bool:
            leptospirose = input('Vacinado contra leptospirose? \n')
            if leptospirose == 'sim':
                leptospirose = True
                resposta_L = 'sim'
            elif leptospirose == 'não':
                leptospirose = False
                resposta_L = 'não'
            else:
                print('Responda com *sim* ou *não*')
            
            
        raiva = None
        while raiva != bool:   
            raiva = input('Vacinado contra raiva? \n')
            if raiva == 'sim':
                raiva = True
                resposta_R = 'sim'
            elif raiva == 'não':
                raiva = False
                resposta_R = 'não'
            else:
                print('Responda com *sim* ou *não*')
        

        if raca == 'cachorro':
            return{'Nome: ':nome, 'Chip: ':chip, 'CPF: ':cpf_daodor, 'Raca: ':raca, 'Porte ':porte, 'Vacinado contra leptospirose: ':resposta_H, 'Vacinado contra hepatete: ':resposta_L, 'Vacinado contra raiva: ': resposta_R}
        
        else:
            return{'Nome: ':nome, 'Chip: ':chip, 'CPF: ':cpf_daodor, 'Raca: ':raca, 'Vacinado contra leptospirose: ':resposta_H, 'Vacinado contra hepatete: ':resposta_L, 'Vacinado contra raiva: ': resposta_R}
        
        
        