class Task:
    def __init__(self, title, description, due_date, status="Non commencée"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"Task({self.title}, {self.description}, {self.due_date}, {self.status})"

class TaskManager:
    def __init__(self):
        # Initialisation de la liste des tâches vide
        self.tasks = []

    def add_task(self, title, description, due_date, status="Non commencée"):
        # Méthode pour ajouter une nouvelle tâche
        # Les paramètres : title (titre), description (description de la tâche), due_date (date d'échéance), status (statut de la tâche)
        # Par défaut, le statut est "Non commencée"
        task = Task(title, description, due_date, status)  # Création d'une instance de la classe Task
        self.tasks.append(task)  # Ajout de la tâche à la liste des tâches

    def list_tasks(self):
        # Méthode pour afficher la liste des tâches
        for task in self.tasks:
            # Parcours de la liste des tâches
            print(f"Titre: {task.title}")  # Affichage du titre de la tâche
            print(f"Description: {task.description}")  # Affichage de la description de la tâche
            print(f"Date d'échéance: {task.due_date}")  # Affichage de la date d'échéance de la tâche
            print(f"Statut: {task.status}")  # Affichage du statut de la tâche
            print()  # Ligne vide pour séparer les tâches dans l'affichage

    def update_task(self, title, new_title=None, new_description=None, new_due_date=None, new_status=None):
        # Méthode pour mettre à jour une tâche existante
        # Les paramètres : title (titre de la tâche à mettre à jour), new_title (nouveau titre),
        # new_description (nouvelle description), new_due_date (nouvelle date d'échéance), new_status (nouveau statut)
        for task in self.tasks:
            # Parcours de la liste des tâches
            if task.title == title:
                # Si le titre de la tâche correspond au titre spécifié
                if new_title is not None:
                    task.title = new_title  # Mise à jour du titre
                if new_description is not None:
                    task.description = new_description  # Mise à jour de la description
                if new_due_date is not None:
                    task.due_date = new_due_date  # Mise à jour de la date d'échéance
                if new_status is not None:
                    task.status = new_status  # Mise à jour du statut

    def delete_task(self, title):
        # Méthode pour supprimer une tâche
        # Le paramètre : title (titre de la tâche à supprimer)
        self.tasks = [task for task in self.tasks if task.title != title]
        # Crée une nouvelle liste de tâches en excluant la tâche avec le titre spécifié

# Exemple d'utilisation :
task_manager = TaskManager()  # Création d'une instance de TaskManager
task_manager.add_task("Faire les courses", "Acheter des légumes et du lait", "2022-01-30", "En cours")
task_manager.add_task("Réunion", "Réunion d'équipe à 14h", "2022-02-05", "Non commencée")

task_manager.list_tasks()  # Affiche la liste des tâches
task_manager.update_task("Faire les courses", new_status="Terminée")  # Met à jour le statut d'une tâche
task_manager.list_tasks()  # Affiche la liste des tâches mise à jour
task_manager.delete_task("Réunion")  # Supprime une tâche
task_manager.list_tasks()  # Affiche la liste des tâches après suppression