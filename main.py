action = True
class Pizza:
    def __init__(self,name, price, vegetarienne=False):
        #Initialisation des variables
        self.name=name
        self.price=price
        self.vegetarienne=vegetarienne
        self.ingredients=[]
    
    # Fonction qui ajoute des ingredients :
    def ajoute(self,new):
        self.ingredients =self.ingredients + new

    # Fonction pour afficher la pizza :
    def afficher(self):
        print(f"La Pizza {self.name} coute {self.price}€")
        for inc in self.ingredients:
            print(f"\033[0m- {inc}")

    # Fonction qui gère la selection de l'utilisateur :
    def get_selection():
        valid_input = False
        while (valid_input is False):
            print()
            choice = input("Choisissez une action: ")
            if (Pizza.parse_int(choice) is True):
                return int(choice)
            else:
                print("Erreur veuillez reessayer.")
    # Check les erreurs sur la selection :
    def parse_int(input):
        try:
            int(input)
            return True
        except ValueError:
            return False
    # Check si la pizza est vegetarienne ou non  :
    def check_Vegetarienne(self):
        if self.vegetarienne:
            return True
        else:
            return False

# Seconde class qui hérite de la première :
class PizzaPersonnalise(Pizza):
    def __init__(self, name, price):
        Pizza.__init__(self, name, price)

    def NewIngredient(self):
        string = input('Ajouter un ingrédient à votre pizza personnalisé (ENTRER pour terminer) :')
        if string == "":
            return ""
        else:
            self.ingredients = self.ingredients + [string]
            self.price += 1.2
            return string


# On rempli la collection de pizza :
pizza1 = Pizza("Hawai", 9.5,True)
pizza1.ajoute(['tomate','ananas', 'oignons'])

pizza2 = Pizza("4 saisons", 11)
pizza2.ajoute(['Oeuf','Emmental', 'Tomate', 'Jambon', 'Olives'])

pizza3 = Pizza("Végétarienne", 7.8,True)
pizza3.ajoute(['Champignons', 'Tomate', 'Oignons', 'Poivrons'])

pizzas_instances = [pizza1, pizza2, pizza3]

# Check du choi de l'utilsateur avec des cas précis pour chaque :
while action:
    print("Choix disponibles:")
    print("1) Menu - Voir toute la carte.")
    print("2) Pizza - Choisir une pizza en particulié")
    print("3) Pizza - Créer votre propre pizza fait maison !")
    print("4) Pizza - Choisir une pizza vegetarienne !")
    print("5) Arreter")
    move = Pizza.get_selection()
    
    if(move ==1):
                print(f"\033[0m\033[4mLa liste de nos pizzas :\n")
                for i in range(len(pizzas_instances)):
                    pizzas_instances[i].afficher()
                    print("\n")

    elif(move == 2):
        number = int(input('Entrez le numéro de la pizza :'))

        if len(pizzas_instances) > number:
            print(f"Voici la pizza numéro {number} :\n")
            pizzas_instances[number].afficher()
            print("\n")
        else:
            print("Pizza non reconnue") 
    elif(move == 3):
        time = True
        pizza_custom = PizzaPersonnalise("Pizza personnalisé", 7)

        while time:
            step = pizza_custom.NewIngredient()
            if(step == ''):
                time = False          
        pizza_custom.afficher()
        pizzas_instances.append(pizza_custom)

    elif(move == 4):
        print(f"Toutes nos pizzas végétarienne sont ici : ")
        # Check avec boucle for entre l'instance et le check vegetarienne :
        for i in range(len(pizzas_instances)):
            if(pizzas_instances[i].check_Vegetarienne()) :
                pizzas_instances[i].afficher()

    elif(move == 5):
        print("Commande fini !\n")
        action = False
    
    else:
        print(f"erreur veuillez réessayer") 


