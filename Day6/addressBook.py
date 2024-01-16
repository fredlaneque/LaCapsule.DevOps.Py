# ADDRESS BOOK
#
# L’objectif de ce challenge est de créer un ensemble de classes permettant de construire un carnet d’adresses.
#
# 👉 Initialisez une classe Person(), permettant d’instancier des objets à partir d’attributs lastname, firstname, 
# phone et mail. L’objet disposera également de la méthode __repr__ pour imprimer les informations de la personne.
#
# 👉 Initialisez une classe Work(), permettant d’instancier des objets à partir d’attributs lastname, firstname, 
# phone, mail, company, address et company_phone. 
# L’objet disposera également de la méthode __repr__ pour imprimer les informations de la personne et de son travail.
#
# 👉 Initialisez une classe Dev(), permettant d’instancier des objets à partir d’attributs lastname, firstname, 
# phone, mail, company, address, company_phone, languages (sous forme de liste) et preferred_stack ("backend" ou "frontend"). 
# L’objet disposera également de la méthode __repr__ pour imprimer les informations de la personne, 
# de son travail et de ses préférences de dev.
#
# Mise en place du carnet
#
# 👉 Initialisez une classe Contacts(), qui contiendra un ensemble d’objets sous forme de liste 
# (des objets de Person, Work ou Dev, peu importe). Associez à Contacts une méthode __init__ ne prenant pas d’arguments, 
# permettant simplement d’initialiser une instance, et une méthode __repr__ permettant d’afficher 
# le contenu de l’instance sous forme de chaîne de caractères.
#
# 👉 Ajoutez à votre classe Contacts une méthode add_contact permettant d’ajouter un contact 
# à partir d’une instance de Person, une méthode search_contact permettant de trouver un contact 
# à partir de son nom (argument obligatoire) et de son prénom (argument optionnel) 
# si plusieurs contacts ont le même nom dans le carnet d’adresses, une méthode remove_contact #
# permettant de supprimer un contact du carnet en connaissant son nom et son prénom.

class Person:
    def __init__(self, lastname, firstname, phone, mail):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.mail = mail

    def __repr__(self):
        return f"\tLastname: {self.lastname}, \tFirstname: {self.firstname}, \tPhone: {self.phone}, \tEmail: {self.mail}"

class Work(Person):
    def __init__(self, lastname, firstname, phone, mail, company, address, company_phone):
        super().__init__(lastname, firstname, phone, mail)
        self.company = company
        self.address = address
        self.company_phone = company_phone

    def __repr__(self):
        return f"WORK{super().__repr__()}\n, \tCompany: {self.company}, \tAddress: {self.address}, \tCompany Phone: {self.company_phone}"

class Dev(Work):
    def __init__(self, lastname, firstname, phone, mail, company, address, company_phone, languages, preferred_stack):
        super().__init__(lastname, firstname, phone, mail, company, address, company_phone)
        self.languages = languages
        self.preferred_stack = preferred_stack

    def __repr__(self):
        return f"DEV{super().__repr__()}\n, \tLanguages: {self.languages}, \tPreferred Stack: {self.preferred_stack}"

class Contacts:
    def __init__(self):
        self.contacts_list = []

    def __repr__(self):
        return '\n'.join(str(contact) for contact in self.contacts_list)

    def add_contact(self, contact):
        self.contacts_list.append(contact)

    def search_contact(self, lastname, firstname=None):
        found_contacts = [contact for contact in self.contacts_list if contact.lastname == lastname and (firstname is None or contact.firstname == firstname)]
        return found_contacts

    def remove_contact(self, lastname, firstname):
        self.contacts_list = [contact for contact in self.contacts_list if not (contact.lastname == lastname and contact.firstname == firstname)]

def main():
    my_contacts = Contacts()

    while True:
        print("\nMenu du Carnet d'Adresses")
        print("1. Ajouter un contact")
        print("2. Rechercher un contact")
        print("3. Supprimer un contact")
        print("4. Afficher tous les contacts")
        print("5. Quitter")
        choice = input("Entrez votre choix (1-5): ")

        if choice == "1":
            add_contact_to_list(my_contacts)
        elif choice == "2":
            search_contact_in_list(my_contacts)
        elif choice == "3":
            remove_contact_from_list(my_contacts)
        elif choice == "4":
            print(my_contacts)
        elif choice == "5":
            print("Sortie du programme.")
            break
        else:
            print("Choix invalide, réessayez.")

def add_contact_to_list(contacts):
    type_contact = input("Type de contact (person, work, dev): ").lower()
    lastname = input("Nom de famille: ")
    firstname = input("Prénom: ")
    phone = input("Téléphone: ")
    mail = input("Email: ")

    if type_contact == "person":
        contacts.add_contact(Person(lastname, firstname, phone, mail))
    elif type_contact == "work":
        company = input("Entreprise: ")
        address = input("Adresse: ")
        company_phone = input("Téléphone de l'entreprise: ")
        contacts.add_contact(Work(lastname, firstname, phone, mail, company, address, company_phone))
    elif type_contact == "dev":
        company = input("Entreprise: ")
        address = input("Adresse: ")
        company_phone = input("Téléphone de l'entreprise: ")
        languages = input("Langues parlées (séparées par une virgule): ").split(',')
        preferred_stack = input("Stack préférée (backend/frontend): ")
        contacts.add_contact(Dev(lastname, firstname, phone, mail, company, address, company_phone, languages, preferred_stack))
    else:
        print("Type de contact non reconnu.")

def search_contact_in_list(contacts):
    lastname = input("Nom de famille du contact à rechercher: ")
    firstname = input("Prénom: ")
    found_contacts = contacts.search_contact(lastname, firstname)
    if found_contacts:
        print("Contacts trouvés:")
        for contact in found_contacts:
            print(contact)
    else:
        print("Aucun contact trouvé.")

def remove_contact_from_list(contacts):
    lastname = input("Nom de famille du contact à supprimer: ")
    firstname = input("Prénom: ")
    contacts.remove_contact(lastname, firstname)
    print(f"Contact {firstname} {lastname} supprimé.")

if __name__ == "__main__":
    main()