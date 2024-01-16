from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your routes here

def first_route(request):
    return JsonResponse({ "successful": True })

def message(request):
    return JsonResponse({ "answer": "Hello, world!" })

def calc_square(request, number):
    square = number * number
    return JsonResponse({ "result": square })

def concat(request, str1, str2):
    concat_result = f"{str1} {str2}" 
    return JsonResponse({ "result": concat_result })

@csrf_exempt
def json_route(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            employees = data.get('employees', [])
            student_names = [employee['name'] for employee in employees if employee.get('status') == 'student']
            return JsonResponse( {"student_names": student_names} )
        except json.JSONDecodeError as e:
            return JsonResponse( {"error": "Ce format JSON est invalide"}, status=400 )
    else:
        return JsonResponse( {"error": "Cette methode n'est pas authorisée"}, status=405 )

@csrf_exempt    
def fill(request):
    if request.method == 'POST':
        try:
            #Recupère le contenu
            content = request.body.decode('utf-8')
            # Ouvre le fichier data pour y ecrire le contenu
            with open('data.txt', 'a') as file:
                file.write(content)
            return JsonResponse( {"success": True} )
        except json.JSONDecodeError as e:
            return JsonResponse( {"error": str(e)}, status=500 )
    else:
        return JsonResponse( {"error": "Cette methode n'est pas authorisée"}, status=405 )
    
@csrf_exempt   
def upload_route(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        response_data = {
            "name": uploaded_file.name,
            "type": uploaded_file.content_type,
            "size": uploaded_file.size
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse( {"error": "La requete est invalide"}, status=400 )
    
@csrf_exempt
def process_advanced_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Convertit la chaîne JSON en un dictionnaire Python
            employees = data.get('employees', [])

            # Créez des dictionnaires pour stocker les employés par statut
            employee_groups = {'admin': [], 'student': [], 'teacher': []}

            for employee in employees:
                status = employee.get('status', '')
                age = employee.get('age', 0)
                name = employee.get('name', '')

                # Ajoutez l'employé au groupe approprié
                employee_groups[status].append({'name': name, 'age': age})

            # Calculez la moyenne d'âge et la liste des noms pour chaque groupe
            result = {}
            for status, employees in employee_groups.items():
                if employees:
                    total_age = sum([employee['age'] for employee in employees])
                    average_age = total_age / len(employees)
                    names = [employee['name'] for employee in employees]
                    result[status] = {'average_age': average_age, 'names': names}

            return JsonResponse(result)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)