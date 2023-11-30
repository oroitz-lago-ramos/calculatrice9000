# Pour tenir compte des priorités de calcul nous pouvons utliser l'algorithme
# de Shunting-yard. Celui-ci me parait un peu compliqué pour la tache 
# et j'ai donc idéalisé une autre solution

#Pour le moment elle ne prends pas en compte les puissances ni parenthèses
#Plus bas j'implémenterais pour les parenthèses et puissance 
#puisqu'ils sont au meme niveau de priorité.
#Sachant que récupérer l'information entre parenthèses et un peu plus complexe


# def evaluer_expression(a, op, b):
#     if op == '*':
#         return a * b
#     elif op == '/':
#         return a / b
#     elif op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
    
# def calculer(expression):
#     elements = expression.split(" ")
#     for i in range(len(elements)):
#         if elements[i] == '*' or elements[i] == '/':
#             a = int(elements[i - 1])
#             op = elements[i]
#             b = int(elements[i + 1])
#             result = evaluer_expression(a, op, b)
#             elements[i-1:i+2] = [result]
#     result = 0
#     for i in range(len(elements)):
#         if elements[i] == '+' or elements[i] == '-':
#             a = int(elements[i - 1])
#             op = elements[i]
#             b = int(elements[i + 1])
#             result = evaluer_expression(a, op, b)
#             elements[i-1:i+2] = [result]
#     print(elements)

# # expression = input("Veuillez rentrer l'expression que vous souhaitez calculer")
# expression = "24 + 4 * 3"
# calculer(expression)

#Du fait que la liste elements change de taille j'ai une erreur de out of index et donc j'ai du rajouter un concept de stack
# Le problème que j'ai rencontré c'est que je ne pouvais pas mettre dans la stack le calcul prioritaire et ce qui avait avant sans
# la verfication, donc au final j'ai du me baser sur l'algorithme de shunting-yard pour en faire une version simplifié


# Cette fonction me servira pour calculer les elements de la liste avec l'index i i-1 et i+1
def evaluer_expression(a, op, b):
    if op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro n'est pas autorisée.")
        return a / b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    
def calculer(expression):
    
    expression = expression.strip()
    elements = expression.split(" ")
    
    valid = set(['*', '/', '+', '-'])
    for element in elements:
        if not element.isdigit() and element not in valid:
            print("Erreur: Expression invalide.")
            return
        
    # Cette liste servira pour stocker le début de la liste ainsi que le résultat
    stack = []
    
    i = 0
    while i < len(elements):
        # Si elements[i] est un opérateur on l'ajoute à la stack
        # Si stack n'est pas nul et que l'élement de stack à i-1 est un opérateur * ou / 
        # alors on efectue le calcul avec chiffre index i-2, opérateur i-1 et chiffre i
        # sinon, ça veut dire que elements[i] est un chiffre et on l'ajoute à la stack 
        
        if elements[i] in ['*', '/', '+', '-']:
            stack.append(elements[i])
        else:
            if len(stack) > 0 and stack[-1] in ['*', '/']:
                op = stack.pop()
                a = int(stack.pop())
                result = evaluer_expression(a, op, int(elements[i]))
                stack.append(result)
            else:
                stack.append(elements[i])  
        i += 1
    
    # Calculer le résultat final à partir de la pile
    # Il faut faire attention à mettre d'abord le b 
    # Sinon il pourrait fausser le résultat si c'est une soustraction
    result = 0
    while len(stack) > 1:
        b = int(stack.pop())
        op = stack.pop()
        a = int(stack.pop()) if stack else 0
        result = evaluer_expression(a, op, b)
        stack.append(result)
    
    print("Résultat :", stack[0])

expression = input("Veuillez rentrer l'expression que vous souhaitez calculer avec des espace entre chaque opérateur et chaque nombre\nOpérateurs permis * / + - : ")
# exemple : expression = "24 + 4 * 3 - 6 / 2 * 5"
calculer(expression)
